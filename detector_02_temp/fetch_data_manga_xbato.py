# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: detecting a change in the web 
# 		its also persistent
# 		is abstracted for editing convenience
# ========================================================================
# HEADERS
# ========================================================================

import requests as req
from bs4 import BeautifulSoup as bs

from model_manga_data import MangaData

# ========================================================================
# FETCH RELEVANT DATA
# ========================================================================

# manga id is on the old api is easy to get 
# https://mto.to/chapter/3659715
# new api is weirder
# https://mto.to/title/120455-our-sunny-days/2428150-ch_1
# its the numbers on the right
# but it still works on the old api
# https://mto.to/chapter/2428150
# its just a different formatting in the front end me thinks
# but the old one still works

def fetch_data_xbato(
		manga_id:str = "3041986"
	)->MangaData:
	ret_val:MangaData = MangaData()

	url_base:str = "https://mto.to/chapter"
	url:str = rf"{url_base}/{manga_id}"

	# ====================================================================
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
		response:req.Response = req.get(
			url, 
			timeout=2, 
			headers=headers, 
			allow_redirects=True
		)
	except Exception as e:
		print(e)
		return ret_val

	soup:bs = bs(response.content.decode("utf-8"), "html.parser")
	soup:bs = soup.select("optgroup option")[-1]

	ret_val.chapter_title += f"{soup.get_text().strip()}"
	ret_val.chapter_link_latest += f"{soup.get('value').strip()}"

	return ret_val
