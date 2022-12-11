#1. 9-floor building with 4 entrances and 144 appartments




#2.Deternine days in a year
y=int(input('Enter year number:'))
if y % 100 !=0 and y % 4 == 0:
    print('The year', y, 'has 366 days.')
elif y %400 == 0:
    print('The year', y, 'has 366 days.')
else:
    print('The year', y, 'has 365 days.')

#3.Existing or non-existing triangle
a = float(input('Enter 1st side of triangle:'))
b = float(input('Enter 2st side of triangle:'))
c = float(input('Enter 3rd side of triangle:'))
if a+b>c and a+c>b and b+c>a:
    print('Such triangle exists')
else:
    print('Such triangle does not exist')