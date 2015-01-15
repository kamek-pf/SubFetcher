import subfetcher 
import sys

def cli():
	if len(sys.argv) == 2:
		subfetcher.main(sys.argv[1])
	else:
		print("Pass the path to your video as first argument")
