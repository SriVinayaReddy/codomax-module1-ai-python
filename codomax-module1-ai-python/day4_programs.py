# Day 4: Beginner Python Programs

# 1. Even or Odd
num = 7
print("Even" if num % 2 == 0 else "Odd")

# 2. Largest of three numbers
a, b, c = 10, 25, 15
print("Largest:", max(a, b, c))

# 3. Factorial
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")

# 4. Multiplication table
num = 6
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 5. Sum of numbers (1 to n)
n = 10
total = sum(range(1, n + 1))
print(f"Sum of 1 to {n} is {total}")

# 6. Simple calculator
x, y, op = 20, 4, "+"
if op == "+": result = x + y
elif op == "-": result = x - y
elif op == "*": result = x * y
elif op == "/": result = x / y
print(f"{x} {op} {y} = {result}")

# 7. List operations
skills = ["Python", "ML"]
skills.append("DL")
skills.remove("ML")
print("Skills:", skills, "| Count:", len(skills))
