# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: model for inter function communcation in recording scraped data
# 		
# ========================================================================
# HEADERS
# ========================================================================

# ========================================================================
# CLASS
# ========================================================================

class ModelData():
	def __init__(
			self,
			data_label:str = "",
			data:str = ""

		) -> None:
		self.data_label:str = data_label
		self.data:str = data
