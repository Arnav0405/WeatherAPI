# main.
import requests
import os

from dotenv import load_dotenv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 0]

        self.location_input = TextInput(hint_text='Enter location')
        self.add_widget(self.location_input)

        self.get_weather_button = Button(text='Get Weather', on_press=self.get_weather)
        self.add_widget(self.get_weather_button)

        self.weather_label = Label(text='')
        self.add_widget(self.weather_label)


    def get_weather(self, instance):
        # Fetch weather data here
        # Update self.weather_label.text with the weather 
        location = self.location_input.text
        #Getting information from the dotenv file
        load_dotenv()
        apikey = os.getenv("WeatherAPIKey")
        params = {
                'access_key': apikey,
                'query': f'{location}'
                }

        api_url = 'http://api.weatherstack.com/current'
        response = requests.get(api_url, params)

        try:
            data = response.json()

            weather_description = data['current']["weather_descriptions"]
            temperature = data['current']['temperature']

            weather_info = f'Weather: {weather_description}, Temperature: {temperature}°C'
            self.weather_label.text = weather_info
            
        except KeyError:
            print(f'Key Error')
            print(data)
            self.weather_label.text = 'Error fetching weather data'
            pass
        

class WeatherApp(App):
    def build(self):
        return MyApp()

if __name__ == '__main__':
    WeatherApp().run()
