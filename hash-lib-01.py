import hashlib
import numpy as np
# finding a string which has '1111' at the end of it hash sha256

while True:
    i=np.random.uniform(0.0,1000.0)
    data= 'my name is Saeed and my number is 123.' + str(i)
    m=hashlib.sha256()
    m.update(data.encode('utf-8'))
    hash=m.hexdigest()

    if hash[-4:] == '1111':
        print('Fount it, the string is:')
        print(data)
        print("hash is:")
        print(hash)
        break

#TODO: visit here https://emn178.github.io/online-tools/sha256.html
#       and here https://crackstation.net/ (rainbow crack)

# TODO: search for sha1 algorithm, and also md#
# 
# TODO: in case of adding an increasing integer 
# try to create a version of this program working 
# with all the different cases of upper and lower case letters
# create an array of all possible cases, and check all that array elements
