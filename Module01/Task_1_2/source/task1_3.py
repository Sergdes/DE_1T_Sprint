def ArabToRoma(x):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]
    t = thous[x // 1000]
    h = hunds[x// 100 % 10]
    te = tens[x// 10 % 10]
    o =  ones[x % 10]
    return t+h+te+o

# Проверка на примере
print(ArabToRoma(3))
print(ArabToRoma(9))
print(ArabToRoma(1945))

