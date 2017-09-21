import tweepy
from datetime import date
from datetime import timedelta
from tweepy import OAuthHandler
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import pandas as pd
import numpy as np

from credentials import *

def twitter_setup():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	return api

def evaluate_sent(text):
    blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return blob.sentiment[0]

api = twitter_setup()
today = date.today()

for i in range(0,7):
    last_week = today - timedelta(days=i)

querys = "BPCE", "Banque Populaire", "Caisse Epargne", "Natixis", "Credit Foncier", "Credit Cooperatif", "BRED", "Casden"
since_date=last_week
query = "BPCE"

max_tweets = 10


f = open("./outputs/twitter_output.csv", "w")
for x in querys:
	query = x
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=x, tweet_mode="extended", lang="fr").items(max_tweets)]
	for t in searched_tweets:
		s = str("Twitter")
		f.write(s)
		f.write(",")
		s = str(query)
		f.write(s)
		f.write(",")
		s = str(t.created_at)
		s = s[:-9]
		s = s.replace(",", "")
		s = s.replace("\n", "")
		f.write(s)
		f.write(",")
		s = str(t.full_text)
		s = s.replace(",", "")
		s = s.replace("\n", "")
		f.write(s)
		f.write(",")
		s = evaluate_sent(t.full_text)
		if s > 0:
			s = str("good")
		elif s == 0:
			s = str("average")
		elif s < 0:
			s = str("bad")
		f.write((str(s)))
		f.write(",")
		s = str(int(t.retweet_count) + int(t.favorite_count))
		f.write(s)
		f.write(",\n")
