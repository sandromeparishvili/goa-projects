# in binary code 1 represents  ----- ON
# And in binari code 2 represents ------ OFF
# Binary code helps computers to perform billions of tiny operations

print(type(5 < 9))
print(type(50 > 100)) #---------------- 'bool' (boolean)'s value is either "true" 
 # or "false", a comparison question is always is in boolean value.

soil_moisture = 80
print(soil_moisture < 100) # ---------- True
type(soil_moisture)

soil_moisture = 120
print(soil_moisture < 100) # ---------- False
type(soil_moisture)

# ------------------------  And - Or

print(True and True) #---------- and is an operator, but it supports "False"
print(True and False)
print(False and False)

print(True or True)
print(False or True) # ---------- or is an operator too, but supports "True"
print(False or False)
#------------------------------------
# and operator

# And operator Preference False

print(True and True) # True
print(True and False) # False
print(False and False) # False
print(False and True) # False

# or operator

# or operator Preference True

print(True or True) # True
print(True or False) # True
print(False or False) # False
print(False or True) # True