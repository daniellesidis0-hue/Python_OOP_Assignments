#Function to check if one number is a multiple of the other
def is_multiple(num1,num2):
    if num1==0 or num2==0:
        return False
    # Check if num1 is a multiple of num2
    if num1%num2==0:
        return True
    # Check if num2 is a multiple of num1
    if num2 % num1 == 0:
        return True
    return False

#Main Program
if __name__ == "__main__":
    print("--- Multipe Check (REPL) ---")
    print("Enter numbers to check, or -1 to exit: ")

    #Infinite Loop
    while True:
        print("\n--- New Check ---")
        val1=int(input("Enter first number: "))

        if val1==-1:
            print("Exiting program. Goodbye!")
            break
        val2=int(input("Enter second number: "))
        
        if val2==-1:
            print("Exiting program. Goodbye!")
            break
        
        #Process Using The Function
        is_match=is_multiple(val1,val2)

        #Print Output Result
        if is_match:
            print("Yes! One of them is a multiple of the other")
        else:
            print("They are not multiples!")
        




            