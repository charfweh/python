def isyear(year):
    leap = False
    if year%4 == 0 and year%400 == 0:
        leap = True
    elif year%100 == 0 and year%400 == 0:
        leap = True
    else:
        leap = False
    return leap
year = int(input())
print(isyear(year))
print("mod",2100%400)
