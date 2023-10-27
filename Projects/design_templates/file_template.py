import csv
import os
import sys


class File: 
    class Create:
        def __init__(self,header,path,dataset):
            self.meta_data = header
            self.path = path
            self.data_store = {}
            self.insertKey()
            self.insertVal(dataset)

        def write1(self):
            with open(self.path,"w") as file:
                csvWriter = csv.DictWriter(file,fieldnames = self.meta_data)
                csvWriter.writeheader()

        def write2(self):
            with open(self.path,"a") as file:
                csvWriter = csv.DictWriter(file, fieldnames = self.meta_data)
                if(self.isHeader()):
                    csvWriter.writerow(self.data_store)   
    
        def insertKey(self):
            for i in self.meta_data:
                self.data_store[i] = None 

        def insertVal(self,dataset):
            counter = 0
            for i in dataset:
                self.data_store[self.meta_data[counter]] = i
                counter = counter + 1

        def isHeader(self):
            for i in self.meta_data:
                if (i.__eq__(self.data_store[i])):
                    return False
            return True

        def create(self):
            if(not os.path.exists(self.path)):
                self.write1()
                self.write2()
            else:
                self.write2()

    class Read:
        def __init__(self,header,path):
            self.meta_data = header
            self.path = path
    
        def read1(self,category_counter,data):
            with open(self.path,"r") as file:
                csvReader = csv.DictReader(file, fieldnames = self.meta_data)
                for entry in csvReader:
                    if ((entry[self.meta_data[category_counter-1]].__eq__(data)) and (self.isHeader(entry))):
                        print(entry)
            

        def read2(self):
            with open(self.path,"r") as file:
                csvReader = csv.DictReader(file, fieldnames = self.meta_data)
                for entry in csvReader:
                    if (self.isHeader(entry)):
                        print(entry)

        def isHeader(self,data_store):
            for i in self.meta_data:
                if (i.__eq__(data_store[i])):
                    return False
            return True

    class Update:
        def __init__():
            return

        def update(self):
            return

    class Delete():
        def __init__(self,header,path,filterpath):
            self.meta_data = header
            self.path = path
            self.filter_path = filterpath
            return  
    
        def delete1(self,category_counter,data):
            self.filterReader(self.path,self.filter_path,category_counter,data)
            self.delete2()
            self.filterReader(self.filter_path,self.path,category_counter,data)
            self.delete3(self.filter_path)

        def filterReader(self,rd_path,wt_path,category_counter,data):
            with open(rd_path,"r") as file:
                csvReader = csv.DictReader(file, fieldnames = self.meta_data)
                for entry in csvReader:
                    if ((not entry[self.meta_data[category_counter-1]].__eq__(data)) and (self.isHeader(entry))):
                        self.filterWriter(wt_path,self.extractData(entry))
    
        def filterWriter(self,wt_path,dataset):
            File().Create(self.meta_data,wt_path,dataset).create()

        def extractData(self,dataset):
            data = []
            for i in dataset.values():
                data.append(i)
            return data

        def delete2(self):
            with open(self.path,"w") as file:
                csvWriter = csv.DictWriter(file, fieldnames = self.meta_data)
                csvWriter.writeheader()

        def delete3(self,path):
            os.remove(path)

        def isHeader(self,data_store):
            for i in self.meta_data:
                if (i.__eq__(data_store[i])):
                    return False
            return True


def main():
  meta_data = ["Name","Age"]
  test_data = ["Subhankar","25"]
  test_data1 = ["Subhankar","19"]
  test_data2 = ["Tanir","23"]
  test_data3 = ["Subhankar","36"]
  path = "D:\Test.txt"
  print("\nFile-Created")
  File().Create(meta_data,path,test_data).create()
  File().Create(meta_data,path,test_data1).create()
  File().Create(meta_data,path,test_data2).create()
  File().Create(meta_data,path,test_data3).create()
  print("\nReading specific")
  File().Read(meta_data,path).read1(1,"Tanir")
  print("\nReading All")
  File().Read(meta_data,path).read2()
  filter_path = "D:\Filter.txt"
  print("\nDeletion specific")
  File().Delete(meta_data,path,filter_path).delete1(2,"19")
  print("Read All")
  File().Read(meta_data,path).read2()

main()
