import time
name = input("enter your name ")
text = ["Hello", "How are you"]
for i in range(len(text)):
    print(f"{text[i]} {name}")
    time.sleep(1)
print("I am bot try app in python")
