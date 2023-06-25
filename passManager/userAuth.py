import sys
import csv
import os
import getpass
import passwordManager as pM



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
    pM.PasswordMan(dirPath,"",-m)
  
  def acceptNewUser(self):
   if(sys.argv[2] == "-w"):
     username=input("\nUsername:")
     try:
       self.userStore(pM.PasswordMan(dirPath,username , sys.argv[2]) , username)
     except:
       print("\nFile-Operation:(Failed)--->Permission:Denied")
       print("\nPlease refer command manual:")
       self.userStore(pM.PasswordMan(dirPath,username , "-m") , username)
   else:
    print("\nFile-Operation:(Failed)--->Permission:Denied")
    print("\nPlease refer command manual:")
    self.userStore(pM.PasswordMan(dirPath,username , "-m") , username)
  
  
  def userStore(self, passManObj, user):
   self.objUF.authInitialise(user , getpass.getpass(prompt="\nMaster-Key:"))
   if(passManObj.objP.isFileExist(userAuthPath)):
     self.objUF.write(userAuthPath)  
   else:
     self.objUF.erase(userAuthPath)
     self.objUF.write(userAuthPath)
   
  def retrieveOld(self):
   if(sys.argv[2] != "-d"):
    self.objUF.authInitialise(input("\nUsername:") , getpass.getpass(prompt = "\nMaster-Key:"))
    try:
       self.objUF.read(userAuthPath)
    except:
       print("\nFile-Search:(Failure)")
       print("\nError:File-Search-Incomplete")
       print("\nPlease refer command manual:")
       pM.PasswordMan(dirPath,"","-m")
   else:
    print("\nFile-Deletion:(Failed)--->Permission:Denied")
    print("\nPlease refer command manual:")
    pM.PasswordMan(dirPath,"","-m")

  def delUser(self):
   try:
     self.objUF.authInitialise(input("\nUsername:") , getpass.getpass(prompt = "\nMaster-Key:"))
     self.objUF.delFile(userAuthPath)
     self.objUF.delEntry(userAuthPath , userTempPath)
     self.objUF.delEntry(userTempPath , userAuthPath)
     pM.pathManager().remTempFile(userTempPath)
   except:
    print("\nFile-Deletion:(Failed)--->Permission:Denied")
    print("\nPlease refer command manual:")
    pM.PasswordMan(dirPath,"","-m")

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
          pM.PasswordMan(dirPath,row[self.fields[0]],sys.argv[2])
        except:
          pM.PasswordMan(dirPath,row[self.fields[0]],"-m")
  
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
          pM.PasswordMan(dirPath,row[self.fields[0]],sys.argv[1])
        except:
          pM.PasswordMan(dirPath,row[self.fields[0]],"-m")
        
  if(not flag):
   print("Master-Key:Mismatched--->Permission:Denied")
 
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
    pM.PasswordMan(dirPath,"","-m")