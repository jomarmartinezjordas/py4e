'''
Week 4

Unicode Characters and Strings

ASCI - American Standard Code Interchange

each character is represented by a number between 0 and 256 store in 8 bits of memory
ord() function tells us the numeric value of a simple ASCII Characters

Unicode - Universal Code

Multi-byte Characters
> UTF-16 (Two bytes)
> UTF-32 (Four bytes)
> UTF-8 (1-4 bytes)

Python Strings to bytes
> when sending bytes, we need to encode Python3 strings to a given character encoding
> when reading data from external resource, we must decode based on the character set so it will be representd in python3 as a string

urllib - library that does all the socket work for use and makes web pages look like a file

Web Scraping
- when a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information and then looks at more web pages
- also called as 'spidering the web' or 'web crawling'


'''

# Representing Simple Strings
print(ord('H')) # this prints '72'
print(ord('e')) # this prints '101'

# Python Strings to bytes
while True :
    data = mysock.recv(512)
    if (len(data) < 1 ) :
        break
    mystring = data.decode()
    print(mystring)

# HTTP request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True :
    data = mysock.recv(512)
    if (len(data) < 1 ) :
        break
    mystring = data.decode()
    print(mystring)

# urllib

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand :
    print(line.decode().strip())

# mini web browser
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

# Pasring a website
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
