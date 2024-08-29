item = 0
stack = []

#Able to add to the stack
#Able to pop something from the stack
#Able to limit the size of the stack to 5 

print("STACK")
option = int(input("""1: Push
2: Pop
3: Print Stack 
4: Exit
  """))
while option != 4:
  if option == 1 and len(stack) < 5:
      while True:
        item = input("""Enter item to push:
        Enter Q to quit.
        """)
        if item.upper() == "Q":
          break
        while len(stack) < 5:
         stack.append(item)
  elif option == 1 and len(stack) >= 5:
      print("""
      Stack is full""")

  elif option == 2 and len(stack) > 0:
      item = stack.pop()
      print("Popped item: ", item)
  elif option == 2 and len(stack) == 0:
      print("Stack is empty")
  elif option == 3:
        for i in range(len(stack)-1,-1,-1):
          print("")
          print("The current stack:")
          print(stack[i])
          print("")


  option = int(input("""
1: Push
2: Pop
3: Print Stack 
4: Exit
"""))
print("Bye, bye.")