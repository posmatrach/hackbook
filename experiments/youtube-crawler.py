#!/usr/bin/python

# Author: Abhinay Omkar
# Title: One-liner to download youtube video in Python
from urllib import urlopen, unquote; 
from urlparse import parse_qs, urlparse; youtube_watchurl="http://www.youtube.com/watch?feature=player_embedded&v=oEAmQZDTB1g";

video_id = parse_qs(urlparse(youtube_watchurl).query)['v'][0]; open(video_id+'.mp4', 'wb').write(urlopen("http://www.youtube.com/get_video?video_id=%s&t=%s&fmt=18"%(video_id, parse_qs(unquote(urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read().decode('utf-8')))['token'][0])).read())
print video_id
