# coding=utf8
import urllib2
from bs4 import BeautifulSoup
import re
max = 0

entos = []
ektos = []
assoi =[]
isopalies =[]
dipla =[]

url = urllib2.urlopen("http://www.oddscheck.net/?page=home&cmd=def")
content = url.read()
soup = BeautifulSoup(content)

for td in soup.findAll("td", { "class":"home greyb" }):
	entos.append(td.a.string)
	assoi += re.findall("\d+.\d+", str(td.a.string.encode('utf-8')))
	
for td in soup.findAll("td", { "class":"draw lightgreyb" }):
	#print str(td.a.string.encode('utf-8'))
	isopalies += re.findall("\d+.\d+", str(td.a.string.encode('utf-8')))
	
for td in soup.findAll("td", { "class":"away greyb" }):
	ektos.append(td.a.string)
	dipla += re.findall("\d+.\d+", str(td.a.string.encode('utf-8')))
	

for x,y,z,en,ek in zip(assoi,isopalies,dipla,entos,ektos):
	ganiota = 1 - ( 1 / ( (1/float(x)) + (1/float(y)) + (1/float(z)) ) )
	
	if ( ganiota < 0 ):
		kerdos = 100 - (100/float(x) + 100/float(y) + 100/float(z))
		if kerdos > 10:
			print en.encode('utf-8')+"\t"+ek.encode('utf-8')
			print str(ganiota) + " \t" +x+" \t" +y+" \t" +z 
			print str(100/float(x))+" \t" +str(100/float(y))+" \t" +str(100/float(z))
			print "KERDOS -> " + str( kerdos)+"\n\n"

		if ganiota < max:
			max = ganiota

print max
