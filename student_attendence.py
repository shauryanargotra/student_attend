""" this is the program where we will mark students present or absent
and then send their parents emails regarding their absent ward"""

import csv
from datetime import date

my_file = open('student-attend.csv', 'a')
print('Please Mark the Following Student P or A or L: ')

# entering date and leaving a blank row in the file
myday = date.today()
writer = csv.writer(my_file)
writer.writerow([])
writer.writerow([myday])
mystu_list = []


def students():
    shaurya = input('shaurya: ')
    rohan = input('Rohan: ')
    krish = input('krish: ')
    ark = input('ark: ')

    writer.writerow([])
    writer.writerow(['shaurya', shaurya])
    writer.writerow(['Rohan', rohan])
    writer.writerow(['krish', krish])
    writer.writerow(['Ark', ark])
    # writer.writerow([shaurya, rohan, krish, ark])

    # if shaurya.upper() == 'A':
    #     return 'student mail'
    # elif rohan.upper() == 'A':
    #     return 'student mail'
    # elif krish.upper() == 'A':
    #     pass
    # elif ark.upper() == 'A':
    #     pass

    if shaurya.upper() == 'A':
        mystu_list.append('student mail')
    if rohan.upper() == 'A':
        mystu_list.append('student mail')
    if krish.upper() == 'A':
        pass
    if ark.upper() == 'A':
        pass
    return mystu_list


student = students()
print(student)
