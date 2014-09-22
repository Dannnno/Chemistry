###TODO List - updated 9/1/2014 10:30:11 AM 
---
GitHub:

* Understand how GitHub works **in progress**
	* pushing **done**
	* commiting **done**
	* branches **no clue**
* Look into a private repository
	* cost?  

MarkDown: **Completed**

* Learn about markdown and convert README.txt to README.md
* Potentially convert other *.txt files to *.md files
    
GUI:  **on hold**

- Create Main Window
- Create Menu options (File, Edit, Options, Help, etc)   
	- Compound creation support
	- Bond type support
	- atom type rupport
	- radical support
	- lpe support 
	- Charge support
- should open with a single Carbon as the default compound
- create a function ```near(clickLoc)``` that finds the nearest existing object and returns it if the distance is within a certain pixel tolerance
- display currently selected button/function
- Connect the GUI with the underlying framework (pretty pictures -> actual compounds)
- **`TestMolecule()`** should have several characteristics
	- `snap()` fit things to nice lines, appropriate bond lengths, etc
	- `autofill()` fill octet
		- Carbons get C-H bonds
		- All others get lone pair electrons
	- `autocalc()` determine formal charge
	- `resonate()` find and display resonance
	- `progress()` show a progress bar
	- `finish()` 
		- display the finished molecule (if possible)
		- display errors in feedback if necessary
		- name according to IUPAC standards
- `PublishMolecule` should save the molecule's information somewhere
- Should be a way to save current work without publishing molecule
    
Long term: **Not started**

- Name project
- Create .exe
- Port to mobile devices
	- iOS
	- Android

Readability: **meh**

- Obfuscation: **not started**
	- How?
	- May need to use Java/C to do it
		- Cython?
- Commenting: **barely started**
	- In line/block comments
	- Docstrings
- **Pythonic ways of doing things**
	- Getters/Setters with `@property`  