import sqlite3
import shutil
import os
import os
import sys
import urllib.parse
from datetime import datetime,timedelta
import matplotlib.pyplot as plot



domainExtensions = ["com","org",""]
queryTitle = "'%%'" 

dayFactor = 365
tz = 9

dt_To = datetime.now()
dt_From = datetime.now()-timedelta(days=dayFactor*12)

browserPath = "C:\\Users\\SUBHANKAR\\AppData\\Local\Google\\Chrome\\User Data\\Default\\History"
tempPath = "D:\\chromrHistory_SS"



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
  
  def base_url(self,url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()  

class Query:
  
  def __init__(self):
   self.queryUrl = []
   self.objT = Time()
   self.objL = LinkParser()
   return
  
  def assignQuery(self,webList):
   for i in webList:
     self.queryUrl.append("'%{}%'".format(i))
  
  def clearQuery(self):
   for i in range(len(self.queryUrl)):
     self.queryUrl.pop()
  
  def showQuery(self):
   for i in self.queryUrl:
     print(i)
  
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
  
  def fetchQuery(self,index):
    time_from,time_to = self.objT.timeRangeSet(dt_From,dt_To, tz)
    fetch_result = self.sqlQuery(time_from, time_to, queryTitle, self.queryUrl[index])
  
    #print(f"{len(fetch_result)} results...")
    return len(fetch_result)
    
 

def main():
 objQ=Query()
 objQ.assignQuery(domainExtensions)
 objQ.showQuery()
 print(f"Query chrome history")
 print(f"From: {objQ.objT.dtToString(dt_From)}, To: {objQ.objT.dtToString(dt_To)}")
 print(f"Title {queryTitle}")
 print(f"Url {domainExtensions[0]}")

 total_result=objQ.fetchQuery(2)

 specific_result=objQ.fetchQuery(0)

 percent=(specific_result/total_result)*100

 print("Percent:{0:.2f}%".format(percent))
 
 k=[20,30,50]
 plot.pie(k, labels = domainExtensions)
 plot.legend(title = "domain_extensions:")
 plot.show()
 
main() 