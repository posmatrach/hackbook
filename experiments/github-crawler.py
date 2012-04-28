#!/usr/bin/python
from pygithub3 import Github

gh = Github()
bitbox = gh.users.get('bitboxer')
print bitbox