import urllib2
import re

urlfile = urllib2.urlopen("http://twitaholic.com")
string = urlfile.read()

username_list = list()

char_index = 0

at_list = list()
end_list = list()

sawat = false 

for char in string:
	if char == "@"
	
	at_list.append(char_index)
	char_index ++





