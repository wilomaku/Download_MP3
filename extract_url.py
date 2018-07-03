from __future__ import unicode_literals
import subprocess, sys, bs4, requests, re, eyed3, youtube_dl, csv, glob

if len(sys.argv) > 1:
    # Get address from command line.
    savedir = ' '.join(sys.argv[1:])
    # TODO: Get address from clipboard.
else:
    # Get address from clipboard.
    #url_youtube = pyperclip.paste()
	savedir = input('Paste save path, including final /: ')

#url_youtube = 'https://www.youtube.com/watch?v=WjCgYk_APVU'
url = r'/home/wilomaku/Downloads/test.html'
page = open(url)
youtubeSoup = bs4.BeautifulSoup(page.read(), 'lxml')

logfile_path = '{}url_list.txt'.format(savedir)
log = open(logfile_path, 'w')

title_song = youtubeSoup.select('#thumbnail')
for i in range(len(title_song)):
	try:
		log.write(title_song[i]['href'])
		log.write('\n')
	except:
		continue

log.close()
