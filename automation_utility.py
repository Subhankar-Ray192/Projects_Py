import psutil
import subprocess

class Network:
 
 def __init__(self):
  return
 
 def status(self):
  result = subprocess.run("netsh interface show interface", capture_output = True, text = True)
  output = result.stdout.lower()
  print(output)
  if("wifi" in output and "connected" in output):
   return True
  elif("wifi" in output and "disconnected" in output):
   return False
  else:
   print("Status:Unknown")
 
 def enable(self):
  enable_run = subprocess.run("netsh interface set interface \"wi-fi\" enable", capture_output = True)
  print(enable_run.stdout)
  
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

def main():
  Network().status()
  #Network().enable()
  Network().nearbySpt()
  #Network().connect("\"Redmi Note 12 Pro 5G\"")
  Network().connectionInfo()
  #Network().disconnect()
  #Network().disable()
  Network().showP()

main()