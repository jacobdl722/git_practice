def printText(text):
    return f"{text} World!"

text = input().title()
current_time = int(input("What time is it? "))
print(printText(text=text))
print(f"Time of now is {current_time}")