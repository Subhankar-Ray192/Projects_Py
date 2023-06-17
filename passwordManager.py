import sys
import csv
import os
from getpass import getpass


passkeep=["Website","Password","Level"]

class File:

 def __init__(self):
  self.objE=Encrypt()
  self.website={"Website":"","Password":"","Level":-1}


 def dictInitialise(self,web,pasw,lvl,ch):
  if(ch=="-w"):
   self.website["Website"]=web
  
   self.objE.lockText(pasw,lvl)
  
   self.website["Password"]=self.objE.psw
   self.website["Level"]=lvl
  elif(ch=="-r"):
   self.website["Website"]=web
  else:
   self.website["Website"]=web

 def read(self,filePath):
  with open(filePath,"r") as file:
    csvReader=csv.DictReader(file,fieldnames=passkeep)
    for row in csvReader:
      if(row["Website"]==self.website["Website"]):
        self.objE.psw=row["Password"]
        self.objE.unlockText(int(row["Level"]))
    return

 def write(self,filePath):
  with open(filePath,"a") as file:
    csvWriter=csv.DictWriter(file,fieldnames=passkeep)
    csvWriter.writerow(self.website) 
    
 def filterData(self,obj,filePath,tempPath):
  pathManager().unHideFiles(filePath)
  obj.delete(filePath,tempPath)
  obj.delete(tempPath,filePath)
  pathManager().remTempFile(tempPath)
  pathManager().hideFile(filePath)
 
 def delete(self,filePath,tempPath):
  with open(filePath,"r") as file: 
   csvReader=csv.DictReader(file,fieldnames=passkeep)
   for row in csvReader:
    self.erase(tempPath)
    if(row["Website"]!=self.website["Website"]):
     temp=self.website["Website"]

     self.website["Website"]=row["Website"]
     self.website["Password"]=row["Password"]
     self.website["Level"]=row["Level"]
     self.write(tempPath)
     
     self.website["Website"]=temp 
 
 def erase(self,filePath):
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

 def unlockText(self,key):
  print("Password:",end="")
  for i in self.psw:
    print(chr(ord(i)-key),end="")
  print()

class pathManager:
 
 def __init__(self):
  return

 def isFileExist(self,obj,filePath):
  if (not os.path.exists(filePath)):
            obj.erase(filePath)
            obj.write(filePath)
  else:
            obj.write(filePath)

 def remTempFile(self,filePath):
  os.remove(filePath)
  return

 def hideFile(self,filePath):
  p=os.system("attrib +h "+filePath)
  return

 def unHideFiles(self,filePath):
  p=os.system("attrib -h "+filePath)
  return
 
class PasswordMan:
 
 def __init__(self,choice):
  self.objF=File()
  self.objP=pathManager()
  if(choice.__eq__("-w")):
   self.store()
  elif(choice.__eq__("-r")):
   self.view()
  elif(choice.__eq__("-f")):
   self.remove()
  else:
   help()
  return

 def store(self):
  print(1)
  self.objF.dictInitialise(input("Website:"),getpass(),int(input("Level:")),"-w")
  self.objP.isFileExist(self.objF,"D:\\Password.txt")
  self.objP.hideFile("D:\\Password.txt")

 def view(self):
  print(2)
  self.objF.dictInitialise(input("Website:"),"",0,"-r")
  self.objF.read("D:\\Password.txt")
  self.objP.hideFile("D:\\Password.txt")
  return

 def remove(self):
  print(3)
  self.objF.dictInitialise(input("Website:"),"",0,"-f")
  self.objF.filterData(self.objF,"D:\\Password.txt","D:\\tempFile.txt")
  return  
     
def main():
 print(sys.argv[1])
 PasswordMan(sys.argv[1])
   

main()