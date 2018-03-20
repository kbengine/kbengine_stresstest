# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from Space import Space
import d_entities
import d_spaces

class SpaceCenter(Space):
	def __init__(self):
		Space.__init__(self)
		self.avatars = {}
		self.lastGateCount = 0

	def onEnter(self, entityCall):
		"""
		defined method.
		进入场景
		"""
		self.avatars[entityCall.id] = entityCall
		Space.onEnter(self, entityCall)
		
	def onLeave(self, entityID):
		"""
		defined method.
		离开场景
		"""
		if entityID in self.avatars:
			del self.avatars[entityID]
		
		Space.onLeave(self, entityID)

	def onGateSpawn(self, gate):
		"""
		"""
		self.lastGateCount  += 1
		gate.name += str(self.lastGateCount)
		gate.mapID = self.lastGateCount