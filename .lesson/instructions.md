# Loops

## Introduction

Loops are a fundamental piece of most programming languages, and Python is not an exception. Similarly to e.g. R, Python counts with two main types of loops: the `for` loop and the `while` loop.

## `while` loops

### Definition

The `while` loop repeats a set of commands until a certain condition is met. This has the risk of running the loop forever if the condition is never met, which is a reason why `while` loops are less popular than `for` loops. They are, nevertheless, more general, and particularly useful in numerical calculus.

Let's start with a `while` loop that calculates the first 12 Fibonacci numbers:

```python
fib_0= 0
fib_1= 1
i = 0
while i < 10:
    i += 1
    fib = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib
    print(f'{fib=}')
```

We can make things a bit more compact with a couple of tricks: multiple assignments and the walrus operator for assignment statements:

```python
fib_0, fib_1 = 0, 1
i = 0
while (i:= i + 1) <= 10:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    print(f'{fib=}')
```

In any case, the workings of the loop are the same: initial values are assigned, an expression gets evaluated, a few statements are executed, and the loop starts again until the expression becomes true.

### `break`

Sometimes it is not clear ex ante when we want the loop to stop. In this example, maybe we want the loop to run until the Fibonacci numbers surpass `50`. In that case we can use the `break` command, which dwells inside the loop. We typically do not need the condition in the `while` anymore, so we can write `while True`.

```python
fib_0, fib_1 = 0, 1
i = 0
while True:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    if (fib > 50):
        break
    print(f'{fib=}')
```

### continue

We may want to skip a few lines of code in a loop without breaking its flow. In those cases we will use `continue`. For instance, we may want to skip those Fibonacci numbers between 100 and 200, but keep the loop until they reach 400.

```python
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
```

### optional `else``

`while` loops can have an `else` clause afterwards that evaluates once the `while` loop completes unless the reason is a `break`. Let's compare these two examples:

```python
fib_0, fib_1 = 0, 1
i = 0
while (i:= i + 1) <= 10:
    fib = fib_1 + fib_0
    fib_0, fib_1 = fib_1, fib
    print(f'{fib=}')
else:
    print('The loop finished normally')
```

```python
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
```

This `else` statement is like a _break checker_ that we get for free with the `while` loop.

## `for` loop

### Definition

The `for` loop is the classic loop that allows us to iterate through a data structure in a controlled manner. It is particularly important in Python because of the use of _iterators_, which we will cover later on.

`for` loops can simplify `while` loops when we are traversing a predefined data structure. See how the code below becomes much more concide if we iterate through the tuple.

```python
horsemen = 'conquest', 'war', 'famine', 'death'
i = -1
while (i:= i + 1) < len(horsemen):
    print(horsemen[i])
```

```python
for i in horsemen:
    print(i)
```

We can iterate not only through tuples but through, e.g., strings.

```python
alphabet = 'abcde'
for i in alphabet:
    print(i)
```

### `break`, `continue`, and `else`

`for` loops feature `break`, `continue`, and `else` in a similar fashion to `while` loops. Let's illustrate this with a few examples:

