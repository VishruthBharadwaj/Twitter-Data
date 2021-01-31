# Twitter Data Scraping using Twitter API


Have Sign-up to twitter accound applied for Twitter API in Developer portal and took credentials

Using Twitter API have fetched maximum data of tweets using documentation of twitter.


Before running the script please install tweepy,pandas

# Script Twitter.py
# It will fetch mentioned below data of user:
a)username

b)description

c)retweetcount

d)text

e)location

f)following

g)followers 

h)totaltweets

i)tweetscreatedat

j)profilebackgroundimage

k)profilebackgroundcolour

l)profilimageurl

m)numadic_url

n)display_text_range

o)truncatede

p)in_reply_to_status_id

q)in_reply_to_user_id

r)protected

s)geo_enabled

t)verified

u)contributors_enabled

v)is_translator

w)is_translation_enabled

x)profile_link_color

y)profile_sidebar_border_color

z)profile_sidebar_fill_color

aa)profile_text_color

ab)has_extended_profile

ac)default_profile

ad)follow_request_sent

ae)notifications

af)translator_type

ag)retweeted

ah)favorite_count

ai)favorited

aj)lang

ak)is_quote_status 

al)entities

am)url

an)metadata

ao)source

ap)user

aq)id

ar)full_text

as)hashtext

at)listed_count

au)source


# Once it fetch all the detail it will be stored in file named as scraped_tweets.csv

# All the data which are all fetched are recent last 1 minute data.


# When we run the script Twitter.py in cmdprmt

User will get the output as:
# Enter Twitter word to search for

Please enter example: #Covid19

# How many recent tweets need to be scraped?:

please enter as example : 30

Everything will be fetched as mentioned above and at last we will get as Scraping completed.

File will be stored as scraped_tweets.csv



# Script Twitter2.py


# It will fetch all the recent data of mentioned date.

Please mention Startdate and enddate in command prompt as mentioned in format of Output


When we run the Script Twitter2.py


We will get output as :

Enter Twitter word to search for

Example: Enter msd

Enter Date since The Tweets are required in yyyy-mm-dd

Example: 2021-01-29

Enter end since The Tweets are required in yyyy-mm-dd

Example: 2021-01-31

How many recent tweets need to be scraped?:

Example: 10


Everything will be fetched as mentioned above and at last we will get as Scraping completed.

File will be stored as Twitter2.csv

