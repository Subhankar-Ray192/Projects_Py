import sys
import csv
import os
from getpass import getpass

filePath="D:\\Password.txt"
passkeep=["Website","Password","Level"]

class File:

 def __init__(self,web,pasw,lvl):
  self.objE=Encrypt()
  self.website={"Website":"","Password":"","Level":-1}
  self.website["Website"]=web
  
  self.objE.lockText(pasw,lvl)
  
  self.website["Password"]=self.objE.psw
  self.website["Level"]=lvl
  print(self.website)

 def read(self):
  return;

 def write(self):
  with open(filePath,"a") as file:
    csvWriter=csv.DictWriter(file,fieldnames=passkeep)
    csvWriter.writerow(self.website) 
    
 
 def erase(self):
  with open(filePath,"w") as file:
    csvWriter=csv.DictWriter(file,fieldnames=passkeep)
    csvWriter.writeheader()
    csvWriter.writerow({"Website":"Master","Password":"5322","Level":1})

class Encrypt:

 def __init__(self):
  self.psw=""
 
 def lockText(self,u,key):
  for i in u:
    self.psw=self.psw+chr(ord(i)+key)
  print("LT",self.psw,end="\n")

 def unlockText(self,key):
  print("Display:",end="")
  for i in self.psw:
    print(chr(ord(i)-key),end="")
  print()

class pathManager:
 
 def __init__(self):
  return

 def isFileExist(self,obj):
  if (not os.path.exists(filePath)):
            obj.erase()
            obj.write()
  else:
            obj.write()
  
def main():
 obj=File(input("Website:"),getpass(),int(input("Level:")))
 pathManager().isFileExist(obj)

main()