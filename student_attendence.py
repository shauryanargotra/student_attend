""" this is the program where we will mark students present or absent
and then send their parents emails regarding their absent ward"""

from datetime import date
from datetime import time
import csv
myfile = open('student-attend.csv', 'a')
print('Please Mark the Following Student P or A or L: ')
myday = date.today()
writer = csv.writer(myfile)
writer.writerow([myday])

def students():
    shaurya = input('shaurya: ')
    rohan = input('Rohan: ')
    kashav = input('kashav: ')
    ark = input('ark: ')


    writer.writerow(['', '', '', ''])
    writer.writerow(['shaurya', 'rohan', 'kashav', 'ark'])
    writer.writerow([shaurya, rohan, kashav, ark])

    if shaurya.upper() == 'A':
        return 'shauryanargotra@gmail.com'
    elif rohan.upper() == 'A':
        return 'nshaurya@aol.com'


student = students()
