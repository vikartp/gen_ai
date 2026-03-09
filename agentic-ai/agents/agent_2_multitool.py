# file: agent_2_multitool.py
import os
import requests
import yfinance as yf
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults  # Built-in
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

model = ChatOpenAI(
    # model="gpt-4o-mini", #Open router
    model="gpt-5.1", # Model zoo
    temperature=0, # Deterministic for testing, change to 1 for more creativity
    base_url= OPENAI_API_BASE
)

search = DuckDuckGoSearchResults()  # Real search!

@tool
def calculate_profit(revenue: float, cost: float) -> float:
    """Calculate profit from revenue and cost."""
    return revenue - cost

@tool
def get_weather(location: str) -> str:
    """Get real-time weather information for a given city or location using Open-Meteo (free, no API key).

    Previously used wttr.in API (https://wttr.in/<city>?format=j1) which returned:
      data["current_condition"][0]  -> temp_C, temp_F, FeelsLikeC, humidity, windspeedKmph, weatherDesc[0]["value"]
      data["nearest_area"][0]       -> areaName[0]["value"], country[0]["value"]
    Switched to Open-Meteo due to frequent timeouts and blocking of non-browser User-Agents.
    """
    import time

    # WMO weather code descriptions
    WMO_CODES = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Icy fog", 51: "Light drizzle", 53: "Moderate drizzle",
        55: "Dense drizzle", 61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow", 77: "Snow grains",
        80: "Slight showers", 81: "Moderate showers", 82: "Violent showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
    }

    try:
        # Step 1: Geocode the location
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={requests.utils.quote(location)}&count=1&language=en&format=json"
        print(f"[weather] Geocoding: {geo_url}")
        t0 = time.time()
        geo_resp = requests.get(geo_url, timeout=10)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        print(f"[weather] Geocode response in {time.time()-t0:.2f}s")

        if not geo_data.get("results"):
            return f"Could not find location: '{location}'. Please try a different city name."

        place = geo_data["results"][0]
        lat, lon = place["latitude"], place["longitude"]
        city_name = place.get("name", location)
        country = place.get("country", "")
        print(f"[weather] Resolved '{location}' → {city_name}, {country} ({lat}, {lon})")

        # Step 2: Fetch current weather
        wx_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,"
            f"weather_code,wind_speed_10m,wind_direction_10m,precipitation"
            f"&timezone=auto"
        )
        print(f"[weather] Weather URL: {wx_url}")
        t1 = time.time()
        wx_resp = requests.get(wx_url, timeout=10)
        wx_resp.raise_for_status()
        wx_data = wx_resp.json()
        print(f"[weather] Weather response in {time.time()-t1:.2f}s")

        curr = wx_data["current"]
        temp_c = curr["temperature_2m"]
        feels_c = curr["apparent_temperature"]
        humidity = curr["relative_humidity_2m"]
        wind_kmph = curr["wind_speed_10m"]
        precip = curr["precipitation"]
        wmo = curr["weather_code"]
        description = WMO_CODES.get(wmo, f"Weather code {wmo}")
        temp_f = round(temp_c * 9 / 5 + 32, 1)

        result = (
            f"Weather in {city_name}, {country}: {description}. "
            f"Temperature: {temp_c}°C / {temp_f}°F (feels like {feels_c}°C). "
            f"Humidity: {humidity}%. Wind: {wind_kmph} km/h. Precipitation: {precip} mm."
        )
        print(f"[weather] Result: {result}")
        return result

    except requests.exceptions.Timeout:
        print(f"[weather] TIMEOUT for location='{location}'")
        return f"Could not fetch weather for '{location}': request timed out. Try again."
    except Exception as e:
        print(f"[weather] ERROR: {type(e).__name__}: {e}")
        return f"Could not fetch weather for '{location}': {type(e).__name__}: {e}"

@tool
def get_stock_info(symbol: str) -> str:
    """
    Get real-time stock market data for any stock.
    For Indian stocks use NSE symbols with .NS suffix (e.g. RELIANCE.NS, TCS.NS, INFY.NS).
    For BSE use .BO suffix (e.g. RELIANCE.BO).
    For US stocks use plain symbols (e.g. AAPL, TSLA).
    Returns price, change, 52-week range, market cap, P/E ratio, volume and more.
    """
    print(f"[stock] Fetching data for symbol='{symbol}'")
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info
        full = ticker.info

        name = full.get("longName") or full.get("shortName", symbol)
        currency = full.get("currency", "")
        exchange = full.get("exchange", "")

        current_price = info.last_price
        prev_close = info.previous_close
        change = current_price - prev_close
        change_pct = (change / prev_close) * 100 if prev_close else 0

        week_52_high = info.year_high
        week_52_low = info.year_low
        market_cap = full.get("marketCap")
        pe_ratio = full.get("trailingPE")
        volume = info.last_volume
        avg_volume = full.get("averageVolume")
        day_high = info.day_high
        day_low = info.day_low

        def fmt_cap(val):
            if val is None: return "N/A"
            if val >= 1e12: return f"{val/1e12:.2f}T"
            if val >= 1e9:  return f"{val/1e9:.2f}B"
            if val >= 1e7:  return f"{val/1e7:.2f}Cr"  # Indian crore
            return str(val)

        result = (
            f"{name} ({symbol}) | Exchange: {exchange} | Currency: {currency}\n"
            f"Current Price : {current_price:.2f} | Change: {change:+.2f} ({change_pct:+.2f}%)\n"
            f"Day Range     : {day_low:.2f} — {day_high:.2f}\n"
            f"52-Week Range : {week_52_low:.2f} — {week_52_high:.2f}\n"
            f"Market Cap    : {fmt_cap(market_cap)} {currency}\n"
            f"P/E Ratio     : {pe_ratio if pe_ratio else 'N/A'}\n"
            f"Volume        : {volume:,} (Avg: {avg_volume:,})" if avg_volume else f"Volume: {volume:,}"
        )
        print(f"[stock] Result: {result}")
        return result
    except Exception as e:
        print(f"[stock] ERROR for symbol='{symbol}': {type(e).__name__}: {e}")
        return (
            f"Could not fetch stock data for '{symbol}': {type(e).__name__}: {e}. "
            f"Make sure to use correct suffix: .NS for NSE India, .BO for BSE India, no suffix for US stocks."
        )

tools = [search, calculate_profit, get_weather, get_stock_info]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "You have access to search, calculator, weather, and stock market tools. "
        "For Indian stocks always append .NS for NSE or .BO for BSE to the ticker symbol. "
        "Use search for general facts, calculator for math, weather for location queries, "
        "and get_stock_info for any stock market question. Reason step-by-step."
    )
)

# --- Questions to ask the agent ---
# Add or remove questions here; they will be joined into a single prompt automatically.
questions = [
    "What is the current stock price of Reliance Industries and TCS?",
    "What's the weather in Bangalore?",
    "Search the latest LangChain version over the web.",
    "How do we fine tune a language model on custom data?",
    "If revenue is $500k and cost is $350k, what's the profit?",
]

combined_prompt = " ".join(questions)
print(f">>> Prompt: {combined_prompt}\n")

inputs = {
    "messages": [("user", combined_prompt)]
}
count = 0
for chunk in agent.stream(inputs, stream_mode="updates"):
    count += 1
    print('>>> Received chunk number:', count)  # Debug line to see all chunks
    if "model" in chunk:
        print(chunk["model"]["messages"][-1].content)
