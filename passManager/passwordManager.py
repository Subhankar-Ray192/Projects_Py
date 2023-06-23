import sys
import csv
import os
from getpass import getpass




directoryPath="D:\\Password_Manager_Root"

garbageFilePath=directoryPath+"\\TempFile.txt"


class CleanUtility:
  
  def __init__(self,header):
   self.objF=File(header)
   return
  
  def cleanEntry(self,filePath):
   with open(filePath,"r") as file:
    csvReader = csv.DictReader(file,fieldnames=self.objF.fields)
    for rows in csvReader:
      if(rows[self.objF.fields[0]]==""):
       self.objF.filterData(filePath,garbageFilePath)
   return

  def cleanDir(self):
   return


class File:

 def __init__(self,pmF):
  self.fields=pmF
  self.objE=Encrypt()
  self.website={"Website":"","Password":"","Level":-1}
  self.updateWebsite={"Website":"","Password":"","Level":-1}


 def dictInitialise(self,web,pasw,lvl,ch):
  if(ch=="-w"):
   self.website[self.fields[0]]=web
  
   self.objE.lockText(pasw,lvl)
  
   self.website[self.fields[1]]=self.objE.psw
   self.website[self.fields[2]]=lvl
  elif(ch=="-u"):
   self.updateWebsite[self.fields[0]]=web
  
   self.objE.lockText(pasw,lvl)
  
   self.updateWebsite[self.fields[1]]=self.objE.psw
   self.updateWebsite[self.fields[2]]=lvl
  else:
   self.website[self.fields[0]]=web

 def read(self,filePath):
  lvl=0
  with open(filePath,"r") as file:
    csvReader=csv.DictReader(file,fieldnames=self.fields)
    for row in csvReader:
      if(row[self.fields[0]]==self.website[self.fields[0]]):
        self.objE.psw=row[self.fields[1]]
        lvl=int(row[self.fields[2]])
        break
    return lvl,self.objE

 def updateRecord(self,filePath):
  with open(filePath,"r") as file:
   csvReader=csv.DictReader(file,fieldnames=self.fields)
   for row in csvReader:
    if(row[self.fields[0]]==self.updateWebsite[self.fields[0]]):
      self.filterData(filePath,garbageFilePath)
      self.website[self.fields[0]]=self.updateWebsite[self.fields[0]]
      self.website[self.fields[1]]=self.updateWebsite[self.fields[1]]
      self.website[self.fields[2]]=self.updateWebsite[self.fields[2]]
      self.write(filePath)
      
 
 def showWeb(self,filePath):
  print("\nWebsites:",end="")
  with open(filePath,"r") as file:
   csvReader=csv.DictReader(file,fieldnames=self.fields)
   for row in csvReader:
     if(row[self.fields[0]]!=self.fields[0]):
       print(row[self.fields[0]],end=",")
   print()

 def write(self,filePath):
  with open(filePath,"a",newline="",encoding="utf-8") as file:
    csvWriter=csv.DictWriter(file,fieldnames=self.fields)
    csvWriter.writerow(self.website) 
    
 def filterData(self,filePath,tempPath):
  pathManager().unHideFiles(filePath)
  self.delete(filePath,tempPath)
  self.delete(tempPath,filePath)
  pathManager().remTempFile(tempPath)
  pathManager().hideFile(filePath)
 
 def delete(self,filePath,tempPath):
  with open(filePath,"r") as file: 
   csvReader=csv.DictReader(file,fieldnames=self.fields)
   self.erase(tempPath)
   for row in csvReader:
    if((row[self.fields[0]]!=self.website[self.fields[0]])and(self.isHeader(row))):
     temp=self.website[self.fields[0]]

     self.website[self.fields[0]]=row[self.fields[0]]
     self.website[self.fields[1]]=row[self.fields[1]]
     self.website[self.fields[2]]=row[self.fields[2]]
     self.write(tempPath)
     
     self.website[self.fields[0]]=temp 
 
 def isHeader(self,row):
  if((row[self.fields[0]]==self.fields[0])or((row[self.fields[1]]==self.fields[1]))or((row[self.fields[2]]==self.fields[2]))):
   return False
  return True
 
 def erase(self,filePath):
  with open(filePath,"w",newline="",encoding="utf-8") as file:
    csvWriter=csv.DictWriter(file,fieldnames=self.fields)
    csvWriter.writeheader()

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
  #self.pathS=dataFilePath
  return

 def pathChange():
  return
 
 def dirCreator(self,filePath):
  if(not self.isFileExist(filePath)):
   os.mkdir(filePath)
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
 
 def __init__(self,userName,choice):
  self.dataFilePath=directoryPath+"\\"+userName+"Password.txt"
  self.header=["Website","Password","Level"]
  self.objF=File(self.header)
  self.objP=pathManager()
  self.objP.dirCreator(directoryPath)
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
  self.objF.dictInitialise(input("\nWebsite:"),getpass(),(int(input("Level:")))%5,"-w")
  if(self.objP.isFileExist(self.dataFilePath)):
       self.objF.write(self.dataFilePath)
       self.clean()
  else:
       self.objF.erase(self.dataFilePath)
       self.objF.write(self.dataFilePath)
       self.clean()
  self.objP.hideFile(self.dataFilePath)

 def view(self):
  if(self.objP.isFileExist(self.dataFilePath)):
      self.objF.dictInitialise(input("\nWebsite:"),"",0,"-r")
      lvl,objE=self.objF.read(self.dataFilePath)
      objE.unlockText(lvl)
  else:
      print("\nFile-Read:(Failure)")
      print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return

 def remove(self):
  if(self.objP.isFileExist(self.dataFilePath)):
    self.objF.dictInitialise(input("\nWebsite:"),"",0,"-f")
    self.objF.filterData(self.dataFilePath,garbageFilePath)
  else:
    print("\nFile-Record-Deletion:(Failure)")
    print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return

 def listingWeb(self):
  if(self.objP.isFileExist(self.dataFilePath)):
    self.objF.showWeb(self.dataFilePath)
  else:
     print("\nFiles-Listing:(Failure)")
     print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return 

 def update(self):
  if(self.objP.isFileExist(self.dataFilePath)):
    self.objF.dictInitialise(input("\nWebsite:"),getpass(),(int(input("Level:")))%5,"-u")
    self.objF.updateRecord(self.dataFilePath) 
  else:
    print("\nFile-Update-Record:(Failure)")
    print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
  return

 def clean(self):
   if(self.objP.isFileExist(self.dataFilePath)):
     CleanUtility(self.header).cleanEntry(self.dataFilePath)
   else:
     print("\nFiles-Clean:(Failure)")
     print("\nError:File-Not-Found","\nPlease check the file-path & try again!")
   return

 def deleteFile(self):
  if(self.objP.isFileExist(self.dataFilePath)):
   self.objP.unHideFiles(self.dataFilePath)
   self.objP.remTempFile(self.dataFilePath)
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

