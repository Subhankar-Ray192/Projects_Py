import sys
import csv
import os
from getpass import getpass
from pathlib import Path


passkeep=["Website","Password","Level"]

dataFilePath="D:\\Password.txt"
garbageFilePath="D:\\TempFile.txt"


class CleanUtility:
  
  def __init__(self):
   self.objF=File()
   return
  
  def cleanEntry(self,filePath):
   with open(filePath,"r") as file:
    csvReader = csv.DictReader(file,fieldnames=passkeep)
    for rows in csvReader:
      if(rows[passkeep[0]]==""):
       self.objF.filterData(filePath,garbageFilePath)
   return


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
      self.filterData(filePath,garbageFilePath)
      self.website[passkeep[0]]=self.updateWebsite[passkeep[0]]
      self.website[passkeep[1]]=self.updateWebsite[passkeep[1]]
      self.website[passkeep[2]]=self.updateWebsite[passkeep[2]]
      self.write(filePath)
      
 
 def showWeb(self,filePath):
  print("\nWebsites:",end="")
  with open(filePath,"r") as file:
   csvReader=csv.DictReader(file,fieldnames=passkeep)
   for row in csvReader:
     if(row[passkeep[0]]!=passkeep[0]):
       print(row[passkeep[0]],end=",")

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
  self.pathS=dataFilePath
  return

 def pathChange():
  return
 
 def isFileExist(self,filePath):
  if (os.path.exists(filePath)):
       return True
  return False

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
  elif(choice.__eq__("-g")):
   self.clean()
  elif(choice.__eq__("-d")):
   self.deleteFile()
  else:
   self.manual()
  return

 def store(self):
  self.objF.dictInitialise(input("Website:"),getpass(),int(input("Level:")),"-w")
  if(self.objP.isFileExist(dataFilePath)):
       self.objF.write(dataFilePath)
       self.clean()
  else:
       self.objF.erase(dataFilePath)
       self.objF.write(dataFilePath)
       self.clean()
  self.objP.hideFile(dataFilePath)

 def view(self):
  if(self.objP.isFileExist(dataFilePath)):
      self.objF.dictInitialise(input("Website:"),"",0,"-r")
      self.objF.read(dataFilePath)
  else:
      print("\nFile-Read:(Failure)")
      print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return

 def remove(self):
  if(self.objP.isFileExist(dataFilePath)):
    self.objF.dictInitialise(input("Website:"),"",0,"-f")
    self.objF.filterData(dataFilePath,garbageFilePath)
  else:
    print("\nFile-Record-Deletion:(Failure)")
    print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return

 def listingWeb(self):
  if(self.objP.isFileExist(dataFilePath)):
    self.objF.showWeb(dataFilePath)
  else:
     print("\nFiles-Listing:(Failure)")
     print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return 

 def update(self):
  if(self.objP.isFileExist(dataFilePath)):
    self.objF.dictInitialise(input("Website:"),getpass(),int(input("Level:")),"-u")
    self.objF.updateRecord(dataFilePath) 
  else:
    print("\nFile-Update-Record:(Failure)")
    print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return

 def clean(self):
   if(self.objP.isFileExist(dataFilePath)):
     CleanUtility().cleanEntry(dataFilePath)
   else:
     print("\nFiles-Clean:(Failure)")
     print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
   return

 def deleteFile(self):
  if(self.objP.isFileExist(dataFilePath)):
   self.objP.unHideFiles(dataFilePath)
   self.objP.remTempFile(dataFilePath)
   print("\nFile-Delete:(Success)")
  else:
   print("\nFile-Delete:(Failure)")
   print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
 
 def manual(self):
  op=["Write ","Read  ","Erase ","Update","Delete","List  ","Help  "]
  opCode=["w","r","f","u","d","l","m"]
  print("\nusage: passwordManager.py -[FLAGS]")
  print("\nOperations:[FLAGS]\n")
  for i in range(7):
   print("File-{x}:-{y}".format(x=op[i],y=opCode[i]))
     
def main():
 try:
  PasswordMan(sys.argv[1])
 except:
  PasswordMan("-m")
   

main()