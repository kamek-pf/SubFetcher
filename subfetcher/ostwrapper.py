import xmlrpc.client
import urllib.request
import gzip
import os
from subfetcher.localvideo import LocalVideo

# OpenSubtitles wrapper
class OpenSubtitleWrapper:

	def __init__(self):
		self.ost = xmlrpc.client.ServerProxy("http://api.opensubtitles.org/xml-rpc")
		self.url = 'No subtitles available'

	# Log into OpenSubtitles
	# Returns a login token needed by XMLRPC
	def login(self):
		login = self.ost.LogIn("", "", "en", "OSTestUserAgent")
		self.token = login['token']
		return login['status']

	# Logout when we're done
	def logout(self):
		logout = self.ost.LogOut(self.token)
		return logout['status']

	# Find subtitles matching the file name
	# Returns the appropriate download URL
	def findSubtitleFor(self, localVideo):
		searchParams = [{'tag': localVideo.name, 'sublanguageid': 'eng'}]
		subtitleQuery = self.ost.SearchSubtitles(self.token, searchParams) 

		if subtitleQuery['data']:
			self.url = subtitleQuery['data'][0]['SubDownloadLink'] 
			return self.url

	# Download the subtitles found by previous method
	# Subtitles are gziped, so gunzip them here
	# TODO : delete the archive afterwards
	def downloadSubtitle(self, localVideo):
		# Do nothing unless we have an URL
		if (self.url != 'No subtitles available'):
			# Set the subtitle destination and download it
			localSrt = localVideo.dirname + '/' + localVideo.noExtName + '.srt'
			localArchive = localSrt + '.gz'
			urllib.request.urlretrieve(self.url, localArchive)

			# Read the downloaded archive's content
			with gzip.open(localArchive, 'rb') as f:
				archiveContent = f.read()
			f.close()

			# Write the subtitle in the original video's directory
			with open(localSrt, 'w') as s:
				s.write(str(archiveContent, 'UTF-8'))
			s.close()

			# Delete the archive
			os.remove(localArchive)

			print('Subtitles :', os.path.basename(localSrt), 'downloaded successfuly.')
			return True
		else: 
			print('No subtitles were downloaded.')
			return False

	# Main method
	# Fetch subtitle from file name
	def fetchSubtitlesFor(self, localVideo):
		self.login()
		self.findSubtitleFor(localVideo)
		self.downloadSubtitle(localVideo)
		self.logout()