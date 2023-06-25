import sys
import csv
import os
from getpass import getpass


def isDriveExist(drive):
 for i in drive:
   if(os.path.exists(i+":\\")):
    print("\nDrive:Located-Successfully")
    return i
 print("\nError:Drive Not Found? Restart..")
 sys.exit(0)

drives=["B","D","E","F"]

selDrv=isDriveExist(drives)
dirPath = selDrv+":\\Password_Manager_Root\\"

userAuthPath = dirPath+"userAuth.txt"
userTempPath = dirPath+"userAuthTemp.txt"


directoryPath = "D:\\Password_Manager_Root"

garbageFilePath = directoryPath+"\\TempFile.txt"

class CleanUtility:
  
  def __init__(self , header):
   self.objF = File(header)
   return
  
  def cleanEntry(self , filePath):
   with open(filePath , "r") as file:
    csvReader = csv.DictReader(file , fieldnames = self.objF.fields)
    for rows in csvReader:
      if(rows[self.objF.fields[0]] == ""):
       self.objF.filterData(filePath , garbageFilePath)
   return

class File:

 def __init__(self,pmF):
  self.fields = pmF
  self.objE = Encrypt()
  self.website = {"Website": "" , "Password": "" , "Level": -1}
  self.updateWebsite = {"Website": "" , "Password": "" , "Level": -1}


 def dictInitialise(self , web , pasw , lvl , ch):
  if(ch == "-w"):
   self.website[self.fields[0]] = web
   self.objE.lockText(pasw , lvl)
   self.website[self.fields[1]] = self.objE.psw
   self.website[self.fields[2]] = lvl
  elif(ch == "-u"):
   self.updateWebsite[self.fields[0]] = web
   self.objE.lockText(pasw , lvl)
   self.updateWebsite[self.fields[1]] = self.objE.psw
   self.updateWebsite[self.fields[2]] = lvl
  else:
   self.website[self.fields[0]] = web

 def read(self , filePath):
  lvl = 0
  with open(filePath , "r") as file:
    csvReader = csv.DictReader(file , fieldnames = self.fields)
    for row in csvReader:
      if(row[self.fields[0]] == self.website[self.fields[0]]):
        self.objE.psw = row[self.fields[1]]
        lvl = int(row[self.fields[2]])
        break
    return lvl,self.objE

 def updateRecord(self , filePath):
  with open(filePath , "r") as file:
   csvReader=csv.DictReader(file , fieldnames = self.fields)
   for row in csvReader:
    if(row[self.fields[0]] == self.updateWebsite[self.fields[0]]):
      self.filterData(filePath , garbageFilePath)
      self.website[self.fields[0]] = self.updateWebsite[self.fields[0]]
      self.website[self.fields[1]] = self.updateWebsite[self.fields[1]]
      self.website[self.fields[2]] = self.updateWebsite[self.fields[2]]
      self.write(filePath)
      
 
 def showWeb(self , filePath):
  print("\nWebsites:" , end="")
  with open(filePath , "r") as file:
   csvReader = csv.DictReader(file , fieldnames = self.fields)
   for row in csvReader:
     if(row[self.fields[0]] != self.fields[0]):
       print(row[self.fields[0]] , end=",")
   print()

 def write(self , filePath):
  with open(filePath , "a",newline="" , encoding="utf-8") as file:
    csvWriter = csv.DictWriter(file , fieldnames = self.fields)
    csvWriter.writerow(self.website) 
 
 def search(self , filePath):
  with open(filePath , "r") as file:
    csvReader = csv.DictReader(file , fieldnames = self.fields)
    for row in csvReader:
     if((row[self.fields[0]] == self.website[self.fields[0]]) and (self.isHeader(row))):
      return True
  return False  

 def searchUpdate(self , filePath):
  with open(filePath , "r") as file:
    csvReader = csv.DictReader(file , fieldnames = self.fields)
    for row in csvReader:
     if((row[self.fields[0]] == self.updateWebsite[self.fields[0]]) and (self.isHeader(row))):
      return True
  return False 
    
 def filterData(self ,filePath , tempPath):
  pathManager().unHideFiles(filePath)
  self.delete(filePath , tempPath)
  self.delete(tempPath , filePath)
  pathManager().remTempFile(tempPath)
  pathManager().hideFile(filePath)
 
 def delete(self , filePath , tempPath):
  with open(filePath , "r") as file: 
   csvReader = csv.DictReader(file , fieldnames = self.fields)
   self.erase(tempPath)
   for row in csvReader:
    if((row[self.fields[0]] != self.website[self.fields[0]])and(self.isHeader(row))):
     temp = self.website[self.fields[0]]
     self.website[self.fields[0]] = row[self.fields[0]]
     self.website[self.fields[1]] = row[self.fields[1]]
     self.website[self.fields[2]] = row[self.fields[2]]
     self.write(tempPath)
     self.website[self.fields[0]] = temp 
 
 def isHeader(self , row):
  if((row[self.fields[0]] == self.fields[0])or((row[self.fields[1]] == self.fields[1]))or((row[self.fields[2]] == self.fields[2]))):
   return False
  return True
 
 def erase(self,filePath):
  with open(filePath , "w" , newline="" ,encoding="utf-8") as file:
    csvWriter = csv.DictWriter(file , fieldnames = self.fields)
    csvWriter.writeheader()

