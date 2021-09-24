# usage of shutil module to copy and replace the files and folders and other basic needs
# shutil - shell utilities


# import os, shutil

# shutil.copy(source, destination)
# shutil.copy("abc.txt", "C:\\Users\\User\\Desktop\\Hello")
'''
this copies the text/content in abc.txt file
  since the destination is folder it creates a new file with same name in the destination folder
  copies all the text/contents to the created file,
  finally returns the path of the new file
'''

# shutil.copy("abc.txt", "xyz.txt")
'''
in this case, the copied text/content is pasted to the file xyz.txt which is automatically created
is no absolute path is mentioned then it considers the relative path
in general the meta data is not totally copied for the files that are copied using copy(),
for more meta data to be copied than the previous one(may not be the complete meta data of the file)
we use copy2()  -> this works the same as the copy() except that it acquires more metadata than compared to copy() for the files
'''

# shutil.copytree(source, destination)
# shutil.copytree("C:\\Users\\User\\Desktop", "F:\\Desktop_files_backup")
'''
this copies all the folders and files and sub-folders in the source path mentioed
then created a new folder as mentioned in the destination and
then the copied files and folders are pasted here

again this retuns the destination path (new location of the copied files)
'''

# shutil.move(source, destination)
# shutil.move("index.html", "NewFolder\\index2.html")
'''
moves the source file to the destination file (this move() method dont accept folder path as the parameter)
else with the file name mentioned
if the destination file already exists then the previous content is overwritten be the copied content
also note that file extensions can also be changed like,

if there is no path as mentioned in the destination parameter dont exists, then this function throws error
'''
# shutil.move("index.html", "NewFolder\\index2.txt") 
'''
this reads the contents in the index.html file and creates a new destination file as mentioned
writes all the content to the created file, then deletes the source file 

'''

# renaming the files is generally done by using the os module rename(pastName, newName) method

# os.unlink(<filePath>) # this deletes the "file" mentioned in the path
# os.rmdir(<folderPath>) #this deletes the "folder" as mentioned in the path, also have to make sure that the folder is empty do that

# shutil.rmtree(<folderPath>)  #this deletes folder along with the subfolders and  the files in the folder path mentioned
# this premanently deletes all the files, like these files will be deleted from trash/recycle-bin too
# most of the times its good option print the files and folders that are being deleted, to make sure that you actually deleting the correct ones


# import send2trash
# send2trash.send2trash(<filePath>) 
# this third party module deletes the folder mentioed, this folder can be restored from recycle bin 
# this module works in only one direction, this can send modules to recycle bin but cannot extract files from recycle bin


###########    walking through a directory tree ####################
# os.walk(<directory>) # - returns three values current folder name, list of subfolders , list of files 
# this walk() keeps the working directory as same and iterates over all the folders in the directory and returns the three items on each iteration on folder

# #  -------------------------------------------
# import os

# for folder, subfolders, files in os.walk("F:\\automation"):
#   print("Current folder: " + folder)
#   for subfolder in subfolders:
#     print("subfolder of " + folder + ": " + subfolder)
#   for f in files:
#     print("file in "+ folder + ": " + f)
#   print("\n")
# # --------------------------------------------------
# os.walk("F:\\automation")
'''
this returns the folders, subfolders in folders, files in the folders as list of strings
'''


#######################   zipping and unzipping the files and folders   ##################################

'''
first we import the zipfile module to read and write zip files and folders
'''
# import os, zipfile
# os.chdir("C:\\Users\\User\\Desktop")
# newZipFile = zipfile.ZipFile('new.zip')

# ZipFile.getinfo(<fileInsideNewZipFile>) -> returns the info about fileInsideNewZipFile
# like wise there are differnet functions for the ZipFile function to read and write and create a file or folder in zip

# use dir(<method>) to get the function names available for that particular method

# print(newZipFile.printdir())


# ----- for extracting zip files we use ZipFile.extractall90 function
# newZipFile.extractall()


# -------------------  zipping a folder--------------
# import os, zipfile
# os.chdir("F:\\NITW_Study\\sem_2-1")
# print(os.getcwd())

# sem_2_1 = zipfile.ZipFile('F:\\NITW_Study\\sem_2_1.zip', 'w')

# for folder, subfolders, files in os.walk("F:\\NITW_Study\\sem_2-1"):
#   # print("Current folder: " + folder)
#   # for subfolder in subfolders:
#     # print("subfolder of " + folder + ": " + subfolder)
#   for f in files:
#     new_file = os.path.join(folder, f)
#     sem_2_1.write(new_file)
#     print("file in "+ folder + ": " + f + " added to sem_2_1.zip")
#   print("\n")

# sem_2_1.close()

# ------------------- single folder --------------------


#  ------------   zip all the folders in directory ----------------
'''
zip all the filders in NITW_Study and move the folders to trash
if any errors then create a new error folder and move the files to the error named folder

'''

import os, zipfile, shutil, send2trash, argparse

os.chdir("F:\\NITW_Study")
print(os.getcwd())
subFolders = []

for folders, subfolders, files in os.walk(os.getcwd()):
  subFolders = subfolders
  break

errorFiles = []

def moveErrorFiles(new_file):
  newErrorDirectory = "Error"
  try:
    os.mkdir(newErrorDirectory)
    print(f"Creating new folder named {newErrorDirectory} to move error files")
  except FileExistsError:
    print("File already exists, moving the files")
  shutil.move(new_file, os.path.join(os.getcwd(), newErrorDirectory))

for folder in subFolders:
  newZipFile = zipfile.ZipFile(folder+'.zip', 'w')
  for folders, subfolders, files in os.walk(folder):
    for f in files:
      new_file = os.path.join(folders, f)
      try:
        newZipFile.write(new_file)
        print("file in "+ folders + ": " + f + " added to " + folder+".zip")
        send2trash.send2trash(new_file)
      except ValueError as error:
        print("\n")
        print(ValueError.__cause__)
        print(error)
        print("\n")
        errorFiles.append(new_file)
        moveErrorFiles(new_file)

  newZipFile.close()
  print("\n")

print("\n\n")
print(f"Total Exception Files: {len(errorFiles)}" )
print("\n\n")
print("Exception Files:")
print(errorFiles)


# ------------------  end of code ---------------------------------------------

'''private ip and public IP'''
'''static public IP '''


# ------------------------------   start of project ---------------------------------
'''
we have to modify the us_date to european date in the filenames not in the text of file
'''

# import os, re

# us_date_pattern = re.compile(r'''
#   ^(.*?)  #any text before group - 1
#   (\d{1,2})  # MM  group - 2
#   -  # -
#   (\d{1,2})  #  DD  group - 3
#   -  # -
#   (\d{4})  #  YYYY  group - 4
#   (.*?)$ # any-text after  group - 5
# ''',re.VERBOSE)

# for f in os.listdir(os.getcwd()):
#   f.replace(" ", "_")
#   print(f)
#   us_date = us_date_pattern.search(f)
#   if us_date == None:
#     continue
#   else:
#     before = us_date.group(1)
#     mm = us_date.group(2)
#     dd = us_date.group(3)
#     yyyy = us_date.group(4)
#     after = us_date.group(5)

#     new_name = before + dd + "-" + mm + "-" + yyyy + after

#     os.rename(f, new_name)
#     # shutil.move(f,new_name) -> this is another method

# --------------------------------   end of project ------------------------------------




# -------------- replace " " with "-"  code ----------------------------

# import os

# for f in os.listdir(os.getcwd()):
#   if ' ' in f:
#     os.rename(f, f.replace(' ','-'))

# print(os.listdir(os.getcwd()))