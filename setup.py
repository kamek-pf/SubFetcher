#!/usr/bin/python

from setuptools import setup, find_packages

setup(
	name = "SubFetcher",
	version = "0.1",
	packages = ['subfetcher'],
	author = "kamek",
	author_email = "b.kamek@gmail.com",
	description = "Subtitles dowmloader for the CLI",
	entry_points = {
        	'console_scripts': ['subfetcher = subfetcher.cli:cli']
        },
	license = "GPL2",
	keywords = "subtitle subtitles tv show episode video",
	url = "http://github.com/kamek-pf/SubFetcher"
)