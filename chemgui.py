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
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, NumericProperty,\
                               ListProperty

from Chemistry.base.periodic_table import periodic_table as pt


mode = 'Element'
element = 'C'
order = 1
chirality = None
app = None


class Element(Widget):
    
    label_ = ObjectProperty()
    color = '[color=3333ff]{}[/color]'
    _text = StringProperty(color.format('C'))
    key = StringProperty('a1')
    pos = ListProperty([0, 0])
    size_hint = ListProperty([None, None])
    
    def __init__(self, key, symb, pos, **kwargs):
        super(Element, self).__init__(**kwargs)
        self.key = key
        with self.canvas.before:
            self.pos = pos
            self.text = symb
            self.label_.text = self.text
        self.canvas.ask_update()
        print self.color
        
    @property
    def text(self):
        return self._text
        
    @text.setter
    def text(self, element):
        self._text = self.color.format(element)
    
    def update(self):
        if mode == 'Element':
            self._text = element
            self.label_.text = self._text
            self.canvas.ask_update()
            return True
        else:
            return False
        
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        elif mode == 'Element':
            self.update()
        return True


class Bond(Widget):
    
    first = StringProperty()
    second = StringProperty()
    _order = NumericProperty()
    _chirality = ObjectProperty()
    size_hint = ListProperty([None, None])
    
    def __init__(self, first, second, order, chirality=None, **kwargs): 
        super(Bond, self).__init__(**kwargs)
        x1, y1, x2, y2 = first.pos
        x2, y2 = second.pos
        x1, x2 = ((x1+12, x2-2) if x1<x2 else (x1-2, x2+12))
        y1, y2 = y1+5, y2+5
        self.first = first.key
        self.second = second.key
        self.order = order
        self.chirality = chirality
        with self.canvas:
            Color(0, 0, 0, 1)
            if order == 1:
                Line(points=[x1, y1, x2, y2], width=1)
            elif order == 2:
                Line(points=[x1, y1+2, x2, y2+2], width=1)
                Line(points=[x1, y1-2, x2, y2-2], width=1)
            elif order == 3:
                Line(points=[x1, y1+2, x2, y2+2], width=1)
                Line(points=[x1, y1, x2, y2], width=1)
                Line(points=[x1, y1-2, x2, y2-2], width=1)
            else:
                raise ValueError(
                        "order's state must be 1, 2, or 3 (not {})"
                            .format(order))

    @property
    def order(self):
        return self._order
        
    @order.setter
    def order(self, ord_):
        self._order = int(ord_)
        
    @property
    def chirality(self):
        return self._chirality
        
    @chirality.setter
    def chirality(self, chiral):
        self._chirality = chiral
        
    def update(self):
        if mode == 'Bond':
            if self.order == 3:
                self.order = 1
            else:
                self.order += 1
            self.chirality = chirality


class LabTable(FloatLayout):
    
    element_keys = ObjectProperty({})
    element_locs = ObjectProperty({})
    acount = NumericProperty(1)
    
    bond_keys = ObjectProperty({})
    bond_locs = ObjectProperty({})
    bcount = NumericProperty(1)
    
    margins = {'Element': 15, 'Bond':20}
    first, second = None, None
    
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        else:
            child = self.compare_touch(touch)
            if child.__class__.__name__ == mode:
                child.update()
                return True
            elif mode == 'Element':
                self.add_element(touch)
            elif mode == 'Bond':
                self.add_bond(touch)
            self.canvas.ask_update()
            return True
            
    def add_element(self, touch):
        global element
        key = 'a{}'.format(self.acount)
        with self.canvas:
            self.element_locs[key] = touch.pos
            e = Element(key, element, touch.pos)
            self.element_keys[key] = element, e
            self.add_widget(e)
        self.acount += 1
        
    def add_bond(self, touch):
        if self.first:
            self.second = self.compare_touch(touch)
            if isinstance(self.second, Element): 
                global order
                key = 'b{}'.format(self.bcount)
                with self.canvas:
                    self.bond_locs[key] = touch.pos
                    b = Bond(self.first, self.second, order)
                    self.bond_keys[key] = b
                    self.add_widget(b)
                self.bcount += 1
            self.first, self.second = None, None
        else:
            self.first = self.compare_touch(touch)
            if not isinstance(self.first, Element):
                self.first = None            
            
    def compare_touch(self, touch):
        try:
            margin = self.margins[mode]
        except KeyError:
            return False
        right, top = map(lambda x: x + margin, touch.pos)
        left, bottom = map(lambda x: x - margin, touch.pos)
        for key, (x, y) in self.element_locs.iteritems():
            if (left <= x and right >= x) and (top >= y and bottom <= y):
                return self.element_keys[key][-1]
            
        
class TextWindow(Widget):
    
    pass
    

class ButtonBar(Widget):
    
    pass
    

class PeriodicTable(BoxLayout): 
    
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            app._popup.dismiss()
            return True
        super(PeriodicTable, self).on_touch_down(touch)
    
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
    
    
class ElementSelector(Button): pass        
        
        
class React(Button):
    
    def callback(self):
        print 'react'
    
    
class Workbench(BoxLayout):
    
    pass
    
    
class ChemApp(App):
    
    def build(self):
        global app
        app = self
        widget = Workbench()
        return widget
        
    def popup(self):
        self._popup = Popup(title='Periodic Table', content=PeriodicTable(),
                      size_hint=(.8, .8))    
        self._popup.open()
        
    def element(self, symbol):
        global element
        element = symbol
        print element, symbol
        self._popup.dismiss()
                      
        
if __name__ == '__main__':
    ChemApp().run()
