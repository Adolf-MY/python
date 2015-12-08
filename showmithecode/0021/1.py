#coding=utf8
__author__ = 'Frank'
import os
from hashlib import sha256
from hmac import HMAC

password = 'secret'
salt = None
salt_length = 8
if salt is None:
    salt = os.urandom(salt_length)
if isinstance(password,unicode):
    password = password.encode('UTF-8')

result = password
print result
for i in xrange(1):
    result = HMAC(result,salt,sha256).digest()
    print result