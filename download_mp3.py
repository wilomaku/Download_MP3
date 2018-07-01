#! python2.7

import subprocess, sys, bs4, requests, re, pyperclip

savedir = '/home/wilomaku/Music/'

if len(sys.argv) > 1:
    # Get address from command line.
    url_youtube = ' '.join(sys.argv[1:])
    # TODO: Get address from clipboard.
else:
    # Get address from clipboard.
    #url_youtube = pyperclip.paste()
	url_youtube = raw_input('Paste video url:')

vid_youtube = requests.get(url_youtube)
vid_youtube.raise_for_status()
youtubeSoup = bs4.BeautifulSoup(vid_youtube.text, 'lxml')

regexp = re.compile(r'[^\n]')
title_song = youtubeSoup.select('h1')[1].getText()
title_song = ''.join(regexp.findall(title_song)).strip()

subprocess.call(['youtube-dl', '-x', '--audio-format', 'mp3', '-o', '{}{}.mp3'.format(savedir,title_song), '{}'.format(url_youtube)])
