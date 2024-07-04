# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu 2024/07/04
# Description		: A template class to 
# HEADERS ================================================================

from manga_class_dynasty import *


# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

def decorator_start_end(func):
	def wrapper():
		separator(f"START\t: {func.__name__}")
		func()
		separator(f"END\t: {func.__name__}")
	return wrapper

# ========================================================================
# FUNCTIONS TEST
# ========================================================================

def dynasty_chapter_test()->None:
	chapter_link:str = "https://dynasty-scans.com/chapters/isnt_it_kiss_nijika_week"
	chapter: DynastyMangaChapter = DynastyMangaChapter(chapter_link)

	chapter._chapter_title = (chapter_link.split('/'))[-1]

	chapter.create_folder()
	chapter.get_pannel_links()
	print(chapter.__str__())
	chapter.download_chapter()

# ========================================================================
# MAIN
# ========================================================================

if __name__ == '__main__':
	dynasty_chapter_test()