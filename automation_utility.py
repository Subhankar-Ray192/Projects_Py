import psutil
import subprocess

class Network:
 
 def __init__(self):
  self.wifi_row = ""
  self.findcomponentInfo()
  return
 
 def findcomponentInfo(self):
  result = subprocess.run("netsh interface show interface", capture_output = True, text = True)
  state = result.stdout.lower()
  lines = state.splitlines()
  
  for line in lines:
   if ("wi-fi" in line):
    self.wifi_row = line
    break
 
 def showStatus(self):
  print(self.wifi_row)
  
 def isEnable(self):
  if ("enabled".__eq__(self.wifi_row.split()[0])):
   return 1
  return 0

 def isConnect(self):
  if ("connected".__eq__(self.wifi_row.split()[1])):
   return 1
  return 0 
  
 def enable(self):
  enable_run = subprocess.run("netsh interface set interface \"wi-fi\" enable", capture_output = True)
  #print(enable_run.stdout)
  
 def nearbySpt(self):
   scan_output =  subprocess.run(["netsh","wlan","show","network"], capture_output = True, text = True)
   networks = scan_output.stdout.split("\n")
   
   print("\nNear-By-Networks")
   for i in networks:
    if("SSID" in i.split(":")[0]):
     print(i.replace("SSID","Hotspots"))

 def connect(self,ssid):
   com = "netsh wlan connect name="+ ssid + " interface=\"wi-fi\""
   connect_result = subprocess.run(com, capture_output = True)
   print("\n",connect_result.stdout.decode("utf-8").replace("\r\n","").replace("'",""))
 
 def disable(self):
  subprocess.run(["netsh","interface","set","interface","Wi-Fi","admin=disable"])

 def connectionInfo(self):
  output = subprocess.check_output(["netsh","wlan","show","interface"])
  output = output.decode("utf-8").replace("\r","").split("\n")
  for i in output:
   print(i)

 def disconnect(self):
  subprocess.run(["netsh","wlan","disconnect"],capture_output = True)

 def showP(self):
  result = subprocess.run("netsh wlan show profiles", capture_output = True)
  profiles = result.stdout.decode("utf-8").replace("\r","").split("\n")
  
  for i in profiles:
   print(i)
 
 def connectionModule(self, choice):
  status_flag = int(str(Network().isEnable()) + str(Network().isConnect()),2)
  if((status_flag == 2) and (choice.__eq__("-de"))):
   self.disable()
   print("Disable:Successful")
  elif((status_flag == 2) and (choice.__eq__("-c"))):
   self.nearbySpt()
   self.showP()
   self.connect("\"Redmi Note 12 Pro 5G\"")
  elif((status_flag == 0) and (choice.__eq__("-e"))):
   self.enable()
   print("\nEnable:Successful")
  elif((status_flag == 3) and (choice.__eq__("-dc"))):
   self.disconnect()
  elif(choice.__eq__("-s")):
   self.findcomponentInfo()
   self.showStatus()
  elif((status_flag == 3) and (choice.__eq__("-ci"))):
   self.connectionInfo()
  elif(choice.__eq__("-n")):
   self.nearbySpt()
  elif(choice.__eq__("-p")):
   self.showP()
  
 def flagAccpt(self,x):
   for i in x:
    self.connectionModule(i)

def main():
  Network().flagAccpt(["-c"])
  #Network().nearbySpt()
  #Network().connect()
  #Network().disconnect()
  #Network().showP()

main()