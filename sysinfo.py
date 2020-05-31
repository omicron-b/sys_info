#!/usr/bin/env python3

import psutil
from os import statvfs

raminfo=dict(psutil.virtual_memory()._asdict())
ramused_perc=int(raminfo['used']/raminfo['total']*100)
stat = statvfs('/')
spaceused=int(stat.f_frsize*(stat.f_blocks-stat.f_bavail)/1024/1024) #this is MB
spacetotal=int(stat.f_frsize*stat.f_blocks/1024/1024) #this is MB
spaceused_perc=int((stat.f_blocks-stat.f_bavail)/stat.f_blocks*100)
# debugging
#print (ramused_perc,spaceused_perc)
#print ('\nRAM USED:   '+str(ramused_perc)+'%   '+'\033[92m'+str(ramused_graph*'▒')+str(ramfree_graph*'⌷'+'\033[0m'))
#print ('\nSPACE USED: '+str(spaceused_perc)+'%   '+'\033[92m'+str(spaceused_graph*'▒')+str(spacefree_graph*'⌷'+'\033[0m'))
#print ('')

def graph(perc,graph_name):
	if perc in range(33,67):
		graph_color = '\033[93m' #yellow
	elif perc in range (67,101):
		graph_color = '\033[91m' #red
	else:
		graph_color = '\033[92m' #fallback to green in other cases
	color_drop = '\033[0m'
	print ('\n'+graph_name+"{:02d}".format(perc)+'%   '+graph_color+str(int(perc/10)*'▒')\
		+str((10-int(perc/10))*'⌷')+color_drop)
	return 1

graph(ramused_perc,'RAM USED:   ')
graph(spaceused_perc,'SPACE USED: ')
print ('')
