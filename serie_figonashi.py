# Seria Figonashi

print("________________________________________")
print("|           Serie Figonashi             |")
print("|_______________________________________|")
print("")

#process
a = 0
b = 1
c = a + b

while c < 900 :
    a = b
    b = c
    c = a + b
    print(c)