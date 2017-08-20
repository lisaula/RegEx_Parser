from lexer import *
from parser import parse
def main():
    ast = parse("(0+1)*+(1.0)")
    print ("parse completing")
    ast.printable("")
    
if __name__ == "__main__":
    main()
