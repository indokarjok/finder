#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("find.txt","r");
	link = raw_input("TARGET :V \n (Contohnya : example.co.il or www.example.co.li :V ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "#################################"
        Space(9); print "##  *** Admin Panel Finder *** ##"
	Space(9); print "##    Recoded By IndoKarjok    ##"
	Space(9); print "##    (_)(_)==D     C'rooTzz   ##"
	Space(9); print "#################################"
Credit()
findAdmin()