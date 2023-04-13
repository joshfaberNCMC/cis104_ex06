'''Count method syntax example'''

string1 = 'In the beginning the Universe was created. This had made many people very angry and has been widely regarded as a bad move.'
string2 = 'the'

total = string1.count(string2[0:50]) # string2 is the substring I'm searching for, 0 is the index location of the main string that I'm starting my search at, and 50 is the location I'm searching up to.
print(total) 