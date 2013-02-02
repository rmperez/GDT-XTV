Group members
Mark Waylonis
Robert Perez
Jason Wong

Contributions
Robert Perez:  Parser, stylesheet, 
Jason Wong: Parser
Mark Waylonis:  User interface, XPath 

Requirements: Python 2.7.3
Directions: 
1. Edit the stylesheet (stylesheet.txt) to your liking without changing the the structure. Only change lines that do not begin with a # and only use valid dot words. Do not include quotation marks.
2. Run xmlparser.py and it will create a file called graph.dot
3. You will be presented with a menu that will let you choose to visual the structure of the entire file, or just parts of the file that match the criteria you give it. 
3a. When entering in options for choices 2 through 4, the string must match exactly and quotes must not be included.
3b. Allow cross references will show connections where different elements have the same author, year, journal, etc. The default setting visualizes the entire file in a flat structure with no cross references marked. Once cross references are allowed, each unique author, year, etc will only appear once and the all relevent arrows will point to it.
4. The graph.dot can now be opened with Graphviz to visualize the result.
5. Graphviz will update the visualization as you choose different menu options

We implemented GDT-XTV, the XML Tree Viewer.  We used a small sample of the dblp.xml file to test our parser and visualization methods. We used python 2.7.2, so as long as the proper version of python is used, no build is required.  We used github for sharing code.  

The given dblp.xml file is too large to run on any tool we tried. In addition, it contains special characters represented in the xml as &uuml; or similar which causes problems for our parsing tool. We have provided a few files labled dblpminix.xml that contain subsets of the dblp.xml with the the special characters removed (by find and replace).

The xml files included are subsets of the DBLP file. dblpmini.xml is the first 100 lines and dblpmini2.xml is the first 1000 lines. The included .dot file was created with dblpmini.xml with option 1, with the visualize entire data function selected.