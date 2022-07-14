from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import time
import datetime 
import pytz
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder
import pyttsx3
import wikipedia
import sqlite3
import random

help_str = '''
ScreenManager:
	WelcomeScreen:
	MainScreen:
	WeatherFunction:
	SearchScreen
<WelcomeScreen>:
	name:'welcomescreen'
	canvas.before:
		Color:
			rgba: 1,1,1,1
		Rectangle:
			pos: self.pos
			size: self.size	
	Image:
		source: 'erwin_1.png'
		allow_stretch: True
		kepp_ratio: True 
		pos_hint: {'center_x':0.5,'center_y':0.6}
		size_hint: (0.8,0.8)

	MDRaisedButton:
		text:'Inicialize'
		pos_hint : {'center_x':0.5,'center_y':0.15}
		size_hint: (0.13,0.08)
		md_bg_color: 10/255,10/255,10/255,1
		on_press: 
			root.manager.current = 'mainscreen'
			root.manager.transition.direction = 'left'
<MainScreen>:
	name: 'mainscreen'
	canvas.before:
		Color:
			rgba: 1,1,1,1
		Rectangle:
			pos: self.pos
			size: self.size	
	Image:
		source: 'erwin_1.png'
		allow_stretch: True
		kepp_ratio: True 
		pos_hint: {'center_x':0.8,'center_y':0.9}
		size_hint: (0.3,0.3)
		
		

	MDLabel:
		id:greeting
		text:'Welcome User'
		theme_text_color: 'Custom'
		text_color: 10/255,10/255,10/255,1
		font_style:'H1'
		halign:'center'

	MDRaisedButton:
		text:'Weather'
		pos_hint : {'center_x':0.4,'center_y':0.15}
		size_hint: (0.13,0.08)
		md_bg_color: 10/255,10/255,10/255,1
		on_press: 
			root.manager.current = 'weatherfunction'
			root.manager.transition.direction = 'left'

	MDRaisedButton:
		text:'WebSearch'
		pos_hint : {'center_x':0.6,'center_y':0.15}
		size_hint: (0.13,0.08)
		md_bg_color: 10/255,10/255,10/255,1
		on_press: 
			root.manager.current = 'searchscreen'
			root.manager.transition.direction = 'left'

	MDRaisedButton:
		text:'Quit'
		pos_hint : {'center_x':0.1,'center_y':0.9}
		size_hint: (0.13,0.08)
		md_bg_color: 10/255,10/255,10/255,1
		on_press: app.quit_program()
			
<SearchScreen>:
	name: 'searchscreen'
	canvas.before:
		Color:
			rgba: 1,1,1,1
		Rectangle:
			pos: self.pos
			size: self.size 
	MDLabel:
		id:my_search
		text:'Search'
		pos_hint: {'center_y':0.5,'center_x':0.5}
		theme_text_color: 'Custom'
		text_color: 10/255,10/255,10/255,1
		font_style:'H2'
		halign:'center'

	MDTextField:
		id:search_get
		pos_hint: {'center_y':0.8,'center_x':0.5}
		size_hint : (0.7,0.1)
		hint_text: 'Topic'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account'
		icon_right_color: 10/255,10/255,10/255,1
		required: True
		line_color_focus:  10/255,10/255,10/255,1
		mode: "rectangle"
		
	MDRaisedButton:
		id: get_search
		text:'Search'
		size_hint: (0.13,0.07)
		md_bg_color: 10/255,10/255,10/255,1
		pos_hint: {'center_x':0.5,'center_y':0.2}
		on_press: app.search_get()

	MDRaisedButton:
		id:back_menu 
		text:'Main Menu'
		pos_hint : {'center_x':0.2,'center_y':0.9}
		size_hint: (0.13,0.08)
		md_bg_color: 10/255,10/255,10/255,1
		on_press: 
			root.manager.current = 'mainscreen'
			root.manager.transition.direction = 'right'
			

<WeatherFunction>:
	name: 'weatherfunction'
	canvas.before:
		Color:
			rgba: 1,1,1,1
		Rectangle:
			pos: self.pos
			size: self.size 
	MDLabel:
		id:my_get
		text:'Weather'
		pos_hint: {'center_y':0.5,'center_x':0.5}
		theme_text_color: 'Custom'
		text_color: 10/255,10/255,10/255,1
		font_style:'H2'
		halign:'center'

	MDTextField:
		id:weather_get
		pos_hint: {'center_y':0.8,'center_x':0.5}
		size_hint : (0.7,0.1)
		hint_text: 'Location'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account'
		icon_right_color: 10/255,10/255,10/255,1
		required: True
		line_color_focus:  10/255,10/255,10/255,1
		mode: "rectangle"
		
	MDRaisedButton:
		id: get_temp
		text:'Get Temp'
		size_hint: (0.13,0.07)
		md_bg_color: 10/255,10/255,10/255,1
		pos_hint: {'center_x':0.5,'center_y':0.2}
		on_press: app.weather_get()

	MDRaisedButton:
		id:back_menu 
		text:'Main Menu'
		pos_hint : {'center_x':0.2,'center_y':0.9}
		size_hint: (0.13,0.08)
		md_bg_color: 10/255,10/255,10/255,1
		on_press: 
			root.manager.current = 'mainscreen'
			root.manager.transition.direction = 'right'

		

'''

