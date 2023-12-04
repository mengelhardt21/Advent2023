from pathlib import Path

result = 0
p = Path(__file__).with_name('data1.txt')
with p.open('r') as f:
    list = f.readlines()

list = [x.strip() for x in list]

for item in list:
    str = ""
    for c in item:
        if c.isdigit():
            str = str + c
    if len(str) > 2:
        d1 = str[0]
        d2 = str[len(str) - 1]
        str = "" + d1 + d2
    if len(str) == 1:
        str = str + str
    result += int(str) 

print(result)
f.close()

