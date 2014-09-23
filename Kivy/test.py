"""
Copyright (c) 2014 Dan Obermiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

You should have received a copy of the MIT License along with this program.
If not, see <http://opensource.org/licenses/MIT>
"""

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import StringProperty
from kivy.event import EventDispatcher

import sys

class outputLabel(EventDispatcher):
	text = StringProperty('')

	def __init__(self, **kwargs):
		super(outputLabel, self).__init__(**kwargs)
		self.text = StringProperty("Hi")

	def write(self, text):
		self.text = StringProperty(text)
		
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