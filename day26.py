# Day 26 - Nested Logic
rDay, rMonth, rYear = [int(x) for x in input().split(' ')]
dDay, dMonth, dYear = [int(x) for x in input().split(' ')]

if (rYear, rMonth, rDay) <= (dYear, dMonth, dDay):
    print(0)
elif (rYear, rMonth) == (dYear, dMonth):
    print(15*(rDay-dDay))
elif rYear == dYear:
    print(500*(rMonth-dMonth))
else:
    print(10000)


