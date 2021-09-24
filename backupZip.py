#! python3

import os, sys, zipfile, argparse

def folderPathByUser():
  folderInput = str(input("Enter folder path: "))
  return folderInput

def moveErrorFiles():
  displayMessage = '[+] If there are any files that are causing error while zipping them,'
  print(displayMessage)
  moveFiles = bool(input("Do you want to coy files to new location for reference(True/False): "))
  return moveFiles

def get_folder_path():
  p = argparse.ArgumentParser(description="Backup zip folder for the current version")
  p.add_argument('-p','--path',dest='path',help='Path of the folder that needs to be zipped')
  p.add_argument('-se','--showErrorFiles',dest='showErrorFiles', help="Whether to show the files that caused error in zipping them", default=True)
  p.add_argument('-me','--moveErrorFiles',dest='moveErrorFiles', help='Move the error files to a new location in the parent directory for reference, (by default it copies the files to new folder)', default=False)
  options = p.parse_args()
  if not options.path:
    options.path = folderPathByUser()
  if not options.moveErrorFiles:
    options.moveErrorFiles = moveErrorFiles()
  return options

userInput = get_folder_path()

'''
If there is any error in zipping the files, then the program creates a new folder and moves the error files here
'''
def handleError(new_file):
  newErrorDirectory = "Error-in-Zipping-Files"
  if not os.path.exists(newErrorDirectory):
    os.mkdir(newErrorDirectory)
    print(f"[+] Created new directory {newErrorDirectory} to store the error files")
  if userInput.moveErrorFiles:
    shutil.move(new_file, os.path.join(os.getcwd(), newErrorDirectory))
    print(f"[+] Moved error file {new_file} to {newErrorDirectory}")
  else:
    shutil.copy2(new_file, os.path.join(os.getcwd(), newErrorDirectory))
    print(f"[+] copied error file {new_file} to {newErrorDirectory}")

try:
  os.chdir(userInput.path)
except FileNotFoundError as error:
  print(f"[-] {error}")
  print("[-] Quitting the program")
  sys.exit()

name = os.path.basename(os.getcwd())
os.chdir("..")

version = 1
while True:
  zipName = name + "_" + str(version) + ".zip"
  if not os.path.exists(zipName):
    break
  version += 1

backupZipFile = zipfile.ZipFile(zipName, 'w')
errorFiles = []

for root, folders, files in os.walk(name):
  for f in files:
    filePath = os.path.join(root, f)
    try:
      backupZipFile.write(filePath, compress_type=zipfile.ZIP_DEFLATED)
    except ValueError as error:
      print(f"[-] Error while Zipping file")
      print(f"[-] Error: {error}")
      errorFiles.append(filePath)
      handleError(filePath)

backupZipFile.close()

if userInput.showErrorFiles and len(errorFiles)>0:
  print("[-] These are the files that has error while zipping them...")
  for i in errorFiles:
    print(i)
else:
  print("[+] Yay.... All Files backedup successfully")