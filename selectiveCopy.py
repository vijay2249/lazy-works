import os
import sys
import argparse

class Backup:
  def get_path():
    return str(input('Enter Folder path: '))
  
  def get_file():
    return str(input('Enter the file extension: '))

def get_arguments():
  vcn = argparse.ArgumentParser(description='Selective copy of files')
  vcn.add_argument('--path', dest='path', help='Path of the folder that you want to copy the required files in')
  vcn.add_argument('--file',dest='file', help='type of files you want to copy')
  options = vcn.parse_args()
  if not options.path:
    options.path = Backup.get_path()
  if not options.file:
    options.file = Backup.get_file()
  return options

arguments = get_arguments()

try:
  os.chdir(arguments.path)
  print(os.getcwd())

except FileNotFoundError as error:
  print(error)
  sys.exit()


print(arguments)