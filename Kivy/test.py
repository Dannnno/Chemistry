import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.event import EventDispatcher

import sys

class outputLabel(EventDispatcher):
	text = StringProperty('')

	def __init__(self, **kwargs):
		super(outputLabel, self).__init__(**kwargs)
		self.text = "Hi"

	def write(self, text):
		self.text = text
		
out = outputLabel
sys.stdout = out
		
class myButton(Button):

	def __init__(self, **kwargs):
		super(myButton, self).__init__(**kwargs)
		
	def on_press(self, event):
		print "Hello World"
		
class RootWidget(Widget): 

	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)


class myApp(App):
    
    def build(self):
        global rw
        rw = RootWidget()
        return rw
		
if __name__ == '__main__':
    myApp().run()		