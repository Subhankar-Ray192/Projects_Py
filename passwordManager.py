import sys
import csv
import os
from getpass import getpass


passkeep=["Website","Password","Level"]

class File:

 def __init__(self):
  self.objE=Encrypt()
  self.website={"Website":"","Password":"","Level":-1}
  self.updateWebsite={"Website":"","Password":"","Level":-1}


 def dictInitialise(self,web,pasw,lvl,ch):
  if(ch=="-w"):
   self.website[passkeep[0]]=web
  
   self.objE.lockText(pasw,lvl)
  
   self.website[passkeep[1]]=self.objE.psw
   self.website[passkeep[2]]=lvl
  elif(ch=="-u"):
   self.updateWebsite[passkeep[0]]=web
  
   self.objE.lockText(pasw,lvl)
  
   self.updateWebsite[passkeep[1]]=self.objE.psw
   self.updateWebsite[passkeep[2]]=lvl
  else:
   self.website[passkeep[0]]=web

 def read(self,filePath):
  with open(filePath,"r") as file:
    csvReader=csv.DictReader(file,fieldnames=passkeep)
    for row in csvReader:
      if(row[passkeep[0]]==self.website[passkeep[0]]):
        self.objE.psw=row[passkeep[1]]
        self.objE.unlockText(int(row[passkeep[2]]))

 def updateRecord(self,filePath):
  with open(filePath,"r") as file:
   csvReader=csv.DictReader(file,fieldnames=passkeep)
   for row in csvReader:
    if(row[passkeep[0]]==self.updateWebsite[passkeep[0]]):
      self.filterData(filePath,"D:\\tempFile.txt")
      self.website[passkeep[0]]=self.updateWebsite[passkeep[0]]
      self.website[passkeep[1]]=self.updateWebsite[passkeep[1]]
      self.website[passkeep[2]]=self.updateWebsite[passkeep[2]]
      self.write(filePath)
      
 
 def showWeb(self,filePath):
  with open(filePath,"r") as file:
   csvReader=csv.DictReader(file,fieldnames=passkeep)
   for row in csvReader:
     if(row[passkeep[0]]!=passkeep[0]):
       print(row[passkeep[0]],end="\n")

 def write(self,filePath):
  with open(filePath,"a",newline="",encoding="utf-8") as file:
    csvWriter=csv.DictWriter(file,fieldnames=passkeep)
    csvWriter.writerow(self.website) 
    
 def filterData(self,filePath,tempPath):
  pathManager().unHideFiles(filePath)
  self.delete(filePath,tempPath)
  self.delete(tempPath,filePath)
  pathManager().remTempFile(tempPath)
  pathManager().hideFile(filePath)
 
 def delete(self,filePath,tempPath):
  with open(filePath,"r") as file: 
   csvReader=csv.DictReader(file,fieldnames=passkeep)
   self.erase(tempPath)
   for row in csvReader:
    if((row[passkeep[0]]!=self.website[passkeep[0]])and(self.isHeader(row))):
     temp=self.website[passkeep[0]]

     self.website[passkeep[0]]=row[passkeep[0]]
     self.website[passkeep[1]]=row[passkeep[1]]
     self.website[passkeep[2]]=row[passkeep[2]]
     self.write(tempPath)
     
     self.website["Website"]=temp 
 
 def isHeader(self,row):
  if((row[passkeep[0]]==passkeep[0])or((row[passkeep[1]]==passkeep[1]))or((row[passkeep[2]]==passkeep[2]))):
   return False
  return True
 
 def erase(self,filePath):
  with open(filePath,"w",newline="",encoding="utf-8") as file:
    csvWriter=csv.DictWriter(file,fieldnames=passkeep)
    csvWriter.writeheader()
    #csvWriter.writerow({"Website":"Master","Password":"5322","Level":1})

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
  elif(choice.__eq__("-l")):
   self.listingWeb()
  elif(choice.__eq__("-u")):
   self.update()
  else:
   help()
  return

 def store(self):
  self.objF.dictInitialise(input("Website:"),getpass(),int(input("Level:")),"-w")
  self.objP.isFileExist(self.objF,"D:\\Password.txt")
  self.objP.hideFile("D:\\Password.txt")

 def view(self):
  self.objF.dictInitialise(input("Website:"),"",0,"-r")
  self.objF.read("D:\\Password.txt")
  self.objP.hideFile("D:\\Password.txt")
  return

 def remove(self):
  print(3)
  self.objF.dictInitialise(input("Website:"),"",0,"-f")
  self.objF.filterData("D:\\Password.txt","D:\\tempFile.txt")
  return

 def listingWeb(self):
  self.objF.showWeb("D:\\Password.txt")
  return 

 def update(self):
  self.objF.dictInitialise(input("Website:"),getpass(),int(input("Level:")),"-u")
  self.objF.updateRecord("D:\\Password.txt") 
  return
     
def main():
 print(sys.argv[1])
 PasswordMan(sys.argv[1])
   

main()