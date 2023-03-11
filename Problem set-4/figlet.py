import figlet
import sys
import random
import pyfiglet 
from pyfiglet import Figlet

figlet = Figlet()

enter = input("Input: ")
print("Output: ",pyfiglet.figlet_format(enter,random.choice(figlet.getFonts())))

