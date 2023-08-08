add = lambda NUM1, NUM2: NUM1 + NUM2

mul = lambda NUM1, NUM2: NUM1 * NUM2

div = lambda NUM1, NUM2: NUM1 // NUM2

diff = lambda NUM1, NUM2: NUM1 - NUM2

def main():
    while True:
        input_str = input()
        values = input_str.split()
        
        num1 = int (values[0])
        op   = values[1]
        num2 = int (values[2])
        
        match op:
            case "+":
                print("=",add(num1, num2))

            case "-":
                print("=",diff(num1, num2))
                
            case "x":
                print("=",mul(num1, num2))

            case "/":
                print("=",div(num1, num2))
                
if __name__== "__main__":
    main()
    


                
                
        