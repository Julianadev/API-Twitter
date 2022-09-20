from twitter import *

#acesse seu token da api em https://developer.twitter.com
tweet = Twitter(auth=OAuth("TOKEN", "TOKEN_SECRET", "KEY", "SECRET"))
timeline = tweet.statuses.home_timeline()
friend_timeline = tweet.statuses.friends_timeline()

tweet.statuses.update(status = "Python API'S ARTICLE")
search = tweet.search.tweets(q= "Python")
hashtag = tweet.search.tweets(q="Python")
time = tweet.search.tweets(q="Python API", since ="2022-09-20")

