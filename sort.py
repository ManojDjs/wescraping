from datetime import datetime
# Function to print the data stored in the list
def printDates(dates):
    for i in range(len(dates)):
        print(dates[i])
if __name__ == "__main__":
    dates =  ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018",
              "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]
    # Sort the list in ascending order of dates
    dates.sort(key = lambda date: datetime.strptime(date, '%d %b %Y'))
    # Print the dates in a sorted order
    printDates(dates)
    lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
    # Using sort() function
    lst.sort(key=len)
    print(lst.sort(reverse=True))
    print(lst)
