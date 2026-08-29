suhu = float(input("Suhu:")) 

if suhu < 25:
    suhu= "Dingin"
elif suhu > 30:
    suhu = "Panas"
else:
    suhu = "normal" 
print("", suhu)  