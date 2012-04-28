#!/usr/bin/python
import twitter

api = twitter.Api(consumer_key='7hygGjKMjkZ4ZskqG2eraw',
consumer_secret='j7Zhu9CLynAF0G1LEiCSuQzBglqAzG5myLjaCfgxQ8', access_token_key='7225222-5Ypyum6Zl2zjOci1A9aa3umGhIdHjZgMqB77tluY', access_token_secret='2h6kakrFFgkVPHEw85Uk17os5ThjFajz1MJmI9SPOII')


for tweet in api.GetSearch("#ah12", per_page=50):
	print tweet.text
	
for tweet in api.GetSearch("#ADVANCEhack", per_page=50):
	print tweet.text

