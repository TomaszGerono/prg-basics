import re

def f(addr):
    # Return True if cell address is valid
    # an address contains 1 or 2 uppercase letter A through ZZ,
    # or lowercase letters a through zz and a row number 1-9999

    pattern = re.compile(r"[A-Za-z]{1,2}\d{1,4}")

    match = pattern.fullmatch(addr)

    if match:
        return True
    
    else:
        return False
    

if __name__ == "__main__":
    print(f("A4")) # True
    print(f("a4")) # True
    print(f("4a")) # False
    print(f("bC123")) # True
    print(f("bcd555")) # False
    print(f("g80915")) # False