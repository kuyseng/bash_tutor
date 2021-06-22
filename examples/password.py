#!/usr/bin/python

import hashlib

def salted_password(password, salt):
  password_salt = password + salt
  result = hashlib.sha256(password_salt.encode()).hexdigest()
  return result



import sys
result = salted_password(sys.argv[1], sys.argv[2])

#password = raw_input("Enter password: ")
#salt = raw_input("Enter salt: ")
#result = salted_password(password, salt)
print(result)
