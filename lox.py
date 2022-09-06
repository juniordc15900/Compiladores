from scanner import Scanner

def error(line, message):
    report(line, "",message)

def report(line, where, message):
    print(f"[line {line}]\n Error {where} : {message} ")

class Lox:

    def __init__(self,hadError):
        self.hadError = False

    @staticmethod
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.scanTokens()
        for token in tokens:
            print(token)

    @staticmethod
    def runFile(path):
        with open(path,"r",encoding="utf-8") as arq:
            bytes = arq.readlines()
            Lox.run(bytes) #Charset do python
            if Lox.hadError:
                exit()
    @staticmethod
    def runPrompt() -> None:
        
        while True:
            line = input(">>> ")
            if line == None:
                break
            else: 
                Lox.run(line)
                Lox.hadError = False
                
