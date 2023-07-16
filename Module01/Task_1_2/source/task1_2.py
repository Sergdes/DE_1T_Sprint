 

def RevStr(st):
    return  st[::-1]

def Paliandr(st):
    rev = RevStr(st)
    if (rev == st):
        return True
    else:
        return False
# Проверка на примере
x1 = "taco cat"
x2 = "rotator"
x3 =  "black cat"
print(Paliandr(x1), Paliandr(x2), Paliandr(x3))
