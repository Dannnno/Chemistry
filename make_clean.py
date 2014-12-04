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

import os
from collections import deque

                  
def extract_files(start_dir=os.getcwd(), excludes=[]):
    to_crawl = deque([filename 
                      for filename in os.listdir(start_dir)
                      if not filename.startswith('.') and
                      not filename in excludes])
    extracted = set()
    
    while to_crawl:
        current = to_crawl.popleft()
        
        if current in extracted:
            continue
        
        if os.path.isdir(current):
            to_crawl.extendleft(
                map(lambda x: os.path.join('', current, x),
                    extract_files(os.path.join(start_dir, current))))
            continue
            
        extracted.add(current)
        
    return filter(lambda x: x.endswith('.pyc'), extracted)
    
    
def delete_files(files):
    map(os.remove, files)
    

def make_clean(*except_):
    delete_files(extract_files(excludes=except_))
    
    
if __name__ == '__main__':
    make_clean('docs')
    