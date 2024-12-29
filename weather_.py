import tkinter as tk
from tkinter import ttk, messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")

        # Create variables to store user input
        self.location_var = tk.StringVar()

        # Create labels and entry widgets
        location_label = ttk.Label(root, text="Enter Location:")
        self.location_entry = ttk.Entry(root, textvariable=self.location_var)

        # Create buttons
        get_weather_button = ttk.Button(root, text="Get Weather", command=self.get_weather)

        # Create labels to display weather information
        self.temperature_label = ttk.Label(root, text="")
        self.humidity_label = ttk.Label(root, text="")
        self.wind_speed_label = ttk.Label(root, text="")
        self.rain_chances_label = ttk.Label(root, text="")
        self.pressure_label = ttk.Label(root, text="")

        # Grid configuration
        location_label.grid(row=0, column=0, padx=10, pady=10)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)
        get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.temperature_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.humidity_label.grid(row=3, column=0, columnspan=2, pady=10)
        self.wind_speed_label.grid(row=4, column=0, columnspan=2, pady=10)
        self.rain_chances_label.grid(row=5, column=0, columnspan=2, pady=10)
        self.pressure_label.grid(row=6, column=0, columnspan=2, pady=10)

    def get_weather(self):
        location = self.location_var.get()
        if not location:
            messagebox.showinfo("Error", "Please enter a location.")
            return

        api_key = "4604f7378fd3c9831338a005171a2835"# Replace with your actual API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": location, "units": "metric", "appid": api_key}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            # Print the entire JSON response for debugging
            print(data)

            # Check if the 'main' key is present in the response
            if 'main' not in data:
                messagebox.showinfo("Error", "Invalid response format. Check the console for details.")
                return

            # Access weather information
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            rain_chances = data["clouds"]["all"]
            pressure = data["main"]["pressure"]

            # Update labels with weather information
            self.temperature_label.config(text=f"Temperature: {temperature}°C")
            self.humidity_label.config(text=f"Humidity: {humidity}%")
            self.wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
            self.rain_chances_label.config(text=f"Chances of Rain: {rain_chances}%")
            self.pressure_label.config(text=f"Pressure: {pressure} hPa")

        except requests.exceptions.RequestException as e:
            messagebox.showinfo("Error", f"Error fetching weather data: {e}")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


