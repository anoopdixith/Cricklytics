import urllib2
from bs4 import BeautifulSoup
import re

def main():
	p = re.compile('\/ci\/content\/player\/[0-9].')
	for class_num in range(1,4):
		for ctr in range(1,10):
			response = urllib2.urlopen("http://www.espncricinfo.com/ci/content/player/caps.html?country="+str(ctr)+";class="+str(class_num))
			page_source = response.read()
			#print page_source
 			soup = BeautifulSoup(page_source)
			for link in soup.find_all('a'):
    				url = link.get('href')
				match_obj = p.match(url)
				if match_obj:
					with open("all_international_players_link.txt", "a") as text_file:
    						text_file.write(url+"\n")

if __name__ == "__main__":
    main()


