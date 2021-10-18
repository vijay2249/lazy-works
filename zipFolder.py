# --------------------   START OF CODE   -----------------------------

# import modules
try:
  import os
  import zipfile
  import shutil
  import send2trash
  import argparse
  import sys
  import subprocess
except:
  if sys.platform in ['win32','cygwin']:
    subprocess.check_output("python -m pip install --upgrade pip", shell=True)
    subprocess.check_output("python -m pip install send2trash", shell=True)
  else:
    subprocess.check_output("pip install --upgrade pip", shell=True)
    subprocess.check_output("pip install send2trash", shell=True)

class Backup():
  # get folder or directory input from user
  def get_folder_input(self):
    folder_input = str(input("[+] enter folder path: "))
    if folder_input == "":
      return os.getcwd()
    return folder_input

# this is recommended method, taking folder input from command line arguments
# if user forgets to input the command line arguments then get_folder_input() function runs to get the user input
def getDirectory():
  p = argparse.ArgumentParser(description='Zipping the folder')
  p.add_argument("-f","--folder",dest="folder", help="Enter the folder path to that you need to zip")
  p.add_argument('-se','--showErrorFiles',dest='showErrorFiles', help="Whether to show any error in zipping the files", default=True)
  p.add_argument('-sf','--showFiles', dest='showFiles', help='Display the zipping files in the terminal', default=True)
  p.add_argument('-r', '--removeFiles', dest='removeFiles', help='Remove the zipped files (default is false)', default=False)
  p.add_argument('-df', '--deleteForever', dest='deleteForever', help='permanently remove the zipped files (default is false)', default=False)
  options = p.parse_args()
  if not options.folder:
    options.folder = Backup.get_folder_input()
  return options

# handling error while zippong files
'''
if there is any error is zipping files
  in the parent directory, "Error-in-Zipping-Files" folder will be created and the error generated files are moved here

'''
def handleError(new_file):
  newErrorDirectory = "Error-in-Zipping-Files"
  try:
    os.mkdir(newErrorDirectory)
    print(f"[+] Created new directory {newErrorDirectory} to store the error files")
  except FileExistsError as error:
    print(f"[-] {newErrorDirectory} already exists and moving these files here")
  
  shutil.move(new_file, os.path.join(os.getcwd(), newErrorDirectory))

arguments = getDirectory()

try:
  os.chdir(arguments.folder)
except FileNotFoundError as error:
  print(error)
  sys.exit()

userInput = os.getcwd()
print(f"[+] Zipping the directory {os.getcwd()}")
name = os.getcwd().split("\\")[-1] #zip folder name

print(f"[+] Zip folder name: {name}")

os.chdir("..")
newZipFile = zipfile.ZipFile(name+".zip", 'w')
errorFiles = []
for root, folders, files in os.walk(os.getcwd()):
  if userInput in root:
    for f in files:
      new_file = os.path.join(root.replace(userInput,name), f)
      print(f"[+] file path {new_file}")
      try:
        newZipFile.write(new_file, compress_type=zipfile.ZIP_DEFLATED)
        if arguments.showFiles:
          print(f"[+] file in {folders} : {f} added to {name}.zip")
      except ValueError as error:
        print(ValueError.__cause__)
        print(error)
        errorFiles.append(new_file)
        handleError(new_file)
    print("\n")

newZipFile.close()

if arguments.deleteForever:
  shutil.rmtree(arguments.folder)
elif arguments.removeFiles:
  send2trash.send2trash(arguments.folder)

if arguments.showErrorFiles and len(errorFiles) > 0:
  for i in errorFiles:
    print(i)
else:
  print(f"[+] There are no files generating error while zipping the files")