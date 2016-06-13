
import urllib2
import requests
from bs4 import BeautifulSoup
import pandas as pd

print "Twitter username:"
user = raw_input()
url = "https://twitter.com/%s"
res = urllib2.urlopen(url % user)
html = res.read()
soup = BeautifulSoup(html, 'lxml')
tweets = soup.find_all('li', 'js-stream-item')
tweet_text = soup.find_all('p', 'js-tweet-text')
tweet_timestamps = soup.find_all('a', 'tweet-timestamp')
tweet_links = soup.find_all('a', 'js-details')
t= []
rng = len(tweet_text)
for i in range(0, rng):
    txt = tweet_text[i].get_text().encode('ascii', 'ignore')
    tmp = tweet_timestamps[i].get_text().encode('ascii', 'ignore')
    t.append({'text':txt,'time': tmp})
op = pd.DataFrame(t)
op.columns = ['text','time']
print('')
print('')
print('')
print('')
print('')
print('================//====================')
print('User name: ') 
print(user)
print('================//====================')
print('Recent tweets: ') 
print(op.tail)
print('================//====================')
print('Do you want to save as csv? [y/n]:')
dld = raw_input()
if dld == 'y':
	fn = str('twitter_user_' + user + '.csv')
	op.to_csv(fn)
	print('Saved csv!') 
else:
	print('csv file not saved this time...') 


