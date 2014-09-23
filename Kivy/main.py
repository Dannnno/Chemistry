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

from __future__ import division

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from random import randint
import time

tdict = {0:"None", 1:"Element", 2:"Bond", 3:"Charge", 4:"Radical", 5:"Lone Pair"}
objtype = tdict[0]
mdict = {0:"None", 1:"Add", 2:"Remove", 3:"Change"}
mode = mdict[0]
edict = {0:"None", 1:'H', 2:'He', 3:"Li", 4:"B", 5:"Uuo"}
current_element = edict[1]
allElements = []

class ptPopup(Popup):

    def __init__(self, **kwargs):
        super(ptPopup, self).__init__(**kwargs)
        self.title = 'Periodic Table'
        self.content = Label(text='This will be the PTotE')

class tElement(BoxLayout):
    text = 'C'
    
    def __init__(self, apos, **kwargs):
        super(tElement,self).__init__(**kwargs) 
        self.pos = apos
        global allElements
        allElements.append(self)
        
class tCharge(BoxLayout):
    text = '+'
    
    def __init__(self, apos, **kwargs):
        super(tCharge, self).__init__(**kwargs)
        self.pos = apos
        
class tRad(BoxLayout):
    text = '*'
    
    def __init__(self, apos, **kwargs):
        super(tRad, self).__init__(**kwargs)
        self.pos = apos

class tLPE(BoxLayout):
    text = ':'
    
    def __init__(self, apos, **kwargs):
        super(tLPE, self).__init__(**kwargs)
        self.pos = apos                
        
class tBond(BoxLayout):
    
    def __init__(self, start, end, **kwargs):
        super(tBond, self).__init__(**kwargs)
        self.slope = (end[1]-start[1])/(end[0]-start[0])
        self.intercept = start[1] - self.slope * start[0]
        self.somePoints = []
        x = start[0]
        y = start[1]
        while (x, y) < end and (x, y) > start: pass

class Workbench(FloatLayout):

    def __init__(self, **kwargs):
        super(Workbench,self).__init__(**kwargs)
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            global objtype, mode, current_element, allElements
            current_element = edict[randint(1,5)]
            trueTouch = (touch.pos[0]-15, touch.pos[1]-15)
            print objtype, mode, touch.pos
            
            if mode == 'Add':
                if objtype == 'Element':
                
                    """abool = True
                    for element in allElements:
                        if element.collide_point(*trueTouch):
                            abool = False
                            break
                    if abool:
                        tElement.text = current_element
                        self.add_widget(tElement(trueTouch))"""
                        
                    tElement.text = current_element
                    self.add_widget(tElement(trueTouch))
                    
                elif objtype == 'Charge':
                    someCharge = ['+','-']
                    tCharge.text = someCharge[randint(0,1)]
                    self.add_widget(tCharge(touch.pos)) 
                                       
                elif objtype == 'Radical':
                    self.add_widget(tRad(touch.pos))
                
                elif objtype == 'Lone Pair':
                    self.add_widget(tLPE(touch.pos))
                
                else:pass
                
            if mode == 'Remove':pass
            
            if mode == 'Change':
                if objtype == 'Element':pass
                
                elif objtype == 'Bond':pass
                
                elif objtype == 'Charge':pass
                
                elif objtype == 'Radical':pass
                
                elif objtype == 'Lone Pair':pass
                
                else:pass
                
            return True
            
        def on_touch_move(self, touch):
            global objtype, mode
            if mode == 'Add' and objtype == 'Bond':pass

class Output(FloatLayout): 

    def __init__(self, **kwargs):
        super(Output,self).__init__(**kwargs)

class RootWidget(Widget):

    def setMode(self, n):
        global mode
        mode = mdict[n]
        print mode
        
    def setType(self, n):
        global objtype
        objtype = tdict[n]
        print objtype
    
    def publish(self):
        print "NYI"
        
    def clear(self):
        print "NYI"
        
    def openPTOTE(self):
        self.setMode(1)
        self.setType(1)
        global periodicTable
        periodicTable = ptPopup()
        periodicTable.open()
        time.sleep(10)
        periodicTable.dismiss()
        
    
class ChemGuiApp(App):
    
    def build(self):
        global rw
        rw = RootWidget()
        return rw
        
if __name__ == '__main__':
    ChemGuiApp().run()
