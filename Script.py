import glob
import os
from subprocess import call
import time


def movefile(dest):
	call(["sudo","cp", dest, "/usr/share/fonts/truetype/newfonts/"])
	call(["fc-cache","-f","-v"])


def check(some='/home/mohak/Downloads/*'):

	list_of_files = glob.glob(some)

	latest_file = max(list_of_files, key=os.path.getctime)
	ext = os.path.splitext(latest_file)[-1].lower()
	return ext,latest_file


ext=check()

#print(ext[0])

if ext[0]==".zip" :
	
	call(["unzip", ext[1]])
	ext2=check()
#	print(ext2[0])
	if(ext2[0]==".ttf" or ext2[0]==".TTF" or ext2[0]==".otf"):
		movefile(ext2[1])




elif(ext[0]==".ttf" or ext[0]==".TTF" or ext[0]==".otf"):
	movefile(ext[1])
