# Searching the exact square root

target = int(input('Input an integer number: '))
response = 0

while response**2 < target:
    response += 1

if response**2 == target:
    print(f'The exact square root of {target} is {response}.')
else:
    print(f'The number {target} doesn\'t have an exact square root.')
