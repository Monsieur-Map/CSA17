# Người dùng nhập từ console số nguyên dương n
# In ra tam giác vuông với n dòng + số lượng '*' = số thứ tự dòng
# *
# **
# ***

# CODE CỦA PHÚC
# n = int(input("Nhập số dòng: "))
# i= 1
# sao = "*"
# if n < 3:
#     print("Không đủ điều kiện để làm ra một tam giác")
# else:
#     while i <= n:
#         print(sao) 
#         sao += "*"
#         i +=1
        
#CODE của cô

while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n == "exit":
        print("Bye")
        break
    try:
        if n <= 1:
            print("Vui lòng nhập số nguyên dương! lớn hơn 1")
            n = ""
            continue
            
        
    except Exception as e:
        print("Lỗi bạn ơi")
        continue
        

    for i in range (n):
        print("*" * (i+1))
    
        
          