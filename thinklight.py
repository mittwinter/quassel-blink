#!/usr/bin/env python3

import os
import subprocess
import time

class ThinkLight:
	_chown = '/bin/chown'
	_chgrp = '/bin/chgrp'
	_chmod = '/bin/chmod'
	_sudo = '/usr/bin/sudo'
	_thinkLightProcPath = '/proc/acpi/ibm/light'
	_thinkLightAdjustUseSudo = True
	_thinkLightProcPathOwner = None
	_thinkLightProcPathGroup = 'thinklight'
	_thinkLightProcPathMode = '664'
	_thinkLightCommandOn = 'on'
	_thinkLightCommandOff = 'off'

	def __init__( self ):
		if not os.access( self._thinkLightProcPath, os.W_OK ):
			commandPrefix = []
			if self._thinkLightAdjustUseSudo:
				commandPrefix += [ self._sudo ]
			if self._thinkLightProcPathOwner is not None:
				subprocess.call( commandPrefix + [ self._chown, self._thinkLightProcPathOwner, self._thinkLightProcPath ] )
			if self._thinkLightProcPathGroup is not None:
				subprocess.call( commandPrefix + [ self._chgrp, self._thinkLightProcPathGroup, self._thinkLightProcPath ] )
			if self._thinkLightProcPathMode is not None:
				subprocess.call( commandPrefix + [ self._chmod, self._thinkLightProcPathMode, self._thinkLightProcPath ] )

	def cmd( self, cmd ):
		try:
			with open( self._thinkLightProcPath, 'w' ) as f:
				f.write( cmd )
				#f.seek( 0 )
		except IOError as e:
			print( e )

	def on( self ):
		self.cmd( self._thinkLightCommandOn )

	def off( self ):
		self.cmd( self._thinkLightCommandOff )

	def blink( self, times, interval ):
		for i in range( times ):
			self.on()
			time.sleep( interval )
			self.off()
			if i < (times - 1):
				time.sleep( interval )

