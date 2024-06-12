f = open("file_handeling/mytxtfile.txt",'w')
f.write('This file is created just now.')
f.close()

# Appending content to the existing file
f = open("file_handeling/mytxtfile.txt",'a')
f.write('This is the content that is added to the existing file.')
f.close()

f = open("file_handeling/mytxtfile.txt",'r')
print(f.read())

import os
if os.path.exists("file_handeling/mytxtfile.txt"):
  os.remove("file_handeling/mytxtfile.txt")
else:
  print("The file does not exist")