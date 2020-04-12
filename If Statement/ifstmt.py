#if is a conditinal stmt
"""
Ex: checking a person age.
Ex: checking the price of the item.
"""

def check_if(age):
    if age>=18:
        print("Riht to vote! {} age people.".format(age))

check_if(18)
#below method won't print any out put , if condition is not satisfied. for this we needto use if else stmt.
check_if(10)

"""
O/P:
Riht to vote! 18 age people.
"""