class Encrypt:

 def __init__(self):
  self.psw=""
 
 def lockText(self , u , key):
  for i in u:
    self.psw = self.psw + chr(ord(i) + key)

 def unlockText(self , key):
  print("Password:" , end="")
  for i in self.psw:
    print(chr(ord(i) - key) , end="")
  print()

class pathManager:
 
 def __init__(self):
  return 
 
 def dirCreator(self , filePath):
  if(not self.isFileExist(filePath)):
   os.mkdir(filePath)
 
 def isFileExist(self , filePath):
  if (os.path.exists(filePath)):
       return True
  return False

 def remTempFile(self , filePath):
  os.remove(filePath)
 
 def hideFile(self , filePath):
  p=os.system("attrib +h " + filePath)

 def unHideFiles(self , filePath):
  p=os.system("attrib -h " + filePath)
 
class PasswordMan:
 
 def __init__(self , dirPath,userName , choice):
  self.dataFilePath = dirPath + "\\" + userName + "Password.txt"
  self.header = ["Website" , "Password" , "Level"]
  self.objF = File(self.header)
  self.objP = pathManager()
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

 def store(self):
  self.objF.dictInitialise(input("\nWebsite:") , getpass() , (int(input("Level:")))%5 , "-w")
  if(self.objP.isFileExist(self.dataFilePath)):
       print(2)
       self.objF.write(self.dataFilePath)
       self.clean()
  else:
       self.objF.erase(self.dataFilePath)
       self.objF.write(self.dataFilePath)
       self.clean()
  self.objP.hideFile(self.dataFilePath)

 def view(self):
  if(self.objP.isFileExist(self.dataFilePath)):
      self.objF.dictInitialise(input("\nWebsite:") , "" , 0 , "-r")
      lvl,objE = self.objF.read(self.dataFilePath)
      objE.unlockText(lvl)
  else:
      print("\nFile-Read:(Failure)")
      print("\nError:File-Not-Found" , "\nPlease check the file-path and try again!")

 def remove(self):
  self.objF.dictInitialise(input("\nWebsite:") , "" , 0 , "-f")
  if((self.objP.isFileExist(self.dataFilePath)) and (self.objF.search(self.dataFilePath))):
    self.objF.filterData(self.dataFilePath , garbageFilePath)
    print("\nFile-Record-Deletion:(Success)")
  else:
    print("\nFile-Record-Deletion:(Failure)")
    print("\nError:File-Not-Found")

 def listingWeb(self):
  if(self.objP.isFileExist(self.dataFilePath)):
    self.objF.showWeb(self.dataFilePath)
  else:
     print("\nFiles-Listing:(Failure)")
     print("\nError:File-Not-Found" , "\nPlease check the file-path & try again!")

 def update(self):
  self.objF.dictInitialise(input("\nWebsite:") , getpass() , (int(input("Level:")))%5 , "-u")
  if((self.objP.isFileExist(self.dataFilePath)) and (self.objF.searchUpdate(self.dataFilePath))):
    self.objF.updateRecord(self.dataFilePath) 
  else:
    print("\nFile-Update-Record:(Failure)")
    print("\nError:File-Not-Found")

 def clean(self):
   if(self.objP.isFileExist(self.dataFilePath)):
     CleanUtility(self.header).cleanEntry(self.dataFilePath)
   else:
     print("\nFiles-Clean:(Failure)")
     print("\nError:File-Not-Found" , "\nPlease check the file-path & try again!")

 def deleteFile(self):
  if(self.objP.isFileExist(self.dataFilePath)):
   self.objP.unHideFiles(self.dataFilePath)
   self.objP.remTempFile(self.dataFilePath)
   print("\nFile-Delete:(Success)")
  else:
   print("\nFile-Delete:(Failure)")
   print("\nError:File-Not-Found" , "\nPlease check the file-path & try again!")
 
 def manual(self):
  user_acc = ["New-User     ","Existing-User","Delete-User  "]
  user_accCode = ["n  -[w]","ru -[w | r | f | u | l | m]","d  -[None]"]
  
  op = ["Write ","Read  ","Erase ","Update","List  ","Help  "]
  opCode = ["w","r","f","u","l","m"]
  
  print("\nUsage: userAuth.py -[TYPE] -[FLAGS]")
  
  print("\nUser-Type:[Type]\n")
  for i in range(3):
   print("{x}:-{y}".format(x = user_acc[i],y = user_accCode[i]))
  
  print("\nManager-Operations:[FLAGS]\n")  
  for i in range(6):
   print("Record-{x}:-{y}".format(x = op[i],y = opCode[i]))
  

