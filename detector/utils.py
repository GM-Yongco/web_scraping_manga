# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: utils for general web scraping
# ========================================================================
# HEADERS
# ========================================================================

import os
from io import TextIOWrapper

import requests as req
from bs4 import BeautifulSoup as bs
	
# ========================================================================
# FUNCTIONS UTIL
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	print("-" * 50)
	print(section_name)
	print("-" * 50)

def write(content:str = "test", file_name:str = "temp.txt") -> None:
	try:
		# checking and creation of text file
		if(os.path.exists(file_name) == False):
			the_file:TextIOWrapper = open(file_name, "x")
			the_file.close

		# encoding='utf-8' to catch the error with sites that have characters the charmap cant handle
		the_file:TextIOWrapper = open(file_name, "w", encoding='utf-8')
		the_file.write(str(content))
		the_file.close
	except Exception as e:
		section(f"ERROR IN {'write':20}\n{e}")

def read(file_name:str = "temp.txt")->str:
	content = ""
	try:
		# checking and creation of text file
		if(os.path.exists(file_name) == False):
			the_file:TextIOWrapper = open(file_name, "x")
			the_file.close

		# encoding='utf-8' to catch the error with sites that have characters the charmap cant handle
		the_file:TextIOWrapper = open(file_name, "r", encoding='utf-8')
		content:str = the_file.read()
		the_file.close
	except Exception as e:
		content = ""
		section(f"ERROR IN {'read':20}\n{e}")
	return content

# ========================================================================

def get_soup(link:str = "https://example.com/")->bs:
	headers = {
		"User-Agent": (
			"Mozilla/5.0 (X11; Linux x86_64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/138.0.0.0 Safari/537.36"
		),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
	}

	try:
		response:req.Response = req.get(link, 
			timeout=2, 
			headers=headers, 
			allow_redirects=True
		)
	except Exception as e:
		section(f"ERROR IN {'request':20}\n{e}")

	soup = bs(response.content.decode("utf-8"), "html.parser")
	return soup