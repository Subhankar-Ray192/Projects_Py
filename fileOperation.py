import csv
import os
import sys

class Create:
    def __init__(self,header,p,dataset):
        self.meta_data = header
        self.path = p
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
    def __init__(self,hd,p):
        self.meta_data = hd
        self.path = p
        return
    
    def read1(self,category_counter,data):
        with open(self.path,"r") as file:
            csvReader = csv.DictReader(file, fieldnames = self.meta_data)
            for entry in csvReader:
                if (entry[self.meta_data[category_counter-1]].__eq__(data)):
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
    def __init__():
        return  

    def delete1(self):
        return

    def delete2(self):
        return

def main():
  meta_data = ["Name","Age"]
  test_data = ["Subhankar","25"]
  test_data1 = ["Subhankar","19"]
  test_data2 = ["Subhankar","23"]
  test_data3 = ["Subhankar","36"]
  path = "D:\Test.txt"
  print("\nFile-Created")
  Create(meta_data,path,test_data).create()
  Create(meta_data,path,test_data1).create()
  Create(meta_data,path,test_data2).create()
  Create(meta_data,path,test_data3).create()
  print("\nReading specific")
  Read(meta_data,path).read1(1,"Subhankar")
  print("\nReading All")
  Read(meta_data,path).read2()

main()
