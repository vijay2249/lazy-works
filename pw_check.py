#! python3

###############     not yet implemented this yet ############################
# master key is to make sure to opened by correct person
# if the master key is correct then copies the required password to clipboard
# else return wrong password -> also for security reasons master key is attempts is accepted only 7 times
# passwordLocker is a dictionary with key as site name and value as password
# these fields are site and password
#############################################################################

# usage
# pyhton file.py delete -> deletes all the stored passwords
# python file.py list -> to list all the sites stored in the list
# python file.py copy <site> -> to copy the site password to the clipboard
# python file.py delete <site> -> removes the site and password from the list
# python file.py update <site> <password> -> updates the already present password
# python file.py save <site> <password> -> to save a password corresponding to site
# python file.py new <site> <length> -> generated strong password of given length for site mentioned and stores it


# re module is to search for the patterns in the text
# sys module is to grab the arguments from user
# pyperclip module used to copy the text to the clipboard
# shelve module is used to store the variables in binary file
# password_generator module is used to generate new strong password
# cryptography module is used to encrypt and decrypt the passwords

import re, sys, pyperclip, shelve
from password_generator.password import Password
from cryptography.fernet import Fernet

p = Password() #password method initiation
locker = shelve.open('locker')

# required password pattern
passwordPattern = re.compile(r'''
  ^(?=.*?[A-Z])                   # at least 1 capital letter
  (?=.*?[a-z])                    # at least 1 lower case letter
  (?=.*?[0-9])                    # at least 1 digit
  (?=.*?[#?!@$%^&*()\-_=+./\\])   # at least 1 special character
  .{8,}$                          # at least 8 characters long
''', re.VERBOSE)

def usage():
  f = "[+] python pw_check.py"
  print("[+] Usage of the file\n")
  print(f"{f} delete -> (to delete all the passwords)")
  print(f"{f} list -> (to list all the sites stored in file)")
  print(f"{f} copy <site> -> (copies the site password to the clipboard)")
  print(f"{f} delete <site> -> (deletes the password for particular site given)")
  print(f"{f} save <sit> <password> -> (to save the password to file)")
  print(f"{f} update <site> <password> -> (updates the password in the file)")
  print(f"{f} new <site> <length> -> (generates the new password and stores it in the file)")

def badPassword():
  print("[-] Bad Password")
  print("[+] Here are some suggestions")
  print("[+] password must contain")
  print("\t[+] atleast one capital letter\n\t[+] atleast one small letter\n\t[+] atleast one letter\n\t[+] atleast one special character\n\t[+] atleast should be 8 characters long")


if len(sys.argv) == 2:
  if sys.argv[1].lower() == 'delete':
    for i in locker:
      del locker[i]
    print("[-] Deleted all the saved passwords")
  
  elif sys.argv[1].lower() == 'list':
    print(list(locker.keys()))
  
  else:
    usage()

elif len(sys.argv) == 3:
  if sys.argv[2] in locker.keys():
    if sys.argv[1].lower() == 'copy':
      safeBox = locker[sys.argv[2]] #this contains key and encrypted password
      crypter = Fernet(safeBox['key']) #using the key to decrypt the password
      decrypt = crypter.decrypt(safeBox['password']) #decrypt the password using the key 
      decrypt = str(decrypt,'utf8') # converting the datatype into string using utf8 encoding
      pyperclip.copy(decrypt) #copy the password to clipboard
    
    elif sys.argv[1].lower() == 'delete':
      del locker[sys.argv[2]]
    
    else:
      usage()
  
  else:
    print("[-] No such site exists in the file")

elif len(sys.argv) == 4:
  if sys.argv[1] not in ['save', 'update', 'new']:
    usage()
  
  else:
    key = Fernet.generate_key() # generates each key for each site
    crypter = Fernet(key) # generates method based on the key
    safeBox = {"key":key} 
    #safe box is temporary dictionary that stores the current site password and key then it appends it to the binary file
    
    if sys.argv[1].lower() == 'new':
      if int(sys.argv[3]) < 8:
        print("Length of the password should be atleast 8")
      # if length is less than 8 return bad choice
      
      else:
        while True: #while loop runs until the generated password is strong and meet the requirements
          newPassword = p.generate_password(int(sys.argv[3])) #generates new password
          if passwordPattern.search(newPassword):
            encrypt = crypter.encrypt(newPassword.encode('utf8')) #encrypt the password
            safeBox["password"] = encrypt #save it in the safeBox
            if sys.argv[2] in locker.keys(): # if the site is already present then it overrides the previous one
              print("[-] site password already present locker, old password is over written by new password")
            locker[sys.argv[2]] = safeBox #append the safeBox to locker
            pyperclip.copy(newPassword) #copy the generated password
            print("[+] generated password is copied to clipboard") 
            break # if the password meets the requirements then we break the loop
    
    # check for user entered password strength
    elif passwordPattern.search(sys.argv[3]):
      encrypt = crypter.encrypt(sys.argv[3].encode('utf8')) #encrypt the password
      safeBox['password'] = encrypt #save the password
      if sys.argv[1].lower() == 'save':
        print("[+] Successfully saved the password")
      
      elif sys.argv[1].lower() == 'update':
        if sys.argv[2] not in locker.keys():
          print("[-] No prior stored credentials found with site, creating new credentials")
      
      else: #if the commands are wrong then run usage()
        usage()
      locker[sys.argv[2]] = safeBox
    
    else: #if the password is bad password then run badPassword()
      badPassword()

else: #if the commands are wrong then run usage()
  usage()

locker.close() # close locker
sys.exit() #exit the process
