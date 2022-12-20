# import webbrowser
# import time

# start = time.time()
# print(start)

# while (time.time()-start) < 5:
#   webbrowser.open("https://github.com")

# webbrowser.close()


# ---------target
# 1. get arguments from user (this is address)
# 2. join the address
# 3. add it to the maps.google.com url
# 4. open the browser using webbrowser module(prefered selenium -> learn about it)
# https://pypi.org/project/selenium/ -> selenium python stable release 

#! python3

# import webbrowser
# import sys
# import pyperclip
# import argparse
# import time


# def get_input():
#     #get input from user
#     if len(sys.argv) > 1:
#         address = ' '.join(sys.argv[1:])
#         print(address)
#     else:
#         #else get input from copied text
#         address = pyperclip.paste()
#     return str(address)

# webbrowser.open_new_tab("https://google.com/maps/search/" + get_input())

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoJuilet.txt', 'wb')
for chucks in res.iter_content(1000000):
    playFile.write(chucks)
playFile.close()