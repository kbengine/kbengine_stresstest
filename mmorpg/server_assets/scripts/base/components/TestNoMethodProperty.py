# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class TestNoMethodProperty(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		INFO_MSG("TestNoMethodProperty::onAttached(): owner=%i" % (owner.id))
		
	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("TestNoMethodProperty::onDetached(): owner=%i" % (owner.id))