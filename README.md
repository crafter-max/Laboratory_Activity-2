# Laboratory_Activity-2
# Laboratory_Activity-2
# 1. I designed my program in a straight formward manner to avoid compexity, i choose this mainly to improve my readibility in the code while making the class and methods.
# 2. First, after the initialization of the variables, and the methods are ready, the user is prompted for a name of their "ipon challenge" and is stored in a variable called name, and is again asked to pick what function to choose (the option to choose function is within a while loop structure). The method is then called after choosing, and before performing the operation the values received are checked, and only stored or manipulated into the variable its suppose to go if its okay. If an incorrect value is inputted, then an exception error occurs (performed using try-except), specifically;
#   except ValueError:
#        print("Input Error: Please enter a numeric value for days/amounts.")
#   OR   
#   except Exception as e:
#        print(f"An unexpected error occurred: {e}")
# 3. It can receive a lot better oop, and especially error handling like what if special characters are used. Also, it just uses a temporary account stored in a variable which can be improve by storing it in the storage as something accessible, so switching is possible.
