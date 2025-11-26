# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: detecting a change in the web 
# 		its also persistent
# 		is abstracted for editing convenience
# 		
# ========================================================================
# HEADERS
# ========================================================================

import json
import requests as req

from model_manga_data import MangaData

# ========================================================================
# FUNCTIONS 1
# ========================================================================

def request_mangadex(
		url:str, 
		limit:int = 100		
	)->json:
	
	# limit is how many chapter links to request
	response:req.Response = req.get(
		url=url,
		timeout=2,
		params = {
			"translatedLanguage[]": [
				"en"
			],
			"limit":limit
		}
	)
	return response.json()

# ========================================================================
# FETCH RELEVANT DATA
# ========================================================================

def fetch_data_mangadex(
		manga_id:str = "9d3d3403-1a87-4737-9803-bc3d99db1424",
	)->MangaData:

	ret_val:MangaData = MangaData(
		manga_id = manga_id,
		manga_title = "NULL",
		manga_site = "NULL",
		chapter_title = "NULL",
		chapter_link_latest = "NULL"
	)

	try:
		url:str = ""
		url += "https://api.mangadex.org"
		url += f"/manga/{manga_id}/feed"

		# ========================================
		limit:int = 100
		response_json:json = request_mangadex(url, limit)
		response_len:int = len(response_json['data'])

		# if the response length is = or near the limit, chances are, 
		# the content over the limit so we request for more
		while response_len > (limit-5):
			limit += 50
			response_json = request_mangadex(url, limit)
			response_len = len(response_json['data'])
	
		# ========================================
		# get latest chapter details from api data
		response_formatted:json = response_json["data"]
		response_formatted = sorted(response_formatted, key=lambda x: float(x["attributes"]['chapter']))
		response_formatted = response_formatted[-1]
	
		ret_val.chapter_title = f"{response_formatted['attributes']['title']}"
		ret_val.chapter_link_latest = f"https://mangadex.org/chapter/{response_formatted['id']}"
	except Exception as e:
		raise

	return ret_val