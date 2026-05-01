#Week 2, problem set 0, Que 1. Converting camelCase to snake_case.
user_input = input("camelCase: ")

def camel_case(s):
    if s == None or s == "":
        return ("enter valid input")
    else:
        snake = ""
        for i in s:
            if i.islower():
                snake += i
            else:
                snake += "_" + i.lower()
        return snake
def main():
    camel = camel_case(user_input)
    print(camel)

main()