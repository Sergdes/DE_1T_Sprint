#Умножить два бинарных числа в формате строк

def BiMultip (x1,x2):
    x3 = int (x1,2) *int (x2,2)
    return (bin(x3))
# Проверка на примере
x1 = "111"
x2 = "101"
print(BiMultip (x1,x2))