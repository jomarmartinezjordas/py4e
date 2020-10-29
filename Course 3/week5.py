'''
Week 5 - Data on the Web

Sending data over the net
example:  Python Dictionary >>>Serialize>>> Wire protocol >>>De-serialize>>> Java HashMap

XML an JSON

XML
- eXtensible Markup Language
- primary purppose is to share Data
- started as a simplified subset of the Standard Generalized Markup Language (SGML)
- hast start tag, end tag, (tags indicate beginning and end of elements) text content, attribute (key word/value pairs on the opening tag of XML), self closing tag
- serialize / de-serialize >> convert data in one program into a common format that can be store and/or transmitted between systems in a programming language-indepenent manner

XML Schema
- description of the legal format of an XML document
- expressed in terms of constraints on the structure and content of documents
- specifies a contract between two systems
- 'validates' whether the XML piece meets the specification of the Schema

'''
## PARSING DATA FROM XML
#for simple tags
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data) # converts the string to a tree like structure
print('Name:', tree.find('name').text) # find in the 'tree' the tag <name>
print('Attr:', tree.find('email').get('hide')) # .get is to parse the attribute

# for multiple tags
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
