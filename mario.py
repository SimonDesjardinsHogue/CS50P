#imprimer les cubes a cents
def main():
  print_column(3)
  
 
def print_column(height):
  for _ in range(height):
  print("#")
  
  
  
  main()
  
#imprimer les cubes avec ?
def main():
  print_row(4)
  
 
def print_row(width):
  print("?" * width):
    
   
main()


#imprimer les gros cubes 3x3

def main():
  print_square(3)
  
def print_square(size):
  # For each row in square
  for i in range(size):
    # For each brick in roww
    for j in range(size):
      # Print brick
      print("#", end="")
    print()
main()

# pourrais utiliser ceci
def print_square(size):
  for i in range(size):
    print_row(size)
    
def print_row(width):
  print("#" * width)
  
main()
