#Positive Numbers Function
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def positivenum(n):
    for num in numlist:
        if num % 2 == 0:
            print(num)


positivenum(numlist)