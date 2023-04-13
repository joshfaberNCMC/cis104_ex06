text = "X-DSPAM-Confidence:    0.8475"
numStart = text.find(':') # this line gives the position of the colon which is 18
numStr = text[numStart + 1 :] # this line splices starting at position 18 + 1 to the end of the string
numFloat = float(numStr.lstrip()) # this strips the leading whitespace from numStr and converts to float

print(numFloat)