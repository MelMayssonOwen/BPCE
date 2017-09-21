import urllib.request
import calendar
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://www.60millions-mag.com/forum/banque-epargne-credit-f76/") as fp:
	soup = BeautifulSoup(fp, 'lxml')
web_output = open('./outputs/web_output.csv', 'w')
dates = []
comments = []
for link in soup.find_all('a', {'class': 'topictitle'}):
	with urllib.request.urlopen(link.get('href')) as fp:
		link_soup = BeautifulSoup(fp, 'lxml')
	for content in link_soup.find_all('p', {'class': 'author'}):
		text = content.contents[3]
		date = []
		j = 0
		for i in range(0, len(text)):
			if text[i] == " ":
				date.append(text[j:i])
				j = i + 1

		dates.append(date[2:len(date) - 1])
	first = 1
	title = link_soup.title.string.replace('•', '')
	for content in link_soup.find_all('div' , {'class': 'content'}):
		comment = content.get_text().replace(',', ';')
		comment = comment.replace('\n', '')
		if first == 1:
			comments.append(title + " " + comment)
		else:
			comments.append(comment)
		first = 0

def format_date(date):
	year = date[2][0:4]
	month = date[1].lower()
	if month == 'janvier':
		month = '01'
	elif month == 'février':
		month = '02'
	elif month == 'mars':
		month = '03'
	elif month == 'avril':
		month = '04'
	elif month == 'mai':
		month = '05'
	elif month == 'juin':
		month = '06'
	elif month == 'juillet':
		month = '07'
	elif month == 'août':
		month = '08'
	elif month == 'septembre':
		month = '09'
	elif month == 'octobre':
		month = '10'
	elif month == 'novembre':
		month = '11'
	elif month == 'décembre':
		month = '12'
	day = date[0]
	return (year + "-" + month + "-" + day)

if len(dates) == len(comments):
	n = len(comments)
	for i in range(0, n):
		output = 'website,BPCE,' + format_date(dates[i]) + ',' + comments[i] + '\n'
		web_output.write(output)
