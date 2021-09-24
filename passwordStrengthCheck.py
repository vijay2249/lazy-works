#! python3
# usage
# 

import re, sys

passwordPattern = re.compile(r'''
  ^(?=.*?[A-Z])                   # at least 1 capital letter
  (?=.*?[a-z])                    # at least 1 lower case letter
  (?=.*?[0-9])                    # at least 1 digit
  (?=.*?[#?!@$%^&*()\-_=+./\\])   # at least 1 special character
  .{8,}$                          # at least 8 characters long
''', re.VERBOSE)

