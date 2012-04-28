#!/usr/bin/python
from pygithub3 import Github
import urllib2
import json

response = urllib2.urlopen('https://api.github.com/repos/bitboxer/hcking/collaborators')
allgitusers = json.loads(response.read())

unique_avatars = {}

for user in allgitusers:
  unique_avatars[user['avatar_url']] = True

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

