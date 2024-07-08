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

@decorator_start_end
def dynasty_chapter_test()->None:
    chapter_link:str = "https://dynasty-scans.com/chapters/isnt_it_kiss_nijika_week"
    chapter: DynastyMangaChapter = DynastyMangaChapter(chapter_link)

    chapter._chapter_title = (chapter_link.split('/'))[-1]

    # chapter.create_folder()
    # chapter.get_pannel_links()
    # print(chapter.__str__())
    print(chapter.__dict__())
    # chapter.download_chapter()

def dynasty_manga_test()->None:
    manga_link:str = "https://dynasty-scans.com/series/the_guy_she_was_interested_in_wasnt_a_guy_at_all"
    manga_link = "https://dynasty-scans.com/series/fuzoroi_no_renri_side_stories"
    manga: DynastyMangaDetails = DynastyMangaDetails(manga_link = manga_link)

    manga._manga_title = (manga._manga_link.split('/'))[-1]

    manga.get_chapter_links()
    #manga.download_manga()
    #print(str(manga))
    print(manga.__dict__())

# ========================================================================
# MAIN
# ========================================================================

if __name__ == '__main__':
    dynasty_manga_test()
