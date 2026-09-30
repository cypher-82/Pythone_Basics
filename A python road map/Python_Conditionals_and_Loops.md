# Python Lecture: Conditional Statements & Loops (Basics to Advanced)

---

# PART 1: Conditional Statements (Decision Making)

Conditional statements program ko **decision lene** ki power dete hain — "agar ye condition true hai to ye karo, warna wo karo."

## 1. `if` Statement — Sabse Basic

```python
age = 20
if age >= 18:
    print("Aap adult hain")
```

**Zaroori baatein:**
- `if` ke baad condition likhte hain jo `True` ya `False` mein evaluate hoti hai
- Condition ke baad **colon `:`** lazmi hai
- Agle line se **indentation** (4 spaces ya 1 tab) shuru hoti hai — Python indentation se hi blocks pehchanta hai (curly braces `{}` nahi hoti jaisa C/Java mein)

**Common mistake:**
```python
if age >= 18:
print("Adult")   # IndentationError — indent nahi kiya
```

## 2. `if-else` — Do Raaste

```python
age = 15
if age >= 18:
    print("Adult hain")
else:
    print("Minor hain")
```

## 3. `if-elif-else` — Multiple Raaste

```python
marks = 75

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(grade)   # B
```

**Kaise kaam karta hai:** Python **upar se neeche** check karta hai, jaise hi koi condition `True` milti hai, wahi block chalta hai aur **baaki saare `elif`/`else` skip** ho jate hain — chahe wo bhi True hon.

```python
x = 10
if x > 5:
    print("5 se bara hai")
elif x > 8:
    print("8 se bara hai")   # ye kabhi nahi chalega, chahe True ho
```

## 4. Nested Conditionals (Condition ke andar Condition)

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID chahiye")
else:
    print("Underage — entry nahi")
```

## 5. Logical Operators Conditions ke Sath (Compact tareeqa)

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```
Isko nested karne ki bajaye `and`/`or` se ek hi line mein likh sakte hain — cleaner code.

## 6. Ternary Operator (One-line if-else)

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

## 7. `pass` Statement

```python
if age >= 18:
    pass    # TODO: baad mein logic likhna hai
```
Python empty block allow nahi karta, is liye placeholder chahiye hota hai.

## 8. Truthy/Falsy Values in Conditions (Important!)

Python mein `if` sirf `True`/`False` hi nahi, kisi bhi value ko check kar sakta hai.

**Falsy values (jo False ki tarah behave karti hain):**
```
0, 0.0, "", [], {}, (), set(), None, False
```

**Baki sab kuch Truthy hai:**
```python
name = ""
if name:
    print("Naam hai")
else:
    print("Naam khaali hai")  # ye chalega
```

```python
my_list = []
if my_list:
    print("List mein data hai")
else:
    print("List khaali hai")   # ye chalega
```

---

# PART 2: Loops (Repetition)

Loops se hum same code baar baar chala sakte hain bina usay copy-paste kiye.

## 1. `while` Loop

Jab tak condition `True` rahe, tab tak chalta rahega:

```python
count = 1
while count <= 5:
    print(count)
    count += 1     # ye zaroori hai warna infinite loop ban jayega!
```
Output: `1 2 3 4 5`

**Infinite Loop ka khatra:**
```python
count = 1
while count <= 5:
    print(count)
    # count += 1 bhool gaye — ye hamesha chalta rahega!
```
Hamesha check karein ke loop ke andar koi cheez hai jo condition ko eventually False bana de.

## 2. `for` Loop — Sabse Zyada Use Hota Hai

Kisi bhi iterable (list, string, tuple, range waghera) ke har element par chalta hai:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**String par loop:**
```python
for char in "Python":
    print(char)
```

**`range()` Function — Numbers pe Loop:**
```python
for i in range(5):        # 0,1,2,3,4  (5 exclude hota hai)
    print(i)

for i in range(1, 6):     # 1,2,3,4,5
    print(i)

for i in range(0, 10, 2): # 0,2,4,6,8  (step = 2)
    print(i)

for i in range(10, 0, -1): # 10,9,8...1  (ulta counting)
    print(i)
```

`range(start, stop, step)` — **stop hamesha exclude hota hai**, ye bohot common confusion hai.

## 3. `break` — Loop ko Force Rokna

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4
```

## 4. `continue` — Sirf Current Iteration Skip Karna

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0 1 3 4
```

**Farq:** `break` = loop se bahar nikal jao. `continue` = is iteration ko chor kar agli pe jao.

## 5. Nested Loops (Loop ke Andar Loop)

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

**Example — Multiplication table:**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

## 6. `else` with Loops

Loop ke sath `else` laga sakte hain — ye tab chalta hai jab loop bina `break` ke poora complete ho:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop bina break ke complete hua")   # ye chalega
```

**Real use-case — search karna:**
```python
numbers = [1, 3, 5, 7]
target = 4

for num in numbers:
    if num == target:
        print("Mil gaya!")
        break
else:
    print("Nahi mila")   # ye chalega kyunke 4 list mein nahi
```

## 7. `enumerate()` — Index bhi Chahiye To

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

## 8. `zip()` — Do Lists Ek Sath Loop Karna

```python
names = ["Ali", "Sara"]
ages = [25, 22]
for name, age in zip(names, ages):
    print(name, age)
# Ali 25
# Sara 22
```

---

# Conditionals + Loops Ka Combo (Real Patterns)

**Even/Odd numbers separate karna:**
```python
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        print(n, "Even")
    else:
        print(n, "Odd")
```

**Counting with condition:**
```python
count = 0
for n in range(1, 21):
    if n % 3 == 0:
        count += 1
print(f"3 ke multiples: {count}")
```

**FizzBuzz (classic interview question):**
```python
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

# Practice Tasks

1. `while` loop se 1 se 10 tak numbers print karein, lekin sirf odd numbers
2. `for` loop se koi list lein aur usme se negative numbers count karein
3. Nested loop se ye pattern print karein:
```
*
**
***
****
```
4. `break` use karke ek list mein pehla number dhoondein jo 50 se bara ho
