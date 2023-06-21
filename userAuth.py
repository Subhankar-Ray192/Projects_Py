import sys
import csv
import os
from getpass import getpass
import passwordManager as pM


userAuthPath="D:\\Password_Manager_Root\\userAuth.txt"

class UserAuth:
  
  def __init__(self,choice):
   self.header=["Username","MasterKey"]
   self.objUF=UserFile(self.header)
   if(choice.__eq__("-n")):
    self.acceptNewUser()
   return

  def acceptNewUser(self):
   if(sys.argv[3]=="-w"):
     x=pM.PasswordMan(sys.argv[2],sys.argv[3])
     self.userStore(x)
  
  def userStore(self,x):
   self.objUF.authInitialise(sys.argv[2],getpass(prompt="Master-Key:"),sys.argv[1])
   if(x.objP.isFileExist(userAuthPath)):
     self.objUF.write(userAuthPath)  
   else:
     self.objUF.erase(userAuthPath)
     self.objUF.write(userAuthPath)

class UserFile:
  
 def __init__(self,pmF):
  self.fields=pmF
  self.userAuthName={"Username":"","MasterKey":""}
  self.updateuserAuthName={"Username":"","MasterKey":""}


 def authInitialise(self,un,mkey,ch):
  if(ch=="-n"):
   self.userAuthName[self.fields[0]]=un
   self.userAuthName[self.fields[1]]=mkey
  else:
   print("xx")

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
    csvWriter.writerow(self.userAuthName) 
    
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

def main():
 UserAuth(sys.argv[1])

main()