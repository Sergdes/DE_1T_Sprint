def valid(st):
    if    st.count("[") == st.count("]") and st.count("{") == st.count("}") and st.count("(") == st.count(")") :
        return (True)
    else:  return (False)

# Проверка на примере
x1= "[{}{}]"
x2 = "{]"
x3 = "{"
print(valid(x1))
print(valid(x2))
print(valid(x3))