import os
from random import randint

for name in os.listdir('pendrive'):
	newname='{}.mp3'.format(randint(0,1000000))
	os.rename("pendrive/"+name,"pendrive/"+newname)
