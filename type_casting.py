"""
Casting in python is the process of converting a value from one datatype to another

In the print() function, we can use a comma to seperate values of different data types
"""

#int to str casting
print("casting ", 123, "from ", type(123), "to ", type(str(123)))

#str to int casting
print("casting '123' from ", type('123'), "to ", type(int('123')))

#float to int conversion
print("casting ", 1.23, "from ", type(1.23), "to ", type(int(1.23)))

#int to float conversion
print("casting ", 123, "from ", type(123), "to ", type(float(123)))

#str to float conversion
print("casting '123 from ", type('123'), "to ", type(float('123')))

#float to str conversion
print("casting ", 1.23, "from ", type(1.23), "to ", type(str(1.23)))


"""
Note: you cannot cast alphabetic characters to int or float, but you can cast all float and int to strings, 
for example int('a') will throw an error.

please see the description below for more information

cheers
"""