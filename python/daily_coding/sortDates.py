# https://www.geeksforgeeks.org/sort-an-array-of-string-of-dates-in-ascending-order/
# https://www.geeksforgeeks.org/how-to-efficiently-sort-a-big-list-dates-in-20s/
from datetime import datetime


dates = ['01 Mar 2017', '03 Feb 2018', '15 Jan 1998']

monthMap = {'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12}

# comp(dates[0], dates[1])
# https://www.geeksforgeeks.org/python-sort-list-of-dates-given-as-strings/
# https://stackoverflow.com/questions/17627531/sort-list-of-date-strings
def convert(date):
    return datetime.strptime(date, '%d %b %Y')

def convert2(date):
    year = int(date.split(' ')[2])
    month = monthMap[date.split(' ')[1]]
    date = int(date.split(' ')[0])

    return year, month, date

# print(convert(dates[0]))
# print(sorted(dates, reverse=True))
print(sorted(dates, key=convert))
print(sorted(dates, key=convert2))