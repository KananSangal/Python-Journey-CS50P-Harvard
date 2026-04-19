# This program reads a mathematical expression from the user and evaluates it based on the operator provided.
exp = input("Expression: ").strip()
x,y,z = exp.split(" ")
match y:
    case "+":
        res = int(x)+int(z)
    case "-":
        res = int(x)-int(z)
    case "*":
        res = int(x)*int(z)
    case "/":
        if z=="0":
            print("Cant divide by zero.")
            exit()
        else:
            res = int(x)/int(z)
print(f"{float(res):.1f}")