#!/usr/bin/env python2

import time

def blinkThinkLight():
	thinklightFile = '/proc/acpi/ibm/light'
	blinkTimes = 5
	blinkInterval = 0.1
	try:
		with open( thinklightFile, 'w' ) as f:
			for i in range( blinkTimes ):
				f.write( 'on' )
				f.seek( 0 )
				time.sleep( blinkInterval )
				f.write( 'off' )
				f.seek( 0 )
				time.sleep( blinkInterval )
	except IOError as e:
		print e

if __name__ == '__main__':
	blinkThinkLight()

