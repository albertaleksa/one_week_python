def func():
    global glob1
    print(f"glob1 = {glob1}")

    glob1 = 5


glob1 = 10
func()
print(f"glob1 = {glob1}")