# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

import os
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

from manga_class import *

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

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
# FUNCTIONS SCRAPE
# ========================================================================

def download_img(
		url:str = "https://xfs-n18.xfspp.com/comic/5003/962/628073bbfe272d6dc98e8269/15928920_1444_2048_1035819.jpeg", 
		file_name:str = "a.png"
	) -> None:
	# check if scraped folder exists
	path = "00_Scraped/"
	if(os.path.exists(path) == False):
		os.makedirs(path)

	path = "00_Scraped/" + file_name
	urlretrieve(url, path)

def get_html(url:str = "https://chihuahuaspin.com/") -> str:
	request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
	page = urlopen(request_site)

	html = (page.read().decode(("utf-8")))
	html = str(html.encode('utf-8'))

	return html

# ========================================================================
# FUNCTIONS SCRAPE HOSEKI SPECIFIC
# ========================================================================

def get_chapter_details(
		chapter_link:str = "https://housekinokunimanga.com/manga/houseki-no-kuni-chapter-2/"
	)->MangaChapterDetails:
	
	chapter = MangaChapterDetails()
	chapter.set_chapter_link(chapter_link)
	# chapter.set_chapter_num(int((chapter_link.replace('/', '').split('-'))[-1]))

	chapter_html = get_html(chapter_link)

	for element in bs(chapter_html, "html.parser").find_all("img", class_ = "lazy lazy-hidden"):
		chapter.add_pannel_link(element.get("data-src"))

	return chapter


# ========================================================================
# MAIN 
# ========================================================================

def main():
	first:MangaChapterDetails = get_chapter_details("https://ajinmanga.online/manga/ajin-chapter-14/#google_vignette")
	first.print_attributes()

	unsucessful:list = []
	for index, elements in enumerate(first.pannel_links):
		try:
			download_img(elements, f"hoseki_chapter_{first.chapter_num}/{index+1}.png")
			print(f"success: pannel {index+1}")
		except:
			unsucessful.append(index)
			print(f"unsuccessfull: pannel {index+1}")

	separator("getting unsuccessfuls")

	while (len(unsucessful) != 0):
		for elements in unsucessful:
			try:
				download_img(first.pannel_links[elements], f"hoseki_chapter_{first.chapter_num}/{elements+1}.png")
				print(f"success: pannel {elements+1}")
				unsucessful.remove(elements)
			except:
				print(f"unsuccessfull: pannel {elements+1}")





if __name__ == '__main__':
	separator("START")
	main()
	separator("END")