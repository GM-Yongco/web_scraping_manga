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

from utils import get_soup
from bs4 import BeautifulSoup as bs

from template_model_data import ModelData

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
	)->ModelData:
	ret_val:ModelData = ModelData()
	ret_val.data = ""

	url_base:str = "https://mto.to/chapter"
	url:str = rf"{url_base}/{manga_id}"

	soup:bs = get_soup(link=url)
	soup:bs = soup.select("optgroup option")[-1]

	ret_val.data += f"Title: {soup.get_text().strip()}"
	ret_val.data += "\n"
	ret_val.data += f"Link: https://mto.to/chapter/{soup.get('value').strip()}"

	return ret_val

def fetch_data_sitting_next_to_me()->ModelData:
	ret_val:ModelData = fetch_data_xbato("3041986")
	ret_val.data_label = "sitting_next_to_me"
	return ret_val

def fetch_data_our_sunny_days()->ModelData:
	ret_val:ModelData = fetch_data_xbato("2428150")
	ret_val.data_label = "our_sunny_days"
	return ret_val

def fetch_data_witch_hat()->ModelData:
	ret_val:ModelData = fetch_data_xbato("78556")
	ret_val.data_label = "witch_hat_atelier"
	return ret_val