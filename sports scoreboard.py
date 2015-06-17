import xml.etree.ElementTree as ET
import urllib2
import datetime
import sys
from bs4 import BeautifulSoup

#for arg in sys.argv:
#	print arg

teamid = str(sys.argv[1])
print teamid

print "It's a great day for baseball"
print datetime.date.today()
year = str(datetime.date.today().year).zfill(2) 
month = str(datetime.date.today().month).zfill(2) 
day = str(datetime.date.today().day).zfill(2) 




#url = 'http://gd2.mlb.com/components/game/mlb/year_'+year+'/month_'+month+'/day_'+day+'/gid_'+year
dayurl= 'http://gd2.mlb.com/components/game/mlb/year_'+year+'/month_'+month+'/day_'+day+'/'
print dayurl



#getting html
html_page =urllib2.urlopen(dayurl)
soup= BeautifulSoup(html_page)

for link in soup.findAll('a'):
	current= str(link.get('href'))
	if teamid in current:
		break
		
print current

url =dayurl+current+'miniscoreboard.xml'
print url

#getting the xml
request = urllib2.Request(url, headers={"Accept" : "application/xml"})
u = urllib2.urlopen(request)
tree = ET.parse(u)
rootElem = tree.getroot()

hometeam=rootElem.attrib['home_name_abbrev']
print 'Home:' +hometeam

awayteam=rootElem.attrib['away_name_abbrev']
print 'Away:' +awayteam

status=rootElem.find('./game_status').attrib['status']
print 'Game Status:'+status

balls=rootElem.find('./game_status').attrib['b']
print 'Balls:'+balls

strikes=rootElem.find('./game_status').attrib['s']
print 'Strikes:'+strikes

outs=rootElem.find('./game_status').attrib['o']
print 'Outs:'+outs

inning=rootElem.find('./game_status').attrib['inning']
print 'Inning:'+inning

homescore=rootElem.find('./linescore/r').attrib['home']
print hometeam+':'+homescore

awayscore=rootElem.find('./linescore/r').attrib['away']
print awayteam+':'+awayscore


#print rootElem.fin

#print rootElem
