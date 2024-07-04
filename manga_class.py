# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class for manga downlaoding
# HEADERS ================================================================
import os
import requests
from typing import List

# ========================================================================
# CLASSES
# ========================================================================

class Template:
	realtive_file_path:str = "scraped/"

# ========================================================================
class MangaPannel(Template):
	def __init__(self, pannel_link: str) -> None:
		self._pannel_link: str = pannel_link
		self._downloaded: bool = False
	
	def __str__(self)->None:
		return f"status: {self._downloaded}\t{self._pannel_link}"
	
	def download_pannel(
		self,
		file_path:str = "",
		file_name:str = "manga_pannel.png"
		)->None:

		file_path = f"{self.realtive_file_path}{file_path}{file_name}"

		try:
			print(f"{'star download':20}: {file_name}")
			response = requests.get(self._pannel_link, timeout = 60)
			open(file_path, 'wb').write(response.content)
		except Exception as e:
			print(f"{'download failed':20}: {file_name}")
			print(e)
		else:
			print(f"{'download success':20}: {file_name}")
			self._downloaded = True
	
# ========================================================================
class MangaChapter(Template):
	def __init__(self, 
		chapter_link:str = "0",
		chapter_title:str = "chapter_title"
		)-> None:

		self._chapter_link:str = chapter_link
		self._chapter_title:str = chapter_title
		self._chapter_folder_created:bool = False
		self._pannels:List[MangaPannel] = []

	def __str__(self)->None:
		retval:str = f"{'CHAPTER':10}:{self._chapter_title}"
		retval = retval + f"{'LINK':10}:{{self._chapter_link}}"
		retval = retval + ("\n") + ("-"*50)
		for elements in self._pannels:
			retval = retval + ("\n") + str(elements)
		retval = retval + ("\n") + ("-"*50)

		return retval
	
	# Core Functions -----------------------------------------------------

	def create_folder(self,
		file_path:str = ""
		)->None:

		try:
			path = fr"{self.realtive_file_path}{file_path}{self._chapter_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			self._chapter_folder_created = True
	
	def add_pannel(self, pannel_link:str)->None:
		self._pannels.append(MangaPannel(pannel_link))

	def download_chapter(self):
		for index, links in enumerate(self._pannels):
			links.download_pannel(file_path = self._chapter_title + '/' ,  file_name = f"{index}.png")
		print("CHAPTER DOWNLOAD TERMINATED")
 
	def get_pannel_links()->None:
		pass
		
# ========================================================================
class MangaDetails(Template):
	def __init__(self, 
		manga_link:str = "0",
		manga_title:str = ""
		)-> None:

		self._manga_link:str = manga_link
		self._manga_title:str = manga_title
		self._manga_folder_created:bool = False
		self._chapters:List[MangaChapter] = []

	def __str__(self)->None:
		retval:str = f"{self._manga_title}:{self._manga_link}"
		retval = retval + ("="*50)

		for elements in self._chapters:
			retval = retval + str(elements)

		retval = retval + ("="*50)

		return retval

	# Core Functions -----------------------------------------------------
	
	def create_manga_folder(self)->None:
		try:
			path = fr"{self.realtive_file_path}{self._manga_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			self._manga_folder_created = True
	
	def create_manga_chapters(self)->None:
		for chapter in self._chapters:
				pass


	def add_chapter(self, chapter_link, chapter_title)->None:
		self._chapters.append(MangaChapter(chapter_link, chapter_title))
	
	def get_chapter_links()->None:
		pass

	