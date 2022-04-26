# en utilisant une loop
# i = 0
# while i < 3:
#     print("meow")
#     i  += 1

# en utilisant une list
#for _ in range(3):
#       print("meow")

# print("meow\n" * 3, end="")


while True:
        n = int(input("What's n? "))
        if n > 0:
                break      
                
 for _ in range(n):
        print("meow")
        
        
        
# or

def main():
        number = get_number()
        meow(number)
        
def get_number():
        while True:
                n = int(input("What's n? "))
                if n > 0:
                        break
        return n

def meow(n):
        print("meow")
                
