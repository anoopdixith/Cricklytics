from bs4 import BeautifulSoup
import urllib2

def main():
	with open("all_international_players_link.txt") as f:
    		content = f.readlines()
	for each in content:
		url_string = "http://www.cricinfo.com" + each
		response = urllib2.urlopen(url_string)
                page_source = response.read()
                soup = BeautifulSoup(page_source)
		basic = soup.findAll("div", { "class" : "ciPlayernametxt" })
		soup1 = BeautifulSoup(str(basic))

		name = soup1.h1.get_text()
		name = name.encode('ascii', 'ignore').replace(","," ").rstrip().lower()
		
		country = soup1.h3.get_text()
		check_repeated(name,2,country)
                check_repeated(name,3,country)
		continue

		full_details = soup.findAll("p", { "class" : "ciPlayerinformationtxt" })
		full_name = BeautifulSoup(str(full_details[0])).span.get_text()

		born = BeautifulSoup(str(full_details[1])).span.get_text()

		born = born.encode('ascii', 'ignore').replace(","," ").rstrip()
		full_name = full_name.encode('ascii', 'ignore').replace(","," ").rstrip()
		country = country.encode('ascii', 'ignore').replace(","," ").rstrip()

		#print name+born+country+full_name

		with open("player_details.txt", "a") as text_file:
                	text_file.write("\n"+name+","+country+","+full_name+",")

def check_repeated(input, limit, country):
	compact = input.replace(" ","")
	for i in range(0,len(compact) - limit+1):
		same = 1
		for j in range(i, i+limit):
			if(compact[j] != compact[i]):
				same = 0
				break
		if same:
			with open("player_repetitions.txt", "a") as text_file1:
                        	text_file1.write("\n"+input+ " (" + str(limit) + ")"+ " ("+country+")" + " ("+compact[i]+")"+" ("+str(len(compact))+")")
	
		


if __name__ == "__main__":
	main()
