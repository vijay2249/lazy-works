#! python3

'''
1. reads the regex search pattern from user -> keep the link to the pythex.org site for more information

2. uses the pattern as the parameter in the script

3. search for the txt files in the current folder

4. search for the pattern given by user in the content in all the txt files in the folder

5. print the matching results
'''

import re, os

userInput = str(input("Enter regex pattern: "))

pattern = re.compile(r''' ''')