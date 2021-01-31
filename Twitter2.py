


# import modules 
import pandas as pd 
import tweepy 
import csv

import datetime
import time
# function to display data of each tweet 
def printtweetdata(n, ith_tweet): 
	print() 
	print(f"Tweet {n}:") 
	print(f"Username:{ith_tweet[0]}") 
	print(f"Description:{ith_tweet[1]}") 
	print(f"Retweet Count:{ith_tweet[2]}") 
	print(f"Tweet Text:{ith_tweet[3]}") 
	print(f"Location:{ith_tweet[4]}") 
	print(f"Following Count:{ith_tweet[5]}")
	print(f"Follower Count:{ith_tweet[6]}") 
	print(f"Total Tweets:{ith_tweet[7]}") 
	print(f"Tweets created at :{ith_tweet[8]}")
	print(f"Tweet profilebackgroundimage:{ith_tweet[9]}")
	print(f"Tweet profileimageurl:{ith_tweet[10]}")
	print(f"Tweet profilebannerurl:{ith_tweet[11]}")
	print(f"Tweet display_text_range :{ith_tweet[12]}")
	print(f"Tweet truncated :{ith_tweet[13]}")
	print(f"Tweet source :{ith_tweet[14]}")
	print(f"Tweet in_reply_to_status_id :{ith_tweet[15]}")
	print(f"Tweet in_reply_to_status_id :{ith_tweet[16]}")
	print(f"Tweet protected :{ith_tweet[17]}")
	print(f"Tweet listed_count :{ith_tweet[18]}")
	print(f"Tweet geo_enabled :{ith_tweet[19]}")
	print(f"Tweet verified :{ith_tweet[20]}")	
	print(f"Tweet contributors_enabled :{ith_tweet[21]}")
	print(f"Tweet is_translator :{ith_tweet[22]}")
	print(f"Tweet is_translation_enabled :{ith_tweet[23]}")
	print(f"Tweet profile_link_color :{ith_tweet[24]}")
	print(f"Tweet profile_sidebar_border_color :{ith_tweet[25]}")
	print(f"Tweet profile_sidebar_fill_color :{ith_tweet[26]}")
	print(f"Tweet profile_text_color :{ith_tweet[27]}")
	print(f"Tweet has_extended_profile :{ith_tweet[28]}")
	print(f"Tweet default_profile :{ith_tweet[29]}")
	print(f"Tweet follow_request_sent :{ith_tweet[30]}")
	print(f"Tweet notifications :{ith_tweet[31]}")
	print(f"Tweet translator_type :{ith_tweet[32]}")
	print(f"Tweet retweeted :{ith_tweet[33]}")
	print(f"Tweet favorite_count :{ith_tweet[34]}")
	print(f"Tweet favorited :{ith_tweet[35]}")
	print(f"Tweet lang :{ith_tweet[36]}")
	print(f"Tweet is_quote_status :{ith_tweet[37]}")
	print(f"Tweet entities :{ith_tweet[38]}")
	print(f"Tweet url :{ith_tweet[39]}")
	print(f"Tweet metadata :{ith_tweet[40]}")
	print(f"Tweet source :{ith_tweet[41]}")
	print(f"Tweet user :{ith_tweet[42]}")
	print(f"Tweet id :{ith_tweet[43]}")
	print(f"Tweet full_text :{ith_tweet[44]}")
	print(f"Hashtags Used:{ith_tweet[45]}") 


