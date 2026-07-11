"""Weather API client using the free Open-Meteo geocoding and forecast APIs."""

import requests


class WeatherService:
    """Retrieve current weather without requiring an API key."""

    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
    WEATHER_CODES = {0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
                     45: "Fog", 48: "Rime fog", 51: "Light drizzle", 53: "Drizzle",
                     55: "Heavy drizzle", 61: "Light rain", 63: "Rain", 65: "Heavy rain",
                     71: "Light snow", 73: "Snow", 75: "Heavy snow", 80: "Rain showers",
                     81: "Rain showers", 82: "Violent rain showers", 95: "Thunderstorm"}

    def get_weather(self, city: str) -> dict[str, str | float | int]:
        """Return the current weather details for *city*."""
        try:
            place_response = requests.get(self.GEO_URL, params={"name": city, "count": 1}, timeout=10)
            place_response.raise_for_status()
            places = place_response.json().get("results", [])
            if not places:
                raise RuntimeError("City not found.")
            place = places[0]
            weather_response = requests.get(
                self.WEATHER_URL,
                params={"latitude": place["latitude"], "longitude": place["longitude"], "current": "temperature_2m,relative_humidity_2m,weather_code"},
                timeout=10,
            )
            weather_response.raise_for_status()
            current = weather_response.json()["current"]
        except requests.RequestException as error:
            raise RuntimeError("Check your internet connection and try again.") from error
        except (KeyError, ValueError) as error:
            raise RuntimeError("The weather service returned an unexpected response.") from error
        return {"city": place["name"], "temperature": current["temperature_2m"],
                "humidity": current["relative_humidity_2m"],
                "condition": self.WEATHER_CODES.get(current["weather_code"], "Unknown")}
