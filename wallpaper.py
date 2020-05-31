import ctypes
import os
import random 
import glob

listOfImages = os.listdir()

listOfImages.remove('wallpaper.py')

listOfImages.remove('.git')

aRandomImage=listOfImages[random.randrange(0,len(listOfImages))]

currentPath = os.path.dirname(os.path.abspath(__file__))

pathToBmp = os.path.normpath(currentPath+'\\'+aRandomImage)

ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToBmp , 0)