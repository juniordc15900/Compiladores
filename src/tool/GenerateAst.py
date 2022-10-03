#https://refactoring.guru/pt-br/design-patterns/visitor/python/example
from sys import argv
from pathlib import Path
from argparse import ArgumentParser


IDENTATION = '    '

class GenerateAst():

    def __init__(self):
        self.outputDir = ''

    def main(self,args):
        if (len(args)!=1):
            print('Usage....')
            exit()
        self.outputDir = args[0]
        self.defineAst(self.outputDir,"Expr",{"Binary" :"left: Expr ,operator: Token ,right: Expr",
                                          "Grouping":"expression: Expr",
                                           "Unary":"operator: Token,right: Expr",
                                           "Literal":"value: Any"})


   

    def defineAst(self,path:Path,baseName,types):
        with open(f'{baseName}.py',mode='w', encoding='utf-8') as arq:
            arq.write(f'class {baseName}():')
            arq.write('\n')
            
            self.defineVisitor(arq,baseName,types) #visitor

            for type in types:
                className = type
                fields = str(types[type]).split(',')
                self.defineType(arq,baseName,className,fields)
        

    def defineVisitor(self,arq,baseName,types):
        name = baseName.lower()
        visitor = f'{name}Visitor'
        
        arq.write('\n\n\n')
        arq.write(f"class {visitor}(ABC):") #!!!
        arq.write('\n')
        
        
        for type in types:
            
            arq.write('\n')
            arq.write(f'{IDENTATION}@abstractmethod')
            arq.write('\n')
            arq.write(f'{IDENTATION}')
            arq.write(f'def visit_{type.lower()}_{name}(self,expr: {baseName}):')
            arq.write('\n')
            arq.write(f'{IDENTATION*2}pass')
            arq.write('\n')

    def defineType(self,arq,baseName,className,fields):
        
        arq.write('\n')
        arq.write(f"    class {className}({baseName}):")
        arq.write('\n')
        #construtor
    
        arq.write(f"        def __init__(self,{','.join(fields)}):")
        arq.write('\n')
        arq.write(f"            super().__init__()")
        arq.write('\n')
        for field in fields:
            name = field[:field.find(':')]
            arq.write(f"            self.{name} = {name}")
            arq.write('\n')
            
    
    

    

if __name__ == '__main__':
    generate = GenerateAst()
    generate.main(argv)