class WelcomeScreen(Screen):
	pass
class MainScreen(Screen):
	pass
class WeatherFunction(Screen):
	pass
class SearchScreen(Screen):
	pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(WeatherFunction(name = 'weatherfunction'))
sm.add_widget(SearchScreen(name='searchscreen'))

class Erwin(MDApp):
	def build(self):
		self.strng = Builder.load_string(help_str)
		return self.strng

	def weather_get(self):
		try:
			location = self.strng.get_screen('weatherfunction').ids.weather_get.text

			api_complete_link = 'https://api.openweathermap.org/data/2.5/weather?q='+ location +'&appid=08c43f1245cecfbb6611738969af6544'
			api_link = requests.get(api_complete_link)
			api_data = api_link.json()
			temp_in_celcius = int(api_data['main']['temp']) - 273

			time.sleep(1.5)
			
			result = (f'The temperature in {location} is: {temp_in_celcius}°C')
			self.strng.get_screen('weatherfunction').ids.my_get.text = result
		except KeyError:
			city_error = 'Please, enter a valid location'
			self.strng.get_screen('weatherfunction').ids.my_get.text = city_error

		except requests.exceptions.ConnectionError:
			connection_error = 'Connection Failed'
			self.strng.get_screen('weatherfunction').ids.my_get.text = connection_error

	def search_get(self):
		try:
			command = self.strng.get_screen('searchscreen').ids.search_get.text
			topic = command.replace("wikipedia", "")
				# it will limit the summary to four lines
			result = wikipedia.summary(topic, sentences=2, auto_suggest=False)
			print(result)
			self.strng.get_screen('searchscreen').ids.my_search.text = result
			self.strng.get_screen('searchscreen').ids.my_search.font_style = 'Body1'
		except wikipedia.DisambiguationError as e:
			next_topic = random.choice(e.options)
			new_result = wikipedia.summary(next_topic, sentences=2, auto_suggest=False)
			print(new_result)
			self.strng.get_screen('searchscreen').ids.my_search.text = new_result
			self.strng.get_screen('searchscreen').ids.my_search.font_style = 'Body1'
		except KeyError:
			self.strng.get_screen('searchscreen').ids.my_search.text = 'Please, check your spelling or be sure to put a real value'
		except requests.exceptions.ConnectionError:
			connection_error = 'Connection Failed'
			self.strng.get_screen('searchscreen').ids.my_search.text = connection_error

	def quit_program():
		Erwin().exit()        



Erwin().run()