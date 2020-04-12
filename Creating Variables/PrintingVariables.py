my_variable=5
x="Hello Python!"
#print("my_variable is "+my_variable)
# The above line of code gives an Error TypeError: can only concatenate str (not "int") to str
# my_variable is a type of int using + operator we cannot do that' why we use str(my_variable)
print("my_variable is "+str(my_variable))
print(x)

# below is multiline comments 
"""
O/P: 
my_variable is 5
Hello Python!
"""