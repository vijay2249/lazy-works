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

import webbrowser
import sys
import pyperclip
import argparse
import time


def get_input():
  if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
    print(address)
  else:
    address = pyperclip.paste()
  return address

start = time.time()
count = 0
while time.time()-start < 5:
  try:
    if webbrowser.open_new_tab("https://google.com/maps/place/" + get_input()):
      count +=1
    # webbrowser.open_new_tab()
  except Exception as error:
    print("[-] Error\n\n")
    print(error)
    print("\n\n")
print(count)