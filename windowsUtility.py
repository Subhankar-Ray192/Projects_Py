import psutil
import subprocess


scriptPath = "D:\Git_&_Github\Git\Projects_Py\windowsUtility.py"

battery = psutil.sensors_battery()
percentage = battery.percent

print(f"Battery Percentage: {percentage}%")

output = subprocess.check_output(["netsh","wlan","show","interface"])
output = output.decode("utf-8").replace("\r","").split("\n")
for i in output:
  #if("SSID".__eq__(i.split(":")[0].strip())):
   print(i)
#print(output)
 
def admin():
  
  username = input("\nUsername:")
  password = input("\nPassword:")
  
  cmd = ["runas","/user:"+username,"python"].append(scriptPath)
  
  subprocess.run(cmd, input = password.encode(), check=True, shell = True)

def enable():
  subprocess.run(["netsh","interface","set","interface","Wi-Fi","admin=enable"], capture_output = True)
  scan_output = subprocess.run(["netsh","wlan","show","networks"], capture_output = True, text = True)
  Networks = scan_output.stdout.split("\n")

  for i in Networks:
   if("SSID" in (i.split(":")[0].strip())):
     print(i.replace("SSID","Hotspot"))

  print(subprocess.run(["netsh","wlan","connect","name=\"Redmi Note 12 Pro 5G\"","ssid=\"Redmi Note 12 Pro 5G\""], capture_output = True))
  print(66) 

def disconnect():
  subprocess.run(["netsh","wlan","disconnect"],capture_output = True)
   
def disable():
  subprocess.run(["netsh","interface","set","interface","Wi-Fi","admin=disable"])

#disable()
enable()
print(55)
#disconnect()
#admin()