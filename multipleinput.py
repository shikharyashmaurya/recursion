a = []
while True:
    value = input()
    if value == "":  # If empty line is entered
        break
    a=a+[int(x) for x in value.split()]
print(a)