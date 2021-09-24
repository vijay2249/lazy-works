#! python3

# usage of the script
# py.exe mcb.pyw save <keyword>  => saves the text to clipboard
# py.exe mcb.pyw list  => lists all the keywords
# py.exe mcb.pyw <keyword>  => loads the text to clipboard
# py.exe mcb.pyw delete => delete all the copied texts
# py,exe mcb.pyw delete <keyword> => deletes the particular keyword, value pair

# shelve module to read and write the files and text
# pyperclip is to make copy of the text
'''
installation of pyperclip module 
windows:- py -m pip install pyperclip
other os :- pip install pyperclip
'''
# sys module is to read the command line arguments


import shelve, pyperclip, sys

clipBoard = shelve.open('clip')

def usage():
  print("[+] Usage of script\n[+] py.exe mcb.pyw save <keyword> (to save the text)\n[+] py.exe mcb.pyw <keyword> (to copy the text to clipboard)\n[+] py.exe mcb.pyw list (to list all the keywords in the file)\n[+] py.exe mcb.pyw delete (to delete all the copied texts)\n[+] py.exe mcb.pyw delete <keyword> (to delete particular copied text)")
  sys.exit()


if len(sys.argv) == 3:
  if sys.argv[1].lower() == 'save':
    clipBoard[sys.argv[2]] = pyperclip.paste()
    print("[+] saved the text into file")
  elif sys.argv[1].lower() == 'delete':
    del clipBoard[sys.argv[2]]
    print(f"[-] Deleted the copied text releated to keyword {sys.argv[2]}")
  else:
    usage()

elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    print(list(clipBoard.keys()))
  elif sys.argv[1].lower() == 'delete':
    print("[-] Deleting all the copied text in the session")
    for keyword in list(clipBoard.keys()):
      del clipBoard[keyword]
  else:
    if sys.argv[1] in list(clipBoard.keys()):
      print(f"[+] Copied the text with keyword {sys.argv[1]}")
      pyperclip.copy(clipBoard[sys.argv[1]])
    else:
      print("[+] No such keyword in the file")
      print("[+] Here is the list of keywords in the file")
      print(list(clipBoard.keys()))

else:
  usage()

clipBoard.close()