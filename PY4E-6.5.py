# Exercise 5: Slicing strings
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
#Find the position of the colon
startslice = str.find(':')
print(startslice)
#Find everything after the colon (+1 used because find starts and includes colon) and stores in a string
valueextracted = str[startslice+1:]
print(valueextracted)
#Cleans whitespace in the new string
cleanvalue = valueextracted.strip()
#Converts new string into a float
floatvalue = float(cleanvalue)
#Print float and check the type
print(floatvalue)
print(type(floatvalue))