#Week 2, problem set 0, Que 4.
#This program checks if a vanity plate is valid or not. The rules for a vanity plate are as follows:
#1. All vanity plates must start with at least two letters.
#2. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
#3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity plate; however, AAA22A would not be acceptable.
#4. The first number used cannot be a '0'.
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = 0
    if s.isalnum() == False:
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    else:
        for p in s:
            if p.isalpha():
                count += 1
                continue
            else:
                continue
        if count<len(s):
            if s[0:count].isalpha() and s[count] != "0":
                    return True
        else:
            if s[0:count].isalpha():
                return True
            else:
                return False


main()
