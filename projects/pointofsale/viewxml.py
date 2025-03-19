#!python3

import xml.etree.ElementTree as ET


root = ET.Element('product')
product = ET.ElementTree( root )



print(ET.tostring(product.getroot(),xml_declaration=True,encoding='UTF-8'))






#productxml = ET.parse('../samplexml/Product.xml')
#productroot = productxml.getroot()

#print(productxml)


#print(productroot.find('.'))




#print(productroot)


