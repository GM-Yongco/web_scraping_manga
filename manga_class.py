# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class for manga downlaoding
# HEADERS ================================================================
import os
import json
import requests
from typing import List, Dict

# ========================================================================
# CLASSES
# ========================================================================

class Template:
	realtive_file_path:str = "scraped/"

	# to clean strings that are illegal as folders and filenames
	def clean_string(self, to_clean:str)->None:
		illegal_characters:List[str] = [ "#","%","&","{","}","\\","<",">","*","?","/","$","!","'",'"',":","@","+","`","|","="]
		for char in illegal_characters:
			to_clean = to_clean.replace(char, "")
		to_clean = to_clean.replace(" ", "_")
		return to_clean

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
		)->bool:

		file_path = f"{self.realtive_file_path}{file_path}{file_name}"

		try:
			print(f"{'start download':20}: {file_name}")
			response = requests.get(self._pannel_link, timeout = 60)
			open(file_path, 'wb').write(response.content)
		except Exception as e:
			print(f"{'download failed':20}: {file_name}")
			print(e)
		else:
			print(f"{'download success':20}: {file_name}")
			self._downloaded = True
		
		return self._downloaded
	
# ========================================================================
class MangaChapter(Template):
	def __init__(self, 
		chapter_link:str = "",
		chapter_title:str = "chapter_title",
		chapter_folder_created:bool = False,
		chapter_complete_download:bool = False
		)-> None:

		self._chapter_link:str = chapter_link
		self._chapter_title:str = chapter_title
		self._chapter_folder_created:bool = chapter_folder_created
		self._chapter_complete_download:bool = chapter_complete_download
		
		self._pannels:List[MangaPannel] = []

	def __str__(self)->None:
		retval:str = f"\n{'CHAPTER':10}:{self._chapter_title}"
		retval = retval + ("\n") + f"{'LINK':10}:{self._chapter_link}"
		retval = retval + ("\n") + ("-"*50)
		for elements in self._pannels:
			retval = retval + ("\n") + str(elements)
		retval = retval + ("\n") + ("-"*50)

		return retval
	
	def __dict__(self)->dict:
		ret_val:dict = {
			"chapter_link":self._chapter_link, 
			"chapter_title":self._chapter_title,
			"chapter_folder_created":self._chapter_folder_created ,
			"chapter_complete_download" : self._chapter_complete_download
		}
		return ret_val

	# Core Functions -----------------------------------------------------

	def create_chapter_folder(self,
		file_path:str = ""
		)->None:

		try:
			path = fr"{self.realtive_file_path}{file_path}{self._chapter_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			print(f"CHAPTER FOLDER CREATED: {self._chapter_title}")
			self._chapter_folder_created = True

	def download_chapter(self, file_path:str = "") -> bool:
		check_val:bool = True
		for index, pannel in enumerate(self._pannels):
			if pannel.download_pannel(
				file_path = file_path + '/' + self._chapter_title + '/' ,  
				file_name = f"{index}.png"
				) == False:
				check_val = False

		self._chapter_complete_download = check_val
		return self._chapter_complete_download
	
	def add_pannel(self, pannel_link:str)->None:
		self._pannels.append(MangaPannel(pannel_link))

	def get_pannel_links(self)->None:
		print("none added in: get_pannel_links")
		
	# Continue Functions -----------------------------------------------------
	

# ========================================================================
class MangaDetails(Template):
	def __init__(self, 
		manga_link:str = "empty",
		manga_title:str = "empty_manga_title"
		)-> None:

		self._manga_link:str = manga_link
		self._manga_title:str = manga_title
		self._manga_folder_created:bool = False

		self._manga_chapters:List[MangaChapter] = []
		self._manga_complete_download:bool = False

	def __str__(self)->None:
		retval:str = f"{'TITLE':10}:{self._manga_title}"
		retval = retval + '\n' + f"{'LINK':10}:{self._manga_link}"
		retval = retval + '\n' + ("="*50)

		for chapter in self._manga_chapters:
			retval = retval + str(chapter)

		retval = retval + '\n' + ("="*50)

		return retval

	def __dict__(self) -> dict:
		ret_val:dict = {
			"manga_link": self._manga_link,
			"manga_title" : self._manga_title,
			"manga_folder_created": self._manga_folder_created,
			"manga_chapters": [],
			"manga_complete_download": self._manga_complete_download
		}
		manga_chapters:list = ret_val["manga_chapters"]
		for chapter in self._manga_chapters:
			manga_chapters.append(chapter.__dict__())

		return ret_val
		
	
	# Core Functions -----------------------------------------------------
	
	def add_chapter(self, 
		chapter_link:str = "",
		chapter_title:str = "chapter_title",
		chapter_folder_created:bool = False,
		chapter_complete_download:bool = False
		)->None:

		self._manga_chapters.append(MangaChapter(
			chapter_link = chapter_link,
			chapter_title = chapter_title,
			chapter_folder_created = chapter_folder_created,
			chapter_complete_download = chapter_complete_download
			))
	
	def get_chapter_links()->None:
		print("none added in: get_chapter_links")

	def create_manga_folder(self)->None:
		try:
			path = fr"{self.realtive_file_path}{self._manga_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			print(f"MANGA FILE CREATED: {self._manga_title}")
			self._manga_folder_created = True
	
	def download_manga(self)->None:
		self.create_manga_folder()
		check_val = True
		for chapter in self._manga_chapters:

			chapter.create_chapter_folder(self._manga_title + '/')
			
			if chapter._chapter_complete_download == False:
				chapter.get_pannel_links()
				if chapter.download_chapter(self._manga_title) == False:
					check_val = False
			
			self.create_resume()
		
		self._manga_complete_download = check_val


	# Resume Functions -----------------------------------------------------
	
	
	resume_file_name = "manga_details.json"

	def create_resume(self)->None:
		check_val = 0
		path = fr"{self.realtive_file_path}{self._manga_title}/{self.resume_file_name}"

		if os.path.exists(path) == False:
			the_file = open(path,"x")   
			the_file.close()

		the_file = open(path, "w", encoding='utf-8')
		json.dump(self.__dict__(), the_file, indent = 4)

	def check_resume(self)->bool:
		path = fr"{self.realtive_file_path}{self._manga_title}/{self.resume_file_name}"

		return True if (os.path.exists(path) == True) else False

	# note: need the link, titile, and folder to have been setup already
	# this function makes get chapter links redundant unless you wanna check for new chapters
	def read_resume(self)->None:
		path = fr"{self.realtive_file_path}{self._manga_title}/{self.resume_file_name}"
		resume_details:dict = json.load(open(path, "r"))
		
		self._manga_link = resume_details["manga_link"]
		self._manga_title = resume_details["manga_title"]
		self._manga_folder_created = resume_details["manga_folder_created"]
		self._manga_complete_download = resume_details["manga_complete_download"]

		for chapters in resume_details["manga_chapters"]:
			print(chapters)
			self.add_chapter(
				chapter_link = chapters["chapter_link"],
				chapter_title = chapters["chapter_title"],
				chapter_folder_created = chapters["chapter_folder_created"],
				chapter_complete_download = chapters["chapter_complete_download"]
				)

	def download_resume(self)->None:

		# updates resume
		self.create_resume()


	
