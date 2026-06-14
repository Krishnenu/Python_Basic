# Python Data Types

Python data types can be broadly categorized into **Immutable** and **Mutable** types.

---

# Immutable Data Types

Immutable objects cannot be modified after creation. Any change results in a new object being created.

## Number

```python
1234
3.14
3 + 4j
0b111

from decimal import Decimal
from fractions import Fraction

Decimal("10.5")
Fraction(3, 4)
```

### Types

- `int`
- `float`
- `complex`
- `Decimal`
- `Fraction`

---

## String

```python
"spam"
"Bob's"
b'a\x01c'
u'sp\xc4m'
```

### Types

- `str`
- `bytes`

---

## Tuple

```python
(1, "spam", 4, "U")

tuple("spam")
```

### Examples

- Tuple
- Named Tuple (`collections.namedtuple`)

---

## Boolean

```python
True
False
```

### Type

- `bool`

---

## None

```python
None
```

### Type

- `NoneType`

---

# Mutable Data Types

Mutable objects can be modified after creation.

## List

```python
[1, [2, "three", 4.5]]

list(range(10))
```

### Type

- `list`

---

## Dictionary

```python
{
    "food": "spam",
    "taste": "yum"
}

dict(hours=10)
```

### Type

- `dict`

---

## Set

```python
set("abc")

{"a", "b", "c"}
```

### Type

- `set`

---

## File Objects

```python
open("eggs.txt")

open(r"C:\ham.bin", "wb")
```

### Type

- File Object

---

# Callable Objects

## Functions

```python
def greet():
    print("Hello")
```

---

## Modules

```python
import math
```

---

## Classes

```python
class Person:
    pass
```

---

# Advanced Python Concepts

## Decorators

```python
@decorator
def my_function():
    pass
```

## Generators

```python
def counter():
    yield 1
```

## Iterators

```python
iterator = iter([1, 2, 3])
```

## Metaprogramming

```python
Person = type("Person", (), {})
```

---

# Quick Reference

| Mutable              | Immutable |
| -------------------- | --------- |
| List                 | int       |
| Dictionary           | float     |
| Set                  | complex   |
| File Object          | Decimal   |
| Most Class Instances | Fraction  |
| Custom Objects       | str       |
|                      | bytes     |
|                      | tuple     |
|                      | bool      |
|                      | NoneType  |

---

# Interview Question

## Can a tuple contain mutable objects?

Yes.

```python
t = ([1, 2], 3)

t[0].append(4)

print(t)
# ([1, 2, 4], 3)
```

The tuple itself is immutable, but it can store references to mutable objects such as lists.
