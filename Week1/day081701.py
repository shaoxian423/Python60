import  tensorflow as tf

print (tf.__version__)
print(tf.config.list_physical_devices('GPU'))
# Check if TensorFlow can access the GPU

import tensorflow as tf
print (tf.__version__)
print ('pls enter your name:')
name = input()
print ('pls enter your age:')
age = int(input())

print ("hello,%s" % name +  ",\n\t!\a your age is %d" % age)
print ('\t\a')

# %d is for integer
# %s is for string
# %f is for float
# %.2f is for float with 2 decimal places
# %x is for hexadecimal
# %o is for octal
# %e is for scientific notation 
# \n is for new line （backslash）
# \t is for tab
# \\ is for backslash
# \' is for single quote
# \" is for double quote
# \r is for carriage return
# \b is for backspace
# \f is for form feed
# \v is for vertical tab
# \a is for alert (bell)
# \0 is for null character
# \N{name} is for Unicode character with name
# \uxxxx is for Unicode character with 16-bit hex value
# \Uxxxxxxxx is for Unicode character with 32-bit hex value
# \ooo is for character with octal value ooo        