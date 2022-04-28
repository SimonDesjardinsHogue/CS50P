def main():
    greeting = input("Greeting: ").strip().lower()
    greetingh = greeting.startswith("h")

    if "hello" in greeting:
        print("$0")
    elif greetingh == True:
        print("$20")
    else:
        print("$100")

main()
