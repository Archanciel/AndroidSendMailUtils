import pickle 

FILE_PATH='/sdcard/file.bin'
DIC = {'usr':'jschnyder@yahoo.com',
       'pw':'' } # specufy your yahoo mail pw here

# Used to generate the file loaded by the sendmail module
# to obtain the credentials to access your Yahoo email account
with open(FILE_PATH, 'wb') as handle:
    pickle.dump(DIC, handle)
    
with open(FILE_PATH, 'rb') as handle:
    b = pickle.loads(handle.read())
    
print(b)

