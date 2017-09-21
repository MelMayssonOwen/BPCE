TWITTER = ./0_twitter_crawler.py
FACEBOOK = ./0_facebook_crawler_1.py
FACEBOOK2 = ./0_facebook_crawler_2.py
WEB = ./0_web_crawler.py
GOOGLE = ./

clear :
	clear
twitter :
	python $(TWITTER)
web :
	python $(WEB)
##facebook :
##	python $(FACEBOOK)
##	python $(FACEBOOK2)

ultimate :
	python 1_ultimate_parser.py

wordcloud :
	python 2_wordcloud.py

categorizer :
	python 2_categorizer.py

display :
	python 3_display.py

all : clear twitter web ultimate wordcloud categorizer display

diapo : clear ultimate wordcloud categorizer display
