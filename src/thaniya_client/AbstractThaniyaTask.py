

import os

import jk_pathpatternmatcher2
import jk_utils

from .ThaniyaBackupContext import ThaniyaBackupContext





class AbstractThaniyaTask(object):

	@property
	def logMessageCalculateSpaceRequired(self) -> str:
		raise NotImplementedError()
	#

	@property
	def logMessagePerformBackup(self) -> str:
		raise NotImplementedError()
	#

	def calculateSpaceRequired(self, ctx:ThaniyaBackupContext) -> int:
		raise NotImplementedError()
	#

	def performBackup(self, ctx:ThaniyaBackupContext):
		raise NotImplementedError()
	#

#














