def calculate_grade(avg):
    if avg >= 90 :
        return 'A'
    elif avg >= 75 :
        return 'B'
    elif avg >= 65:
        return 'C'
    else:
        return 'F'
    

math = int(input("Enter your Math marks==>"))
english= int(input("Enter your Eng marks==>"))
guj=int(input("Enter your Gujarati marks==>"))

total=math+english+guj

avg= (total)/3
grade=calculate_grade(avg)

print(f'Total of All Subject==>{total}')
print(f'Your Avg is ==>{avg}')
print(f'Your grade is ==>{grade}')