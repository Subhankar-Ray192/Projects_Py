import sys
import csv
import os
import getpass
import passwordManager as pM

dirPath="D:\\Password_Manager_Root\\"
userAuthPath=dirPath+"userAuth.txt"

class UserAuth:
  
  def __init__(self,choice):
   self.header=["Username","MasterKey"]
   self.objUF=UserFile(self.header)
   if(choice.__eq__("-n")):
    self.acceptNewUser()
   elif(choice.__eq__("-ru")):
    self.retrieveOld()
   else:
    x.pM.PasswordMan()
   return
  
  def acceptNewUser(self):
   if(sys.argv[3]=="-w"):
     username=input("\nUsername:")
     try:
       self.userStore(pM.PasswordMan(username,sys.argv[2]),sys.argv[2],username)
     except:
       self.userStore(pM.PasswordMan(username,"-m"),sys.argv[2],username)
  
  def userStore(self,x,user):
   self.objUF.authInitialise(user,getpass.getpass(prompt="\nMaster-Key:"),sys.argv[1])
   if(x.objP.isFileExist(userAuthPath)):
     self.objUF.write(userAuthPath)  
   else:
     self.objUF.erase(userAuthPath)
     self.objUF.write(userAuthPath)
   
  def retrieveOld(self):
    self.objUF.authInitialise(input("\nUsername:"),getpass.getpass(prompt="\nMaster-Key:"),sys.argv[1])
    self.objUF.read(userAuthPath)
    return  
     
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
   self.userAuthName[self.fields[0]]=un
   self.userAuthName[self.fields[1]]=mkey
   
  return

 def read(self,filePath):
  flag=0
  with open(filePath,"r") as file:
    csvReader=csv.DictReader(file,fieldnames=self.fields)
    for row in csvReader:
      if((row[self.fields[1]]==self.userAuthName[self.fields[1]])and(row[self.fields[0]]==self.userAuthName[self.fields[0]])): 
        print("Master-Key:Matched--->Permission:Granted")
        try:
          pM.PasswordMan(row[self.fields[0]],sys.argv[2])
        except:
          pM.PasswordMan(row[self.fields[0]],"-m")
        flag=1
  if(not flag):
   print("Master-Key:Mismatched--->Permission:Denied")
  return

 def write(self,filePath):
  with open(filePath,"a",newline="",encoding="utf-8") as file:
    csvWriter=csv.DictWriter(file,fieldnames=self.fields)
    csvWriter.writerow(self.userAuthName) 
 
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