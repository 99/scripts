import random

l= "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"

n = "0123456789"
sChar = "[]{}()*;/,_-?!@#"

gen = l + u + n +sChar
len = 24

passw = "".join(random.sample(gen, len))

print(f"password : {passw}" )
