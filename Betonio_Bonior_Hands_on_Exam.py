print("*************************************\n"
      "|           W E L C O M E           |\n"
      "*************************************")

choice = str(input("How would you like your decimal value to be converted into?\n"
                   "[1] Binary\n"
                   "[2] Octal\n"
                   "[3] Hexadecimal\n"))

if choice == '1':
    dec_binary = int(input("Enter a decimal value to convert:\n"))
    binary_from_dec = format(dec_binary, "b")
    print(f"The binary value of {dec_binary} is {binary_from_dec}.")
elif choice == '2':
    dec_oct = int(input("Enter a decimal value to convert:\n"))
    oct_from_dec = format(dec_oct, "o")
    print(f"The octal value of {dec_oct} is {oct_from_dec}.")
elif choice == '3':
    dec_hex = int(input("Enter a decimal value to convert:\n"))
    hex_from_dec = format(dec_hex, "x")
    print(f"The hexadecimal value of {dec_hex} is {hex_from_dec}.")
else:
    print("Invalid input. Please try again.")
