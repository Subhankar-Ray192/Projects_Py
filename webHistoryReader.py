import sqlite3
import shutil
import os
import sys
import urllib.parse
from datetime import datetime, timedelta


query_title="'%%'"
query_url="'%www.%'"

dt_to = datetime.now()
dt_from= datetime.now()-timedelta(days=365*12)

tz=9

history_file_original="C:\\Users\\SUBHANKAR\\AppData\\Local\Google\\Chrome\\User Data\\Default\\History"
history_file_tmp = "D:\\chromrHistory_SS"

def dtToString(dt):
  return dt.strftime("%Y-%m-%d %H:%M:%S")

def dateFromWebkit(webkit_timestamp, tz):
  epoch_start = datetime(1601,1,1)
  delta = timedelta(hours=tz,microseconds=int(webkit_timestamp))
  return epoch_start+delta

def dateToWebkit(dt,tz):
  epoch_start = datetime(1601,1,1)
  delta = dt-epoch_start-timedelta(hours=tz)
  delta_micro_sec = (delta.days * 60 * 60 * 24 + delta.seconds) * 1000 * 1000
  return delta_micro_sec

def timeRangeSet(dt_from,dt_to,tz):
  time_to = dateToWebkit(dt_to,tz)
  time_from = dateToWebkit(dt_from,tz)
  return time_from,time_to

def sqlQuery(time_from,time_to,title,url):
  
  try:
      if os.stat(history_file_original).st_mtime - os.stat(history_file_tmp).st_mtime > 1:
        shutil.copy2(history_file_original, history_file_tmp)
  except FileNotFoundError:
       shutil.copy2(history_file_original,history_file_tmp)

  con=sqlite3.connect(history_file_tmp)
  c=con.cursor()

  sql_string = f"""SELECT * FROM urls
                   where {time_from} < last_visit_time
                   AND title like {title}
                   AND url like {url}
                   ORDER BY last_visit_time DESC;"""
              
  c.execute(sql_string)
  fetch_result = c.fetchall()
  return fetch_result

def base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()

if __name__=="__main__":
  
  print(f"Query chrome history")
  print(f"From: {dtToString(dt_from)}, To: {dtToString(dt_to)}")
  print(f"Title {query_title}")
  print(f"Url {query_url}")
  
  time_from,time_to = timeRangeSet(dt_from,dt_to, tz)
  fetch_result = sqlQuery(time_from, time_to, query_title, query_url)

  print(f"{len(fetch_result)} results...")
  


  for i in fetch_result:
    time=i[5]
    url=base_url(i[1])
    visited=[i[3]]
    title=i[2]
    
    dt=dateFromWebkit(time,tz)
    time_str=dtToString(dt)

    max_len = 10
    
    if len(title) > max_len:
     title = title[:max_len]+"..."
    
    print(url,visited)
  