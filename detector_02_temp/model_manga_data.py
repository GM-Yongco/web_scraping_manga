# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: model for inter function communcation in recording relevant scraped manga data
# ========================================================================

class MangaData():
	def __init__(
		self,
		manga_id:str = None,
		manga_title:str = None,
		manga_site:str = None,
		chapter_title:str = None,
		chapter_link_latest:str = None
	) -> None:
		self.manga_id:str = manga_id
		self.manga_title:str = manga_title
		self.manga_site:str = manga_site
		self.chapter_title:str = chapter_title
		self.chapter_link_latest:str = chapter_link_latest

	def __str__(self)->str:
		ret_val:str = ""
		ret_val += f"mid {self.manga_id}\n"
		ret_val += f"mti {self.manga_title}\n"
		ret_val += f"msi {self.manga_site}\n"
		ret_val += f"cti {self.chapter_title}\n"
		ret_val += f"cll {self.chapter_link_latest}\n"
		return ret_val

	def set_from_touple(self, tuple:tuple):
		try:
			self.manga_id:str = tuple[4]
			self.manga_title:str = tuple[0]
			self.manga_site:str = tuple[1]
			self.chapter_title:str = tuple[2]
			self.chapter_link_latest:str = tuple[3]
		except Exception as e:
			print(e)