class UserAuth:
  
  def __init__(self,choice):
   self.header = ["Username","MasterKey"]
   self.objUF = UserFile(self.header)
   if(choice.__eq__("-n")):
    self.acceptNewUser()
   elif(choice.__eq__("-ru")):
    self.retrieveOld()
   elif(choice.__eq__("-d")):
    self.delUser()
   else:
    PasswordMan(dirPath,"","-m")
  
  def acceptNewUser(self):
   if(sys.argv[2] == "-w"):
     username=input("\nUsername:")
     try:
      self.userStore(PasswordMan(dirPath,username , sys.argv[2]) , username)
     except:
      print("\nFile-Operation:(Failed)--->Permission:Denied")
      print("\nPlease refer command manual:")
      self.userStore(PasswordMan(dirPath,username , "-m") , username)
   else:
    print("\nFile-Operation:(Failed)--->Permission:Denied")
    print("\nPlease refer command manual:")
    PasswordMan(dirPath, "" , "-m")
  
  
  def userStore(self, passManObj, user):
   self.objUF.authInitialise(user , getpass(prompt="\nMaster-Key:"))
   if(passManObj.objP.isFileExist(userAuthPath)):
     self.objUF.write(userAuthPath)  
   else:
     self.objUF.erase(userAuthPath)
     self.objUF.write(userAuthPath)
   
  def retrieveOld(self):
   try: 
    if(sys.argv[2] != "-d"):
     self.objUF.authInitialise(input("\nUsername:") , getpass(prompt = "\nMaster-Key:"))
     try:  
       self.objUF.read(userAuthPath)
     except:
       print("\nFile-Search:(Failure)")
       print("\nError:File-Search-Incomplete")
       print("\nPlease refer command manual:")
       PasswordMan(dirPath,"","-m")
    else:
      print("\nFile-Deletion:(Failed)--->Permission:Denied")
      print("\nPlease refer command manual:")
      PasswordMan(dirPath,"","-m")
   except:
       print("\nFile-Search:(Failure)")
       print("\nError:File-Search-Incomplete")
       print("\nPlease refer command manual:")
       PasswordMan(dirPath,"","-m")     

  def delUser(self):
   try:
     self.objUF.authInitialise(input("\nUsername:") , getpass(prompt = "\nMaster-Key:"))
     if(self.objUF.delFile(userAuthPath)):
       self.objUF.delEntry(userAuthPath , userTempPath)
       self.objUF.delEntry(userTempPath , userAuthPath)
       pathManager().remTempFile(userTempPath)
     else:
       print("\nFile-Deletion:(Failed)--->Permission:Denied")
       print("\nPlease check:(Username) , (Master-Key)\nPlease refer command manual:")
       PasswordMan(dirPath,"","-m")
   except:
    print("\nFile-Deletion:(Failed)--->Permission:Denied")
    print("\nPlease refer command manual:")
    PasswordMan(dirPath,"","-m")

