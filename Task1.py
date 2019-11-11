#Task1: Converting txt to csv

#import the module
import csv

#open the txt file
f = open("2000_BoysNames.txt")

#read each line
x = f.readlines()

#Create a list which we would put the names and count in file
s = []

# Add all the names and count in file with a comma
for i in x:
    i = i.replace(",", "")
    j = i.replace(" ", ",")
    s.append(j)


# Write words into csv file
csvex = csv.writer(open("2000_BoysNamess.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
csvex.writerow(["First Name","Count"])
csvex.writerow(s)
f.close()