# perform data extraction 
def scrape(words, date_since, numtweet): 
	
	# Creating DataFrame using pandas 
	db = pd.DataFrame(columns=['username', 'description', 'retweetcount', 'text', 'location', 'following', 'followers', 'totaltweets', 'tweetscreatedat', 'profilebackgroundimage',
	 							'profilebackgroundcolour', 'profileimageurl', 'numadic_url', 'display_text_range', 'truncated', 'source', 'in_reply_to_status_id', 'in_reply_to_user_id',
	 							 'protected', 'listed_count', 'geo_enabled', 'verified', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_link_color',
	 							  'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'has_extended_profile', 'default_profile', 
	 							  'follow_request_sent', 'notifications', 'translator_type', 'retweeted', 'favorite_count', 'favorited', 'lang', 'is_quote_status',
	 							   'entities', 'url', 'metadata', 'source', 'user', 'id', 'full_text', 'hashtags']) 
	
	# We are using .Cursor() to search through twitter for the required tweets. 
	 
	tweets = tweepy.Cursor(api.search, q=words, lang="en", 
						since=date_since, until=end_since, tweet_mode='extended').items(numtweet) 
	
	list_tweets = [tweet for tweet in tweets] 
	
	# Counter to maintain Tweet Count 
	i = 1
	
	# we will iterate over each tweet in the list for extracting information about each tweet 
	for tweet in list_tweets: 
		username = tweet.user.screen_name 
		description = tweet.user.description 
		totaltweets = tweet.user.statuses_count 
		retweetcount = tweet.retweet_count 
		location = tweet.user.location 
		following = tweet.user.friends_count
		followers = tweet.user.followers_count 
		totaltweets = tweet.user.statuses_count
		tweetscreatedat = tweet.created_at
		profilebackgroundimage = tweet.user.profile_background_image_url
		profilebackgroundcolour = tweet.user.profile_background_color
		profilimageurl = tweet.user.profile_image_url
		numadic_url = tweet.user.url
		display_text_range = tweet.display_text_range
		truncated = tweet.truncated
		source = tweet.source
		in_reply_to_status_id = tweet.in_reply_to_status_id
		in_reply_to_user_id = tweet.in_reply_to_user_id
		protected = tweet.user.protected
		listed_count = tweet.user.listed_count
		geo_enabled = tweet.user.geo_enabled
		verified = tweet.user.verified
		contributors_enabled = tweet.user.contributors_enabled
		is_translator = tweet.user.is_translator
		is_translation_enabled = tweet.user.is_translation_enabled
		profile_link_color = tweet.user.profile_link_color
		profile_sidebar_border_color = tweet.user.profile_sidebar_border_color
		profile_sidebar_fill_color = tweet.user.profile_sidebar_fill_color
		profile_text_color = tweet.user.profile_text_color
		has_extended_profile = tweet.user.has_extended_profile
		default_profile = tweet.user.default_profile
		follow_request_sent = tweet.user.follow_request_sent
		notifications = tweet.user.notifications
		translator_type = tweet.user.translator_type
		retweeted = tweet.retweeted
		favorite_count = tweet.favorite_count
		favorited = tweet.favorited
		lang = tweet.lang
		is_quote_status = tweet.is_quote_status
		entities = tweet.entities
		url = tweet.user.url
		metadata = tweet.metadata
		source = tweet.source
		user = tweet.user
		id = tweet.id
		full_text = tweet.full_text
		hashtags = tweet.entities['hashtags'] 
		
		# Retweets can be distinguished by a retweeted_status attribute, 
		# in case it is an invalid reference, except block will be executed 
		try: 
			text = tweet.retweeted_status.full_text 
		except AttributeError: 
			text = tweet.full_text 
		hashtext = list() 
		for j in range(0, len(hashtags)): 
			hashtext.append(hashtags[j]['text']) 
		
		# all the extracted information in the DataFrame 
		ith_tweet = [username, description, retweetcount, text, location, following, followers, totaltweets, tweetscreatedat, profilebackgroundimage,
					profilebackgroundcolour, profilimageurl, numadic_url, display_text_range, truncated, source, in_reply_to_status_id, in_reply_to_user_id,
					 protected, listed_count, geo_enabled, verified, contributors_enabled, is_translator, is_translation_enabled, profile_link_color, profile_sidebar_border_color,
					  profile_sidebar_fill_color, profile_text_color, has_extended_profile, default_profile, follow_request_sent, notifications, translator_type,
					   retweeted, favorite_count, favorited, lang, is_quote_status, entities, url, metadata, source, user, id, full_text, hashtext] 
		db.loc[len(db)] = ith_tweet 
		
		# Function call to print tweet data on screen 
		print(i, ith_tweet) 
		i = i+1
	filename = 'Twitter2.csv'
	
	# we will save our database as a CSV file. 
	db.to_csv(filename) 
	
if __name__ == '__main__': 
	
	
	consumer_key="GukVEQqENGxOzKItNQH8WzLnV"
	consumer_secret="y8fnCnbAvVpenm6tG7vDc6EFYnuE6fI6gS2ag0qhAWvqhLMyGj"
	access_token="76901740-uobZSTxtFQd8mVtNgwWcLHw4IrW8UoEI9xInsKfoQ"
	access_token_secret="jYC0L0fZVU4lHhc2TOWt35dFHyRy83bbPDAm8hZVi9Tw5"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
	auth.set_access_token(access_token, access_token_secret) 
	api = tweepy.API(auth) 
	
	
	print("Enter Twitter word to search for") 
	words = input()
	
	print("Enter Date since The Tweets are required in yyyy-mm-dd") 
	date_since = input()

	print("Enter end since The Tweets are required in yyyy-mm-dd") 
	end_since = input() 
	numtweets = input('How many recent tweets need to be scraped?: ')
	numtweet = int(numtweets)
	scrape(words, date_since, numtweet)
	print('Scraping has completed!') 
