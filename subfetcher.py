#!/usr/bin/python

import sys, os.path
from localvideo import LocalVideo
from ostwrapper import OpenSubtitleWrapper

# Main method
def main(argv):
	# Download subtitles if we have a valid path
	if os.path.exists(argv):
		localVideo = LocalVideo(argv)
		ost = OpenSubtitleWrapper()
		ost.fetchSubtitlesFor(localVideo)
		
# Call main when this file is executed
if __name__ == '__main__':
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print("Pass the path to your video as first argument")