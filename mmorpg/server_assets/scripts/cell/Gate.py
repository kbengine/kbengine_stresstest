# -*- coding: utf-8 -*-
import random
import math
import time
import SCDefine
import d_spaces
import KBEngine
from KBEDebug import *
from interfaces.GameObject import GameObject

class Gate(KBEngine.Entity, GameObject):
	"""
	这是一个传送门实体，当玩家进入传送门“self.addProximity(5.0, 0, 0)”的区域，
	传送门将玩家传送至指定地方
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self) 
		
		self.addTimer(1, 0, SCDefine.TIMER_TYPE_HEARDBEAT)				# 心跳timer, 每1秒一次

		if self.getCurrSpace().className == "SpaceCenter":
			self.mapID = 0
			self.getCurrSpace().onGateSpawn(self)
		
	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.className, self.id, tid, userArg))
		if SCDefine.TIMER_TYPE_HEARDBEAT == userArg:
			self.onHeardTimer()
		
		GameObject.onTimer(self, tid, userArg)
		
	def onHeardTimer(self):
		"""
		entity的心跳
		"""
		self.addProximity(3.0, 0, 0)
		
	def onEnterTrap(self, entityEntering, range_xz, range_y, controllerID, userarg):
		"""
		KBEngine method.
		有entity进入trap
		"""
		if entityEntering.isDestroyed or not entityEntering.isPlayer():
			return
			
		#DEBUG_MSG("%s::onEnterTrap: %i entityEntering=(%s)%i, range_xz=%s, range_y=%s, controllerID=%i, userarg=%i" % \
		#				(self.className, self.id, entityEntering.className, entityEntering.id, \
		#				range_xz, range_y, controllerID, userarg))

		if self.uid == 40001003: # cell-scene -> cell-scene
			spaceData = d_spaces.datas.get(entityEntering.spaceUType)
			entityEntering.teleport(None, spaceData["spawnPos"], tuple(self.direction))
		elif self.uid == 40001004: # center->cell-scene
			gotoSpaceUType = 1000 + self.mapID
			spaceData = d_spaces.datas.get(gotoSpaceUType)
			entityEntering.teleportSpace(gotoSpaceUType, spaceData["spawnPos"], tuple(self.direction), {})
		elif self.uid == 40001002: # goback scene
			gotoSpaceUType = entityEntering.lastSpaceUType
			spaceData = d_spaces.datas.get(gotoSpaceUType)
			entityEntering.teleportSpace(gotoSpaceUType, spaceData["spawnPos"], tuple(self.direction), {})
		elif self.uid == 40001005: # goto center
			if "bot_" in entityEntering.name:
				return

			gotoSpaceUType = 1
			spaceData = d_spaces.datas.get(gotoSpaceUType)
			entityEntering.teleportSpace(gotoSpaceUType, spaceData["spawnPos"], tuple(self.direction), {})
		else:					 # cell-scene to 副本
			if entityEntering.spaceUType > 1000 and entityEntering.spaceUType < 3000:
				gotoSpaceUType = 3001
				return
			else:
				gotoSpaceUType = entityEntering.lastSpaceUType
			
			spaceData = d_spaces.datas.get(gotoSpaceUType)
			entityEntering.teleportSpace(gotoSpaceUType, spaceData["spawnPos"], tuple(self.direction), {"spaceKey" : entityEntering.spaceUType})

	def onLeaveTrap(self, entityLeaving, range_xz, range_y, controllerID, userarg):
		"""
		KBEngine method.
		有entity离开trap
		"""
		if entityLeaving.isDestroyed or not entityLeaving.isPlayer():
			return
			
		#INFO_MSG("%s::onLeaveTrap: %i entityLeaving=(%s)%i." % (self.className, self.id, \
		#		entityLeaving.className, entityLeaving.id))
				