class UserFile:
  
 def __init__(self , pmF):
  self.fields = pmF
  self.userAuthName = {"Username":"","MasterKey":""}
  self.updateuserAuthName = {"Username":"","MasterKey":""}


 def authInitialise(self , un , mkey):
   self.userAuthName[self.fields[0]] = un
   self.userAuthName[self.fields[1]] = mkey

 def read(self , filePath):
  flag = 0
  with open(filePath,"r") as file:
    csvReader = csv.DictReader(file,fieldnames = self.fields)
    for row in csvReader:
      if((row[self.fields[1]] == self.userAuthName[self.fields[1]])and(row[self.fields[0]] == self.userAuthName[self.fields[0]])): 
        flag = 1
        print("Master-Key:Matched--->Permission:Granted")
        try:
          PasswordMan(dirPath,row[self.fields[0]],sys.argv[2])
        except:
          PasswordMan(dirPath,row[self.fields[0]],"-m")
  
  if(not flag):
   print("Master-Key:Mismatched--->Permission:Denied")
 
 
 def delEntry(self , filePath , tempPath):
  with open(filePath,"r") as file: 
    csvReader = csv.DictReader(file,fieldnames = self.fields)
    self.erase(tempPath)
    for row in csvReader:
     if((row[self.fields[0]] != self.userAuthName[self.fields[0]])and(self.isHeader(row))):
      temp = self.userAuthName[self.fields[0]]
      self.userAuthName[self.fields[0]] = row[self.fields[0]]
      self.userAuthName[self.fields[1]] = row[self.fields[1]]
      self.write(tempPath)
      self.userAuthName[self.fields[0]] = temp 
 
 def delFile(self , filePath):
  flag = 0
  with open(filePath,"r") as file:
    csvReader = csv.DictReader(file,fieldnames = self.fields)
    for row in csvReader:
      if((row[self.fields[1]] == self.userAuthName[self.fields[1]])and(row[self.fields[0]] == self.userAuthName[self.fields[0]])): 
        flag = 1
        print("Master-Key:Matched--->Permission:Granted") 
        try:
          PasswordMan(dirPath,row[self.fields[0]],sys.argv[1])
        except:
          PasswordMan(dirPath,row[self.fields[0]],"-m")
        
  if(not flag):
   print("Master-Key:Mismatched--->Permission:Denied")
  return flag
  
 
 def write(self , filePath):
  with open(filePath,"a",newline = "",encoding = "utf-8") as file:
    csvWriter = csv.DictWriter(file,fieldnames = self.fields)
    csvWriter.writerow(self.userAuthName) 
 
 def isHeader(self , row):
  if((row[self.fields[0]] == self.fields[0])or((row[self.fields[1]] == self.fields[1]))):
   return False
  return True
 
 def erase(self , filePath):
  with open(filePath,"w",newline = "",encoding = "utf-8") as file:
    csvWriter = csv.DictWriter(file,fieldnames = self.fields)
    csvWriter.writeheader()

if __name__=="__main__":
   try:
     UserAuth(sys.argv[1])
   except:
     PasswordMan(dirPath,"","-m")


