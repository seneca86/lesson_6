# %%
fib_0= 0
fib_1= 1
i = 0
while i < 10:
    i += 1
    fib = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib
    print(f'{fib=}')
# %%
fib_0, fib_1 = 0, 1
i = 0
while (i:= i + 1) <= 10:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    print(f'{fib=}')

# %%
fib_0, fib_1 = 0, 1
i = 0
while True:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    if (fib > 50):
        break
    print(f'{fib=}')
# %%
fib_0, fib_1 = 0, 1
i = 0
while True:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    if (fib > 100) and (fib < 200):
        continue
    elif fib > 400:
        break
    print(f'{fib=}')
# %%
fib_0, fib_1 = 0, 1
i = 0
while (i:= i + 1) <= 10:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    print(f'{fib=}')
else:
    print('The loop finished normally')
# %%
fib_0, fib_1 = 0, 1
i = 0
while True:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    if (fib > 50):
        break
    print(f'{fib=}')
else:
    print('This will never be seen if the break is triggered')
# %%
horsemen = 'conquest', 'war', 'famine', 'death'
i = -1
while (i:= i + 1) < len(horsemen):
    print(horsemen[i])

# %%
for i in horsemen:
    print(i)
# %%
alphabet = 'abcde'
for i in alphabet:
    print(i)

# %%
presidents = ['Washington',
              'Adams',
              'Jefferson',
              'Madison',
              'Monroe',
              'Quincy',
              'Jackson',
              'Van Buren',
              'Harrison',
              'Tyler',
              'Polk',
              'Taylor']

for p in presidents:
    if p.startswith('J'):
        continue
    elif p.startswith('H'):
        print('Found a president starting with H')
        break
    print(p)
else:
    print('Did not encounter any president starting with H')
# %%
for i in range(3):
    print(i)
# %%
for i in range(2,5):
    print(i)
# %%
for i in range(2, 10, 2):
    print(i)
# %%
for i in range(3, -1, -1):
    print(i)
# %%
