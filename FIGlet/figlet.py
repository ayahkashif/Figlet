from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
list = figlet.getFonts()


if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in list:
        sys.exit("Invalid usage")
    else:
        input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
elif len(sys.argv) == 1:
    input = input("Input: ")
    font = choice(list)
    figlet.setFont(font=font)
else:
    sys.exit("Invalid usage")

print(figlet.renderText(input))

