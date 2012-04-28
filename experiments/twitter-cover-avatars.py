#!/usr/bin/python
import twitter

api = twitter.Api(consumer_key='7hygGjKMjkZ4ZskqG2eraw',
consumer_secret='j7Zhu9CLynAF0G1LEiCSuQzBglqAzG5myLjaCfgxQ8', access_token_key='7225222-5Ypyum6Zl2zjOci1A9aa3umGhIdHjZgMqB77tluY', access_token_secret='2h6kakrFFgkVPHEw85Uk17os5ThjFajz1MJmI9SPOII')

alltweets = []

for tweet in api.GetSearch("#ah12", per_page=1000):
	alltweets.append(tweet)
	
for tweet in api.GetSearch("#ADVANCEhack", per_page=1000):
	alltweets.append(tweet)

unique_avatars = {}

for tweet in alltweets:
  unique_avatars[tweet.user.profile_image_url] = True

prefix = "<html><body style='font-face: Palatino'><table><tr><td colspan='10'><center><h1>Advance Hackathing Tweeps</h1></center></td></tr>"
grid = ""
rowcount = 0
for avatar in unique_avatars:
  if rowcount % 10:
    grid = grid + "<td><img src='" + avatar +"' style='margin:1em'></td>"
  else:
    grid = grid + "</tr><tr><td style='margin: 1em'><img src='" + avatar +"' style='margin:1em'></td>"
  rowcount += 1
postfix = "</tr></table></body></html>"
output = prefix + grid + postfix

print output

