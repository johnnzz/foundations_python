
file = open("data.txt", "a")

while (True):
    user_input = input("enter something: ")
    if user_input.lower() == "exit":
        break
    file.write(user_input + "\n")
file.close()
