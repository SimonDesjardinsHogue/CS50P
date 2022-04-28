def main():
    x = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    if reponse(x):
        print("Yes")
    else:
        print("No")

def reponse(x):
    return x == "42" or x == "forty-two" or x == "forty two"


main()
