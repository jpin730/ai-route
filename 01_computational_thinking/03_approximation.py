# Searching the square root approximation applying brute force search

target = int(input('Input an integer number: '))
eps = 0.01
step = eps**2
response = 0.0

while abs(response**2 - target) >= eps and response <= target:
    response += step

if abs(response**2 - target) >= eps:
    print(f'The square root of {target} was not found.')
else:
    print(f'The square root approximation of {target} is {response}.')
