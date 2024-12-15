def hello_world():
    print("Hello, World!")

def ask_yes_no():
    response = input("Yes or No? (y/n): ")
    if response.lower() == 'y':
        print("good")
    elif response.lower() == 'n':
        print(":-(")
