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

# ========================================================================
# MAIN
# ========================================================================

if __name__ == '__main__':
	separator("START")

	# manga_link:str = "https://dynasty-scans.com/series/the_guy_she_was_interested_in_wasnt_a_guy_at_all"
	# manga_title:str = "The Guy She Was Interested in Wasn't a Guy At All"
	# manga: DynastyMangaDetails = DynastyMangaDetails(manga_link = manga_link, manga_title = manga_title)

	chapter_link = "https://dynasty-scans.com/chapters/the_guy_she_was_interested_in_wasnt_a_guy_at_all_ch00"
	chapter: DynastyMangaChapter = DynastyMangaChapter(chapter_link)

	chapter.create_folder()

	separator("END")