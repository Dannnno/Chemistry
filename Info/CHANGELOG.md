###Changelog - updated 1/30/2014 11:37:48 AM 
---
Current stage of development: Pre-Alpha  
Current program version: NA

**12/05/2013** 

- began production
- `molarmasscalc.py` created
          
**12/06/2013** 

- created element class and began adding methods
- began creating support for basic element data name, symbol, number, mass
- created periodic class and began adding methods
- began creating support to identify/locate elements on the periodic table based on an input
- `element.py` created
- `molarmasscalc.py` updated
          
**12/07/2013**

- expanded scope of project
- decided to attempt to build a program to take reactants and predict reaction, and be able to show the steps
- created initial instancing of updated element class
- began framework for a periodic table in a numpy array
- `element.py` updated
- `ptable.dat` created
- `elements.dat` updated

**12/08/2013**

- changed respository to Chemistry
- minor rework to the methods of class Element
- created the periodic table array, populated with Element objects via class periodic
- deleted class Periodic, replaced with `tablecreate()`
- recreated *.dat files as *.txt files
- created excel file for better *.txt management
           
**12/09/2013** 

- Minor reworks to `element.py`
-            began GUI work
-                 created initial windowing, button and class support
-            Moved Changelog from `README.txt` to `CHANGELOG.txt`
-            Rewrote `README.txt` in order to better explain and lay out the project
-            Created `TODO.txt` in order to keep myself on track

**12/10/2013**

- Continued adding functionality to GUI
- Learned how to use callback, kind of
- began creating classes (named gX to distinguish from the non graphical varient)
- Updated `TODO.txt`
- Clarified necessary functionality of GUI
- Initialized location dictionaries

**12/11/2013** 

- Continued adding functionality to GUI
	- Considering choosing a different language to work in
		- Java maybe?

**12/26/2013**

- Got back on the wagon, fixed element.py
- Moved periodic table creation back into a class, `class Mendeleev`
- Added basic functionality to class Mendeleev
- Element creation and periodic creation +/- complete, began considering compound creation and manipulation 
- postponed GUI implementation
- Added a Bond Class
- Added a Compound Class
	- Added functionality to these
- Created superclass Chemistry
	- made all other classes (Element, Mendeleev, Bond, Compound) subclasses of the Chemistry superclass
	- superclass currently has no functionality

**12/27/2013**

- Added more functionality to Compound class and compound creation
- slightly edited functionality of all other chemistry subclasses
           
**1/02/2014** 

- Added functionality to Compound Class
**
01/05/2014**   

- Began adding support for structural relationships in Compound Class

**1/06/2014** 

- Completed initial support for element placing in Compound Class
- Began creating support for bond creation/placing in Compound Class
- Enhanced bond creation functionality in Element Class
                
**1/12/2014** 

- After much ado found a working solution with pyparsing for complex/branched compounds
- Began rewriting functionality to support association with `self.structure`
- Early functionality with forked compounds need to work on sizing issues of self.structure
- Created superclass Reactions
	- Doesn't do anything, but made me feel good inside

**1/15/2014** 

- Finished updating functionality for branched compounds
	- Began adding functionality for very complex compounds 
		-  need to fix overlap issue, nested arrays?
		-  need to fix sizing of self.structure
		-  need to add functionality for re-sizing/shaping self.structure
	- Began adding functionality for rings (class Ring(Compound)) and bridged structures (class BridgedStructure(Ring))
	- Began adding functionality for double/triple bonds in a compound
- Transitioned all user-side text documents `README.txt`, `TODO.txt`, `CHANGELOG.txt` to **MarkDown** equivalents `README.md`, `TODO.md`, `CHANGELOG.md`
                  
**1/16/2014**

-  Began considering the `enable` and `enaml` modules for use in construction of a GUI
-  Continued adding support for nested/very complex compounds
	- Works fine as long as proper parentheses are present
	- work on a function that will take a normal string version of a formula and add parentheses
	- or don't ~ low priority  

**1/17/2014**

- Moved stuff from `testchem.py` to `chemistry.py` because it was working
- Started working on ring and double/triple bond support in `test.py`
	- Once initial support is ready it will be moved to `testchem.py` for more strenuous testing 
	- initial ring support completed.  support still needed for:
		- bonding to main structure
		- more complex substituents
		- actual element/bond support - currently only has temporary string support   
		- needs double/triple bond support for bonds within the ring or to the main structure 
	- initial double/triple bond support completed  
- Updated docstrings and commented code in `chemistry.py`.  Removed unnecessary whitespace and newlines where there was no significant impact on readability

**1/18/2014**

- Completed initial support for double and triple bonds in `branching()` within `testchem.py`
- Completed initial support for rings in `test.py`
	- began working on `class Compound()` and related functions to support the addition of rings in `testchem.py`

**1/19/2014**

- Completed support for rings in `testchem.py`
	- still needs support for double bonds to/within the ring 
- Need to adjust `class Mendeleev()` and `toElement()` so that they create a unique element each time
- Adjust methods of bond creation so they are less cumbersome - put it all in bothBonds?
- find a better way to put all the substituents on a ring

**1/21/2014**

- Finished updating `chemistry.py`
- Working on optimizing the creation of bonds by type, location, etc
- Working on creating unique element objects instead of copying them
	- Began working on improved `populate()` and `toElement()` functions in **`test1.py`**

**1/22/2014**

- finished work in `test1.py`, began work on improved bond creation regardless of source in `test2.py`

**1/23/2014**

- continued work in `test2.py` and `testchem2.py` to improve bonding

**1/24/2014**

- Began major rework of `Element` class.  `Element` now contains all methods and subclasses such as `Hydrogen(Element)` and `Carbon(Element)` are each unique and contain atom specific information within.  First goal is to have common OChem elements created - program could eventually have different 'packages' for OChem, Gen Chem, P Chem, etc (?)
	- Work currently being done in `newchem.py`
- Created file `errors.py` to create and handle all custom exceptions I may/may not need.

**1/26/2014**

- Using `newchem2.py` as the temporary directory for specific element objects - contains Hydrogen, Carbon, Oxygen, Nitrogen and common halogens
- Began rewriting program to make use of the new compounds
	- use a dictionary to match symbols and a `'Hydrogen()'` like statement
	- when converting the strings to elements it should take the symbol, match to the dictionary, then use `eval()` to create the object
- added `InvalidBondException` to `errors.py`
- moved extensive list of element objects to `elements.py`

**1/27/2014**

- Used `asd.py` to iterate through the element list and update `elements.py`
	- Completed rework (for now - still needs oxidation support) 
- Continued updating `newchem2.py` so that it functions equivalently to `chemistry.py`
	- goal is to create a more elegant approach to the program
- Deleted some of the extraneous test `*.py` and `*.txt` files  

**1/28/2014**

- Continued working on `newchem2.py`
	- completed support for Element creation, Bond creation, Mendeleev creation
		- `populate()` `toElement()` `bondIt()` `stringify()` finished
	- finished support for `Compound`
	- began support for ring creation and bridged structure creation
- began working with `enaml` to create a GUI - actual effectiveness tbd

**1/29/2014**

- continued playing with `enaml`

**1/30/2014**

- concluded that `enaml` is not going to work for my purposes. Investigating Java as an alternative   