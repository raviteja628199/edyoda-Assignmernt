#imteger(immutable)
#num = 10
#num1 = 10
#num2 = 20

# arithmatic operators

# +
# -
# *
# /
# % - MODULUS
# ** - EXPONENTIA
# // - FLOOR DIVISION


#no_1 =20
#no_2 = 30
#add = no_1 + no_2
#print("addition of",no_1,"and",no_2,":",add)

#substraction(-)

#no_1 =20
#no_2 = 30
#sub = no_1 - no_2
#print(type(sub))
#print("substraction of",no_1,"and",no_2,":",sub)

#divion(/)
#no_1 =10
#no_2 = 5
#division = no_1 / no_2
#print(type(division))#print("division of",no_1,"and",no_2,":",division)

#modulus(%) returns remiander
#no_1 =10
#no_2 = 5
#modulus = no_1 % no_2
#rint("modulus of",no_1,"and",no_2,":",modulus)

#exponentia (**) - power#
# no_1 =10
#no_2 = 5
#expo = no_1 ** no_2
#print("expo of",no_1,"and",no_2,":",expo)

#floor division (//) - coverts the float valuse into int which is returned by /

#no_1 = 26
#no_2 = 9
#div= no_1 / no_2
#print("division of",no_1,"and",no_2,":",div)


#floor_div = no_1 // no_2#
#print("floor division of",no_1,"and",no_2,":",floor_div)


#logical operator
# 1. and - returns true if both statements are true
# 2. or - returns true if one of the statements is true
# 3. not - reverse the output, it returns the false is the output is True

#num1 = 10
#num2 = 20 
#num3 = 30
#and operator
#is_true = num1 is not num2 and num1 is not num3
#print(is_true)

# not operator
#is_true = num1 is num2 or num1 is not num3
#print(is_true)

#or operator
#is_true = num1 is num2 or num1 is not num3
#print(is_true)

#membership operator

#in - returns true if a sequence with the specified value is present in the object 
#not in - returns true if a sequence

lst1 = [10,20,30,60,70]
num1 = 70

is_present = num1 in lst1
print(is_present)

is_not_present = num1 not in lst1
print(is_not_present)


#comparision operators

# == - equal
# != - not equal
# > - greater than
# < - lesss than
# >= - greater than equal to 
# <= - less than equal to

#num_1 = 40
#num_2 = 90

#==
#equal = num_1 = num_2
#print("equal :",equal)

#!=

#not_equal = num_1 != num_2
#print("not_equal,:",equal)

#>
#greater_than = num_1 > num_2
#print("greater than  :",greater_than)

#<
#less_than = num_1 < num_2
#print("less_than :",less_than)

#>=
#greater_than_equal_to = num_1 >= num_2
#print("greater_than_equal_to :",greater_than_equal_to)

#<
#less_than_equal_to = num_1 <= num_2
#print("less_than_equal_to :",less_than_equal_to)

# identity operator

# is - returns true if both the variables are the same object
# is not - returns true if both the variables are not the same object 

#num1 = 10
#num2 = 120 
#is_equal = num1 is  num2
#print(is_equal)


#num1 = 10
#num2 = 120 
#is_equal = num1 is not  num2
#print(is_equal)

# assignment operator

# =
# +=
# -=
# *=
# /=
# %=
# - 
# **=


num1 = 20
num2 = 40
print("num1 before addition :",num1)
num1 += num2 #num1 = num1 + num2
print("num1 after addition :",num1)

num1 = 20
num2 = 40
print("num1 before multiply :",num1)
num1 *= num2 #num1 = num1 + num2
print("num1 after multiply :",num1)

num1 = 20
num2 = 40
print("num1 before division :",num1)
num1 /= num2 #num1 = num1 + num2
print("num1 after division:",num1)

num1 = 20
num2 = 40
print("num1 before modulus :",num1)
num1 %= num2 #num1 = num1 + num2
print("num1 after modulus :",num1)

num1 = 20
num2 = 40
print("num1 before exponentia :",num1)
num1 **= num2 #num1 = num1 + num2
print("num1 after exponentia :",num1)




