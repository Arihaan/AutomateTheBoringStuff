import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    results = ''
    for _ in range(100):
        i = random.randint(0, 1)
        if i == 0:
            results += 'T'
        else:
            results += 'H'

    if 'TTTTTT' in results or 'HHHHHH' in results:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks/100))
