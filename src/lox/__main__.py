from sys import argv
from lox import Lox

def main(args):
    if len(args) > 1:
        raise Exception("Erro")
    elif len(args) == 1:
        Lox.runFile(args[0])
    else:
        Lox.runPrompt()

main(argv[1:])

