#Task2
#Write a python program that prompts the user for the name of .csv file then reads and displays each line of the file as a Python list. Test your program on the 2 csv files that you generated in Task 1
import csv
def displayFile():
    #prompt the user for a file to import
    csvFile = input("Input the file name of the .csv file: ")
    #filter = "CSV file (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    f = open(csvFile,"r")
    if not f: return
    reader = csv.reader(f)
    next(reader,None)
    for row in reader:
        for lists in row:
            print(lists)
            

displayFile()