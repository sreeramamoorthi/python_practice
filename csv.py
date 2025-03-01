
import csv 
  
fields = ['Name', 'Branch', 'Year', 'Percentage'] 
n = int(input("How many records do you want to feed\n"))  
row = [["" for x in range(4)] for y in range(n)]  
for i in range(n): 
    print ("Enter Record [",i,"]") 
    row[i][0] = input("Name : ") 
    row[i][1] = input("Branch : ") 
    row[i][2] = input("Year : ") 
    row[i][3] = input("Percentage : ") 
     
filename = "University.csv" 
  
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(row)
