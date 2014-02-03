#How to use this folder
---
Updated 2/2/2014 10:00:54 PM 

##For adding data to the element objects
1. Open `elements.xlsx`
2. Add new data into this file, on the 2nd group (to the right)
	* Make sure that the left group is updated, I like the cleaner look to it
3. Copy paste this into a brand new temporary text file 
	* it can be named anything, I like `a.txt` 
	* yay, it is (sort of) ordered!
4. Either write a new python script or add onto `formatText.py` to combine your new Data with `ab.txt`
5. Run `formatText.py` and make sure `ab.txt` has been properly updated with the new data, and is properly formatted
6. Open `formatEPY.py` and add the relevant code
	* Getters/Setters in `class Element` as needed
	* `self.XXX` declarations in the unique classes
7. Run `formatEPY.py` and make sure `elements.py` is properly formatted
8. Copy/paste `elements.py` to your working directory (once you have code that supports it)

##Other
- `CHANGELOG.md` lists the changes that have been made to the program/repositry
- `TODO.md` lists the things I still need to do, but is not often updated