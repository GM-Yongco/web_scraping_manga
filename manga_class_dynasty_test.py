# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
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
	chapter_link = "https://dynasty-scans.com/chapters/the_guy_she_was_interested_in_wasnt_a_guy_at_all_ch72"
	chapter: DynastyMangaChapter = DynastyMangaChapter(chapter_link)

	chapter._chapter_title = "test chapter 72"

	chapter.create_folder()
	chapter.get_pannel_links()
	chapter.download_chapter()

# ========================================================================
# MAIN
# ========================================================================

if __name__ == '__main__':
	dynasty_chapter_test()