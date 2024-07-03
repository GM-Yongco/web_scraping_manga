# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

import os
from bs4 import BeautifulSoup as bs
import requests

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# FUNCTIONS TEST
# ========================================================================

def write(content:str = "test", file_name:str = "a.txt") -> None:
	# check if references folder exists
	path = "00_REFERENCES/"
	if(os.path.exists(path) == False):
		os.makedirs(path)

	# checking and creation of text file
	path = path + file_name
	if(os.path.exists(path) == False):
		the_file = open(path, "x")
		the_file.close

	# writing in the text file
	the_file = open(path, "w")
	the_file.write(str(content))
	the_file.close
# ========================================================================
# GLOBAL
# ========================================================================

DYNASTY_LINK:str = "https://dynasty-scans.com/"

# ========================================================================
# MAIN 
# ========================================================================


if __name__ == '__main__':
	s:str = "example.com/path/to/file"
	result = s.split("/")
	result.pop()

	print(result)