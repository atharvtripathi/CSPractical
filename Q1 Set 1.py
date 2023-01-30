import csv

#input Roll number you want to search

number = input('Enter number to find: ')
found=0
#read csv, and split on "," the line

with open('Student_Details.csv') as f:
     csv_file = csv.reader(f, delimiter=",")
     #loop through csv list
     for row in csv_file:

     #if current rows index value (here 0) is equal to input, print that row
          if number ==row[0]:
              print (row)
              found=1
          else:
               found=0
if found==1:
     pass

else:
     print("Record Not found")