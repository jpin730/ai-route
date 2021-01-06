# Searching the square root approximation applying binary search
# IMPORTANT: Information must be ordered

target = int(input('Input an integer number: '))
eps = 0.01
roof = max(1.0, target)
floor = 0
response = (roof + floor) / 2

while abs(response**2 - target) >= eps and response <= target:
    if response**2 < target:
        floor = response
    else:
        roof = response

    response = (roof + floor) / 2

print(f'The square root approximation of {target} is {response}.')
