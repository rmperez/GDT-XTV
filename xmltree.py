#written for Python 2.7.3
#this will only work with the dblp format
#reads in dblpmini.xml and outputs graph.dot
import os
import xml.etree.ElementTree as ET
file = "dblpmini.xml"
stylesheet = "stylesheet.txt"
tree = ET.parse(file)
dblp = tree.getroot()

#styelsheet variables
elementShape = "box"
leafShape = "oval"


menu = "0"
print("\nWelcome to XML Tree Visualization")
while menu != "5":  
	print("Here are the options for vizualization of dblp")
	print("1. Vizualize entire file")
	print("2. Select an author")
	print("3. Select a journal")
	print("4. Select a year")
	print("5. Exit")
	menu  = raw_input("please enter choice: ")
	if menu == "1":
		choice = "entire file"
	elif menu == "2":
		choice = "author"
	elif menu == "3":
		choice = "journal"
	elif menu == "4":
		choice = "year"
	elif menu == "5":
		print("Goodbye!")
		exit()
	else:
		print("Invalid menu choice, try again!")
		continue   
	if menu != "1":
		#get user input for specific author, journal, or year
		find = raw_input("please enter desired " + choice + ": ")
		#form query for XPath
		query = "./*[" + choice + "='" + find + "']"
	else:
		find = ""
		#if we want to vizualize the entire file, the query will return all elements of dblp
		query = "./*"
	print("Finding entries for " + choice + " " + find + "..." )

	#open file where we will write out vizualization instructions for graphviz 
	f = open('graph.dot','w')  


#findall performs an XPath query on dblp
	results = dblp.findall(query)
	nresults = len(results)

	if nresults == 0:
		print("No results found.  Please try a new search.\n")
		continue
	elif nresults == 1:
		print("Only one item found matching your criteria.\n")
	else:
		print(str(nresults) + " items found matching your criteria.")
	print("Generating vizualization...\n")


	#need unique numbers so each node will have a distinct name
	x=0
	y=0

	parent = "dblp0"

	f.write("digraph {\n")

	#GRAPH DIRECTION
	f.write("rankdir=LR\n")


	#f.write("node [shape=\"box\"]\n\n")

	f.write(dblp.tag+str(x)+" [label=\""+(dblp.tag).upper()+"\"]\n")
	x=x+1

	for item in results:
		#print item.tag, item.attrib
		
		f.write("node [shape=\"box\"]\n\n")

		f.write(item.tag+str(x)+" [label=\""+(item.tag).upper()+"\\n"+str(item.attrib)+"\"]\n")
		f.write(parent+" -> {"+item.tag+str(x)+"}\n\n")
		for item2 in item:
			if item2.tag == choice:
				print(item2.text)
			#parent is item
			f.write("node [shape=\"box\"]\n\n")
		
			#create new node for element
			f.write(item2.tag+str(y)+" [label=\""+(item2.tag).upper()+"\"]\n")

			#oval shape for element's contents
			f.write("node [shape=\"oval\"]\n")

			#create new node for element's contents
			f.write(item2.tag+str(y)+"x [label=\""+item2.text+"\"]\n")

			#connect element node with element's contents node
			f.write(item2.tag+str(y)+" -> "+item2.tag+str(y)+"x\n")
		
			#connect the parent item with the element node
			f.write(item.tag+str(x)+" -> {"+item2.tag+str(y)+"}\n\n")
		
			#f.write("node [shape=\"box\"]\n")
		
			#print item2.tag+str(y)+" -> \""+item2.text+"\""
			#print item2.tag, item2.text
		
			y=y+1
		x=x+1

	f.write("}\n")
	f.close()