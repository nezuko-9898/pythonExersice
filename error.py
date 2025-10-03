
try:
    num=int(input("Enter the number==>"))
except ValueError:
    print("invalid input")
else:
    print("num successfully added:", num) 
finally:
    print("my name is pravin")