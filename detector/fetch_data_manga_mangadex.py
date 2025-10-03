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

from template_model_data import ModelData

# ========================================================================
# FETCH RELEVANT DATA
# ========================================================================

def fetch_data_mangadex(
		manga_id:str = "9d3d3403-1a87-4737-9803-bc3d99db1424"
	)->ModelData:
	ret_val:ModelData = ModelData()
	ret_val.data = ""


	try:
		url_base:str = "https://api.mangadex.org"
		url_dir:str = f"/manga/{manga_id}/feed"
		url:str = url_base+url_dir

		limit:int = 100
		def request_mangadex(url:str, limit:int = 100)->json:
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
		# ========================================
		response_json:json = request_mangadex(url, limit)
		response_len:int = len(response_json['data'])

		# if the response length is = to the limit, chances are, 
		# the content over the limit so we request for more
		while response_len > (limit-5):
			limit += 50
			response_json = request_mangadex(url, limit)
			response_len = len(response_json['data'])
		# ========================================
		response_formatted:json = response_json["data"]
		response_formatted = sorted(response_formatted, key=lambda x: float(x["attributes"]['chapter']))
		response_formatted = response_formatted[-1]	
		
		ret_val.data += f"Title: Chapter {int(response_formatted['attributes']['chapter']):03} {response_formatted['attributes']['title']}"
		ret_val.data += "\n"
		ret_val.data += f"Link: https://mangadex.org/chapter/{response_formatted['id']}"
	except Exception as e:
		raise


	return ret_val

def fetch_data_tgswiiwagaa()->ModelData:
	ret_val:ModelData = fetch_data_mangadex("9d3d3403-1a87-4737-9803-bc3d99db1424")
	ret_val.data_label = "tgswiiwagaa"
	return ret_val