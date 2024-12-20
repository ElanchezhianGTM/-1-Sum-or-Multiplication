print("Enter two numbers and if the multiplication of the number is less than or equal to 1000 you get their multiplication else you'll get their sum as answer")

f_n = int(input("Type the first number: "))
s_n = int(input("Type the second number: "))

ans_m = f_n * s_n
ans_s = f_n + s_n

if ans_m <= 1000:
    print(f"The multiplication of {f_n} and {s_n} is {ans_m}")
else:
    print(f"The sum of {f_n} and {s_n} is {ans_s} because their multiplication was above 1000")