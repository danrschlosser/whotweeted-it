# -*- coding: utf-8 -*-
import re

#Hard Filters: too short,   
#Modifiers : url (turl), contains their twitter handle or name (replace with ___)
#potential modifiers: multiple hashtags



def filter(tweet):
	editedTweet = turlFilter(tweet)

	return editedTweet 









def turlFilter(string):
	text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', string)
	return text


# def hasTheirName(displayName, string):

# 	if displayName.find(' '):

# 	if string.find('display')



#print filter("My favorite song when I'm thinking about my journey from the projects to success... http://t.co/evqo8Si13B'")


