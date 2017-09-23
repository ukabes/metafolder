""" Metafolder is a simple python utility
---
1. It provides functionality that lets one group a large collection of files.
2. It automatically detects all file properties present in a collection of files.
3. The grouping properties are then selected.
4. Files are then arranged into a folders named by properties.

"""
from pathlib import Path

class MetaFolder:
	""" This is the metafolder class 
		
		Basically provides file grouping functionalities
	"""
	# wkdir instance variable stores the working directory of the class
	# _exts is meant to be a private variable that stores a set of current file properties
	def __init__(self,wkdir="."):
		""" Initialize MetaFolder """
		self.wkdir = Path(wkdir)
		self.exts = self.collect_exts()
		self._exts = self.exts

	def collect_exts(self):
		""" Collects extensions of all the files and returns a set object """

		# Collect all avialable file extensions
			# Go through wkdir, collect a list of all the names of the files
			# Extract file extensions into another list and return a set
		exts  = [file.suffix.split('.')[-1] for file in self.wkdir.iterdir() if file.is_file()]
		return set(exts)

	def fold(self):
		""" This method groups files in their respective folders according to their extensions """

		# Create folders using a prefix and names in _exts, pass over already existing
		for ext in self._exts:
			self.wkdir.joinpath('metafolder_'+ext).mkdir(exist_ok=True)
		# move files into their respective folders

