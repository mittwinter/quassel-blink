#!/usr/bin/env python2

import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import subprocess

blinkThinkLightUseSudo = True
blinkThinklightHelper = '/usr/local/bin/blink-thinklight.py'

# set up main event loop:
DBusGMainLoop( set_as_default = True )

# connect to session bus:
sessionBus = dbus.SessionBus()

# set up callback for quassel notifications(?):
def filterNotifications( bus, message ):
	if message.get_member() != 'Notify':
		return
	args = message.get_args_list()
	# Discard notifications not originating from quassel IRC:
	if len( args ) != 8 or len( args ) < 3 or str( args[ 2 ] ) != 'quassel':
		return
	else:
		thinklightCommand = []
		if blinkThinkLightUseSudo:
			thinklightCommand += [ '/usr/bin/sudo' ]
		thinklightCommand += [ blinkThinklightHelper ]
		subprocess.call( thinklightCommand )

sessionBus.add_match_string_non_blocking( "type='method_call',interface='org.freedesktop.Notifications',member='Notify',path='/org/freedesktop/Notifications',eavesdrop='true'" )
sessionBus.add_message_filter( filterNotifications )

# run event loop:
gobject.MainLoop().run()

