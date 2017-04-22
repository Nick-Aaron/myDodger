#main.py 
from distutils.core import setup 
import glob 
import py2exe 	  
setup(windows = ["main.py"],
      data_files = [("resources",
                    ['resources\\background.wav',
                     'resources\\baddie.png',
                     'resources\\gameOver.wav',
                     'resources\\player.png',
                     'resources\\simsunb.ttf'])])

