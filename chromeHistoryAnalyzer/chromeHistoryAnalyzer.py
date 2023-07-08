import sqlite3
import re
import shutil
import os
import sys
import urllib.parse
from datetime import datetime,timedelta
import matplotlib.pyplot as plot
import math




domainExtensions = ["com","org","net","us","edu"]
protocol = ["www","mail","account","in","chat"]
domainNames=["google","youtube","facebook","instagram","whatsapp"]

queryTitle = "'%%'" 

dayFactor = 365
numberOfYrs = int(input("\nYears:"))
tz = 9

dt_To = datetime.now()
dt_From = datetime.now()-timedelta(days=dayFactor*numberOfYrs)

browserPath = "C:\\Users\\SUBHANKAR\\AppData\\Local\Google\\Chrome\\User Data\\Default\\History"

directoryPath = "History_Analyzer"
tempPath = "\\chrome_historySS"
    
tempPath = directoryPath + tempPath

class Time:
 
  def __init__(self):
   return
  
  def dtToString(self,dt):
   return dt.strftime("%Y-%m-%d %H:%M:%S")

  def dateFromWebkit(self,webkit_timestamp, tz):
   epoch_start = datetime(1601,1,1)
   delta = timedelta(hours=tz,microseconds=int(webkit_timestamp))
   return epoch_start+delta

  def dateToWebkit(self,dt,tz):
   epoch_start = datetime(1601,1,1)
   delta = dt-epoch_start-timedelta(hours=tz)
   delta_micro_sec = (delta.days * 60 * 60 * 24 + delta.seconds) * 1000 * 1000
   return delta_micro_sec

  def timeRangeSet(self,dt_from,dt_to,tz):
   time_to = self.dateToWebkit(dt_to,tz)
   time_from = self.dateToWebkit(dt_from,tz)
   return time_from,time_to
    


class LinkParser:

  def __init__(self):
   return
  
  def baseURL(self,url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()  

class Query:
  
  def __init__(self):
   self.queryURL="'%%'"
   self.url={""}
   self.objT = Time()
   self.objL = LinkParser()
   return
  
  def sqlQuery(self,time_from,time_to,title,url):
   
    try:
       if os.stat(browserPath).st_mtime - os.stat(tempPath).st_mtime > 1:
         shutil.copy2(browserPath, tempPath)
    except FileNotFoundError:
         shutil.copy2(browserPath, tempPath)
   
    con=sqlite3.connect(tempPath)
    c=con.cursor()
   
    sql_string = f"""SELECT * FROM urls
                   where {time_from} < last_visit_time
                   AND title like {title}
                   AND url like {url}
                   ORDER BY last_visit_time DESC;"""
              
    c.execute(sql_string)
    fetch_result = c.fetchall()
    return fetch_result
  
  def fetchQuery(self):
    time_from,time_to = self.objT.timeRangeSet(dt_From,dt_To, tz)
    fetch_result = self.sqlQuery(time_from, time_to, queryTitle, self.queryURL)
  
    for i in fetch_result:
      self.url.add(self.objL.baseURL(i[1]))
      #print(self.url)
    
    return len(self.url),self.url
    

class Visualize:
 
 def __init(self):
  return
 
 def drawPieChart(self,dataset,labelSet,givenTitle):
  plot.pie(dataset, labels = labelSet, autopct = '%1.1f%%', radius = 2)
  plot.title("Chrome:History_Analyzer", pad = 32, loc = "left")
  plot.legend(title=givenTitle, loc='center left', bbox_to_anchor=(-0.1, .1))
  plot.axis('equal')
  plot.show()
  
class Statistics:
 
  def __init__(self):
   self.objQ = Query()
   self.objV = Visualize()
   return
  
  def staticQueryDetails(self):
   print(f"\nFrom: {self.objQ.objT.dtToString(dt_From)}, To: {self.objQ.objT.dtToString(dt_To)}")
   print(f"\nChrome_History_Analyzing....")
   
   
  def genDataDE(self):
   specific_result = []
   subDomainExtension = []
   __,url = self.objQ.fetchQuery() 
   print("\nUnique-Websites:\n")
   for i in domainExtensions:
     sum=0
     for j in url:
       if(re.findall(i+"$",j)):
         print(j)
         sum=sum+1
     if(sum != 0):
      specific_result.append(sum)
      subDomainExtension.append(i)
   self.objV.drawPieChart(specific_result,subDomainExtension,"domain_extensions:")

  def genDataDN(self):
   specific_result = []
   subDomainExtension = []
   __,url = self.objQ.fetchQuery() 
   print("\nUnique-Websites:\n")
   for i in domainNames:
     sum=0
     for j in url:
       if(re.findall(i,j)):
         print(j)
         sum=sum+1
     if(sum != 0):
      specific_result.append(sum)
      subDomainExtension.append(i)
   self.objV.drawPieChart(specific_result,subDomainExtension,"domain_names:")
  
  
  def genDataP(self):
   specific_result = []
   subDomainExtension = []
   __,url = self.objQ.fetchQuery()
   print("\nUnique-Websites:\n") 
   for i in protocol:
     sum=0
     for j in url:
       if(re.findall("https://"+i,j)):
         print(j)
         sum=sum+1
     if(sum != 0):
       specific_result.append(sum)
       subDomainExtension.append(i)
   self.objV.drawPieChart(specific_result,subDomainExtension,"protocol:")
  
  def manual(self):
   print("\nusage: [webHistoryReader.py] -[FLAGS]",", [FLAGS]: {-nam, -ext, -prt}")
   print("\nnam: Domain_Names","\next: Domain_Extension","\nprt: Protocols") 
   return
    

class pathManager:
  
  def __init__(self):
   return 
  
  def isDriveExist(self):
   global directoryPath
   if(os.path.exists("D:\\")):
     directoryPath = "D:\\" + directoryPath
   else:
     directoryPath = "B:\\" + directoryPath
   self.makeDirectory()
   
  def makeDirectory(self):
   global tempPath
   if(not os.path.exists(directoryPath)):
    os.mkdir(directoryPath)
   tempPath = directoryPath + "\\chrome_historySS"


def main():
 
  pathManager().isDriveExist()
  objS = Statistics()
  
  try:
   if(sys.argv[1]=="-ext"):
     objS.staticQueryDetails()
     objS.genDataDE()
   elif(sys.argv[1]=="-nam"):
     objS.staticQueryDetails()
     objS.genDataDN()
   elif(sys.argv[1]=="-prt"):
     objS.staticQueryDetails()
     objS.genDataP()
   else:
     objS.manual()
  except:
   objS.manual()

main() 