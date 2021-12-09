# lazy-works

## Hope these scripts works later-on to have a little more sleep for me
## Learnings from Automate-Boring-Stuff-By-Python book

# Contents in this Repository

## [Zip a Folder using python](./zipFolder.py)

### usage: 
`python zipFolder.py -f <FolderPath>`

### Description

This then create a zip folde with the name of the folder mentioned and the folder is then placed inside the zip folder

input: Desktop/asb/<file>

output: Desktop/asb<zipFolder>/asb/<files>

## [Backup Versions of Folder](./backupZip.py)

### usage: 
`python backupZip.py -p <folderPath>`

### Description:
Same as [Zip a Folder using python](./zipFolder.py)

## [Delete duplicate files](./delete_copies.py)

### usage:
`python delete_copies.py <folder1> <folder2> <folder3> (and so on) <print/trash/delete>`

### Description
You can enter as many folders as you can, but the script checks for just the mentioned folder and its child folders, it does not include parent folder

last arguments explanation:

  `print` - just print the duplicate files

  `trash` - deletes all the duplicate files in the folder and sends them to trash/recycle bin
  
  `delete` - deletes the duplicate files permanently (can't be found in trash after this is executed, there is backup too in case this is just unfortunate command execution)

## [Delete duplicate files code-2](./copies.py)

### Description:
same as [Delete duplicate files](./delete_copies.py)

## [Python MultiClip Board](./mcb.py)

### Usage:

`py.exe mcb.py save <keyword>` => saves the text to clipboard

`py.exe mcb.py list` => lists all the keywords

`py.exe mcb.py <keyword>` => loads the text to clipboard

`py.exe mcb.py delete` => delete all the copied texts

`py.exe mcb.py delete <keyword>` => deletes the particular keyword, value pair

### Description: 
shelve module to read and write the files and text

pyperclip is to make copy of the text

installation of pyperclip module

    windows:- py -m pip install pyperclip
    other os :- pip install pyperclip

sys module is to read the command line arguments


## [Mini Password Locker using Python](./passwordLocker.py)

### Usage:
python passwordLocker.py passwordsuggestions -> gives suggestions to create strong password

`python passwordLocker.py delete` -> deletes all the stored passwords

`python passwordLocker.py list` -> to list all the sites stored in the list

`python passwordLocker.py copy <site>` -> to copy the site password to the clipboard

`python passwordLocker.py delete <site>` -> removes the site and password from the list

`python passwordLocker.py update <site> <password>` -> updates the already present password

`python passwordLocker.py save <site> <password>` -> to save a password corresponding to site

`python passwordLocker.py new <site> <length>` -> generated strong password of given length for site mentioned and stores it

### Description
This basically creates a binary file called locker in your directory where this file is downloaded.

Based on your OS this creates different files,
    
    in Windows it created three files with .dat .dir and .bak extensions
    in mac os and linux systems it creates just .db extension file

This is the created using shelve module

The user password is then encrypted by using the Fernet methods in cryptography module and then stored into the binary file created

When user requests for the particular password to be copied to the clipboard then the program decrypts the password stored and the final value is copied to clipboard

User can also ask for new password generation in the program using the arguments
    
    python passwordLocker.py new <site> <length_of_password>

This then creates new password of given length by using password_generator module

Also the password strength is checked for each password, if it is not a strong password then error pops up giving some suggestions to make a good strong password


### Disclaimer:
`ALL THE SITE NAMES AND PASSWORDS ARE CASE SENSITIVE`

## [Extract Mails and Numbers from file](./ExtractNumbers_Mail.py)

find you file location and then replace the inbuilt one with yours

also dont forget to add one more backslash wherever there is backslash in your file location path
