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

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import \
    StringProperty, ObjectProperty, NumericProperty, ListProperty
from kivy.logger import Logger

from Chemistry.base import periodic_table as pt


mode = 'Element'
element = 'C'
order = 1


class Element(Widget):
    
    symbol = StringProperty('C')
    size = (10, 10)
    pos = ListProperty([0, 0])
    
    def __init__(self, value, pos):
        self.symbol = value
        self.pos = pos
    
    def update(self, value):
        self.symbol = value
        
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        elif mode == 'Element':
            self.symbol = element
        return True
    
    def on_symbol(self, instance, value):
        if not value in pt.periodic_table:
            raise ValueError(
                "Symbol {} is not in the periodic table".format(value))


class Bond(Widget):
    
    first = StringProperty()
    second = StringProperty()
    order = NumericProperty()
    chirality = ObjectProperty()
    pos = ListProperty([0, 0])
    
    def __init__(self, first, second, order, chirality, pos): 
        self.first = first
        self.second = second
        self.order = order
        self. pos = pos
        self.chirality = None


class LabTable(Widget):
    
    elements = ObjectProperty({})
    bonds = ObjectProperty({})
    acount = NumericProperty(1)
    bcount = NumericProperty(1)
    
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            return False
        elif mode == 'Element':
            key = 'a{}'.format(self.acount)
            self.elements[key] = element
            self.add_widget(Element(element, touch.pos))
            self.acount += 1
        elif mode == 'Bond':
            key = 'b{}'.format(self.bcount)
            self.bonds[key] = (1, 2, order)
            Bond(1, 2, order, touch.pos)
            self.bcount += 1
        return True
        
        
class TextWindow(Widget):
    
    pass
    

class ButtonBar(Widget):
    
    pass
    
    
class ElementMode(Button):
    
    def callback(self):
        global mode
        mode = 'Element'
    
    
class BondMode(Widget):
    
    def callback(self):
        global mode
        mode = 'Bond'
    
    
class Order(Button):
    
    def callback(self): print 'Order'
        
        
class Chirality(Button):
    
    def callback(self): print 'Chirality'
    

class ChargeMode(Button):
    
    def callback(self):
        global mode
        mode = 'Charge'
    
    
class ElementSelector(Button):
    
    def callback(self):
        global mode
        mode = 'Selector'
        
        
class React(Button):
    
    def callback(self):
        print 'react'
    
    
class Workbench(Widget):
    
    pass    
    
    
class ChemApp(App):
    
    def build(self):
        app = Workbench()
        return app

        
if __name__ == '__main__':
    ChemApp().run()