# below is the implemenentation that generates even nos from 0 upto n
# generators can be used if we dont want to use extra space
# you get access to next(genObj) to process iterator once

def genEvenNosUpToN(n):
    for i in range(0, n):
        # yield gives one value at a time
        yield i*2

g = genEvenNosUpToN(5) # g => generator object

next(g) # 0
next(g) # 2
print(next(g)) # o/p : 4

# iterate through even nos from generator
for i in genEvenNosUpToN(5):
    print(i)

"""
Output:
$ py even_nos_generator.py 
0
2
4
6
8
"""