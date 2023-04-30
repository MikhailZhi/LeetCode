# Reducing to zero.
""" Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2,
otherwise, you have to subtract 1 from it. """

"""
Full version with printing on each step

numb = int(input('num = '))
steps = 0

while numb>0:
    print(steps, numb)
    if numb%2 == 0:
        numb /=2
    else:
        numb -=1
    steps +=1

print(steps, numb, '\n')    
print('Redcued to zero in', steps, 'steps')
"""

# Short version to site

numb = int(input('num = '))
steps = 0

while numb>0:
    if numb%2 == 0:
        numb /= 2
    else:
        numb -= 1
    steps += 1

return teps
