import xbmc
import xbmcaddon
import os
import subprocess

addon = xbmcaddon.Addon()
launcher = os.path.join(addon.getAddonInfo('path'), 'retroarch.bat')
 
xbmc.executebuiltin('XBMC.Action(Stop)')
subprocess.call(['cmd', '/c', 'start', '/min', launcher])
