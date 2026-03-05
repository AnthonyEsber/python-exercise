a = 5
b = 6

print((a > 2) and (b >= 6)) # true

print('-'*10)

a = True
b = False

print(a and b) # false
print(a or b) # true
print(not a) # false
print(not b) # true

print('-'*10)

a = 10
b = 12
print(f"a:  {a:04b}")
print(f"b: {b:04b}")
print(f"a ^ b:  {a ^ b:04b}")
print(f"a & b: {a & b:04b}")
print(f"a | b: {a | b:04b}")
print(f"a << 4: {a << 4:04b}")
print(f"b >> 4: {b >> 4:04b}")

print('-'*10)

a = 12
b = 12
a1 = [1,2,3]
b1 = [1,2,3]
a2 = 'test'
b2 = 'test'

print(a is not b)
print(a1 is b1)
print(a2 is b2)

print('-'*10)

print(3 in b1)
print('h' in 'hello world')
print('Hello' not in 'hello world')