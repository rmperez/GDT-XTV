#this will only work the dblp format

import xml.etree.ElementTree as ET
tree = ET.parse('dblpmini.xml')
dblp = tree.getroot()

#need somewhat *random* numbers so each node will have a distinct name
x=0
y=0

parent = "dblp0"

print "digraph {"
print "rankdir=LR"
print "node [shape=\"box\"]\n"

print dblp.tag+str(x)+" [label=\""+(dblp.tag).upper()+"\"]"
x=x+1

for item in dblp:
    #print item.tag, item.attrib, item.text
    
    #elementx [label="ELEMENT \n attributes"]
    #print item.tag+str(x)+" [label=\""+(item.tag).upper()+"\\n"+str(item.attrib)+"\"]"
    labelOut = " [label=\""+(item.tag).upper()+"\\n"
    for key in item.attrib:
    	labelOut += key + ": " + item.attrib[key] + "\n"
    print item.tag+str(x) + labelOut + "\"]"
    	
    #dblp0 -> {elementx}
    print parent+" -> {"+item.tag+str(x)+"}\n"
    for item2 in item:
        #parent is item

        #create new node for element
        #elementy [label="ELEMENT"]
        print item2.tag+str(y)+" [label=\""+(item2.tag).upper()+"\"]"

        #oval shape for element's contents
        print "node [shape=\"oval\"]"

        #create new node for element's contents
        #elementyx [label="contents"]
        print item2.tag+str(y)+"x [label=\""+item2.text+"\"]"

        #connect element node with element's contents node
        #elementy -> elementyx
        print item2.tag+str(y)+" -> "+item2.tag+str(y)+"x"
        
        #connect the parent item with the element node
        #elementx -> {elementy}
        print item.tag+str(x)+" -> {"+item2.tag+str(y)+"}\n"
        
        print "node [shape=\"box\"]"
        
        #print item2.tag+str(y)+" -> \""+item2.text+"\""
        #print item2.tag, item2.text
        
        y=y+1
    x=x+1

print "}"
