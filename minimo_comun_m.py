num1= 12
num2= 8
if num1 > num2:
    control =num1
else:
    control =num2

while True:
    if control % num1 ==0 and control % num2 == 0:
        print("el mcm es:",control)
        break
    control += 1