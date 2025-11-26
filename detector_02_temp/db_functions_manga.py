# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating a database to log my sleep schedules
# ========================================================================
# HEADERS
# ========================================================================

from db_connection import SQLConnection
from model_manga_data import MangaData

# ========================================================================
# CLASS
# ========================================================================

class DB_Functions(SQLConnection):
	table_name:str = "table_manga"
	
	def INIT_table_manga(self)->None:
		SQL_command:str = f"""
		CREATE TABLE IF NOT EXISTS {self.table_name} (
			manga_title TEXT,
			manga_site TEXT,
			chapter_title TEXT,
			chapter_link_latest TEXT,

			manga_id TEXT PRIMARY KEY
		);
		"""
		self.SQL_execute(
			SQL_command=SQL_command
		)

	# ========================================================================

	def CREATE_manga_log(
		self,
		manga_id:str = "",
		manga_title:str = "",
		manga_site:str = "",
		chapter_title:str = "",
		chapter_link_latest:str = ""
	):
		SQL_command = f"""
		INSERT INTO {self.table_name} (
			manga_id,
			manga_title,
			manga_site,
			chapter_title,
			chapter_link_latest
		) VALUES (?, ?, ?, ?, ?);
		"""
		params = (
			manga_id,
			manga_title,
			manga_site,
			chapter_title,
			chapter_link_latest,
		)
		self.SQL_execute(
			SQL_command = SQL_command,
			params=params
		)

	# ========================================================================
	
	def GET_manga_log_all(self)->list:
		SQL_command = f"SELECT * FROM {self.table_name}"
		rows:list = self.SQL_fetch(
			SQL_command=SQL_command
		)
		return rows
	
	def GET_manga_log_one(self, manga_id:str = "1") -> list:
		SQL_command = f"""
		SELECT * 
		FROM {self.table_name}
		WHERE manga_id = ?;
		"""
		params = (manga_id)
		rows:list = self.SQL_fetch(
			SQL_command=SQL_command,
			params=params
		)
		return rows

	# ========================================================================

	def UPDATE_manga_log(
		self,
		manga_id:str =None,
		manga_title:str = "NULL",
		manga_site:str = "NULL",
		chapter_title:str = "NULL",
		chapter_link_latest:str = "NULL"
	)-> str:

		ret_val:str = f"UPDATE manga_log-{manga_id}"

		if not manga_id:
			ret_val = f"{ret_val:25}FAILED - manga_id not found"
			return ret_val

		# =====================================
		# get from the current data
		response = self.GET_manga_log_one(manga_id)
		if not response:
			ret_val = f"{ret_val:25}FAILED - manga_log not found"
			return ret_val

		updated_manga_log:MangaData = MangaData()
		updated_manga_log.set_from_touple(response[0])

		# =====================================
		# checking if theres actual changes to implement
		change_flag:bool = False
		if not((manga_title == "NULL") or (manga_title == updated_manga_log.manga_title)):
			updated_manga_log.manga_title = manga_title
			change_flag = True
		if not((manga_site == "NULL") or (manga_site == updated_manga_log.manga_site)):
			updated_manga_log.manga_site = manga_site
			change_flag = True
		if not((chapter_title == "NULL") or (chapter_title == updated_manga_log.chapter_title)):
			updated_manga_log.chapter_title = chapter_title
			change_flag = True
		if not((chapter_link_latest == "NULL") or (chapter_link_latest == updated_manga_log.chapter_link_latest)):
			updated_manga_log.chapter_link_latest = chapter_link_latest
			change_flag = True

		if not change_flag:
			ret_val = f"{ret_val:25}FAILED - no changes"
			return ret_val
		
		# =====================================
		# implementing changes
		SQL_command = f"""
		UPDATE {self.table_name}
		SET
			manga_title = ?,
			manga_site = ?,
			chapter_title = ?,
			chapter_link_latest = ?
		WHERE manga_id = ?;
		"""
		params = (
			updated_manga_log.manga_title,
			updated_manga_log.manga_site,
			updated_manga_log.chapter_title,
			updated_manga_log.chapter_link_latest,
			updated_manga_log.manga_id,
		)
		self.SQL_execute(
			SQL_command = SQL_command,
			params = params
		)
		ret_val = f"{ret_val:25}SUCCESS"

		return ret_val