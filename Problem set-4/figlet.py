import sys
import random
import pyfiglet
from pyfiglet import Figlet

figlet = Figlet()
# if the entered sys.argv is of 1 word then random text will generate
if len(sys.argv) == 1:

    enter = input("Input: ")
    print("Output: ", pyfiglet.figlet_format(
        enter, random.choice(figlet.getFonts())))
# else if the command line is od 3 words it will print your written font
elif len(sys.argv) == 3:
    # if the 1 word if not -f or --font then exit code
    if (sys.argv[1] == "-f" or sys.argv[1]=="--font"):
        # the 2 word that is the font name is sent to the variable f
        f = sys.argv[2]
        #if it execute succesfully then input the value
        try:
            figlet.setFont(font=f)
            enter = input("Input: ")
            print("Output: ", figlet.renderText(enter))
        #otherwise error occurs
        except:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
