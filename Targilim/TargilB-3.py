num = int (input("enter number with 3 digit: "))

print(num)
print("============================")
print(f"{num%10}{num//10%10}{num//100}")