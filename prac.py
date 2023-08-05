def sum(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 // num2

def main():
    print("CALCULATOR")
    print("----------")
    
    num1     = int(input())
    operator = str(input())
    num2     = int(input())
    
    match operator:
        case "+":
            print(sum(num1,num2))
            
        case "-":
            print(sub(num1,num2))
            
        case "x":
            print(mul(num1,num2))
            
        case "/":
            print(div(num1,num2))
            
if __name__ == "__main__":
    main()