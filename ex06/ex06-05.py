text = "X-DSPAM-Confidence:    0.8475"
numStart = text.find('0')
numEnd =text.find('5')
numFull = text[numStart : numEnd + 1]
numFull = float(numFull)

# print(numStart)
# print(numEnd)
print(numFull)