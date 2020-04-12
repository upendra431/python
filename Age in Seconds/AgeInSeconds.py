def readingAge():
    return int(input("Enter your age :"))
def ageInseconds():
    return readingAge() * 365 * 24 * 60 * 60

print("Your age in {} seconds".format(ageInseconds()))

"""
O/P:
Enter your age :27
Your age in 851472000 seconds
"""