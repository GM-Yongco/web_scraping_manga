# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to 
# HEADERS ================================================================

from manga_class import *

from typing import List
import requests
from bs4 import BeautifulSoup as bs

# ========================================================================
# GLOBAL
# ========================================================================

DYNASTY_LINK:str = "https://dynasty-scans.com"

# ========================================================================
# CLASSES
# ========================================================================

class DynastyMangaChapter(MangaChapter):

	def get_pannel_links(self)->None:
		# getting html of the chapter
		response:requests = requests.get(self._chapter_link)
		soup:bs = bs(response.text , 'html.parser')

		# getting suffixes from nav sidebar
		nav_div:bs = soup.find("div", class_= fr"pages-list")
		nav_a_list:List[bs] = nav_div.find_all("a", class_="page")
		img_link_suffxies:List[str] = []
		for a in nav_a_list:
			img_link_suffxies.append(a.get_text())

		# getting image prefix
		images:List[bs] = soup.find_all('img')
		images_link:str = (images[-1]).get('src')
		portions:List[str] = images_link.split("/")
		
		#trims an empty portion cuz the links start with a '/'
		del portions[0]		
		
		#removes the suffix portion of the template link
		portions[-1] = portions[-1].replace(f"{img_link_suffxies[0]}.webp", "")

		# recombines the link to make prefix template
		img_link_prefix:str = DYNASTY_LINK + '/'
		for p in portions:
			img_link_prefix  = img_link_prefix + p + '/'
		
		# somtimes the prefix and the suffix isnt separated by a '/'
		if portions[-1] != "":
			img_link_prefix = img_link_prefix.rstrip('/')

		# getting the image pannel links / mixing prefix and suffix
		for s in img_link_suffxies:
			self.add_pannel(f"{img_link_prefix}{s}.webp")

		print("GOT PANNEL LINKS")

# ========================================================================
class DynastyMangaDetails(MangaDetails):
	def get_chapter_links()->None:
		pass

