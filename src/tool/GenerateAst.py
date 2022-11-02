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
        self.outputDir = 'src/lox'
        self.defineAst(self.outputDir,"Expr",{"Binary" :"left: Expr ,operator: Tokenn ,right: Expr",
                                          "Grouping":"expression: Expr",
                                           "Unary":"operator: Tokenn,right: Expr",
                                           "Ternary":"condition: Expr,thenCond: Expr,elseCond: Expr",
                                           "Literal":"value: Any"})

   

    def defineAst(self,path:Path,baseName,types):
        name = baseName.title()
        visitor = f'{baseName}Visitor'
        with open(f'{path}/{baseName}.py',mode='w', encoding='utf-8') as arq:
            
            
            arq.write(f'from abc import ABC,abstractmethod')
            arq.write('\n')
            arq.write(f'from typing import Any')
            arq.write('\n')
            arq.write(f'from tokenn import Tokenn')
            arq.write('\n')
            self.defineVisitor(arq,baseName,types) #visitor
            arq.write('\n\n')
            arq.write(f'class {name}(ABC):')
            arq.write('\n')
            arq.write(f'{IDENTATION}@abstractmethod')
            arq.write('\n')
            arq.write(f'{IDENTATION}def accept(self, visitor: {visitor}):')
            arq.write('\n')
            arq.write(f'{IDENTATION*2}pass')
            arq.write('\n\n')
            
            for type in types:
                arq.write('\n')
                className = type
                fields = str(types[type]).split(',')
                self.defineType(arq,baseName,className,fields)
                arq.write('\n')


    def defineVisitor(self,arq,baseName,types):
        name = baseName.lower()
        visitor = f'{baseName}Visitor'
        
        arq.write('\n\n\n')
        arq.write(f"class {visitor}(ABC):") #!!!
        arq.write('\n')
        
        
        for type in types:
            
            arq.write('\n')
            arq.write(f'{IDENTATION}@abstractmethod')
            arq.write('\n')
            arq.write(f'{IDENTATION}')
            arq.write(f"def visit{type.title()}{name.title()}(self,expr: '{baseName}'):")
            arq.write('\n')
            arq.write(f'{IDENTATION*2}pass')
            arq.write('\n')

    def defineType(self,arq,baseName,className,fields):
        
        arq.write('\n')
        arq.write(f"class {className}({baseName}):")
        arq.write('\n')
        arq.write(f'{IDENTATION}')
        
        #construtor
    
        arq.write(f"def __init__(self,{','.join(fields)}) -> None:")
        arq.write('\n')
        
        for field in fields:
            name = field[:field.find(':')]
            arq.write(f"{IDENTATION*2}self.{name} = {name}")
            arq.write('\n')
        
        arq.write('\n')
        arq.write(f'{IDENTATION}')
        arq.write(f'def accept(self, visitor: {baseName}Visitor) -> None:')
        arq.write('\n')
        arq.write(f'{IDENTATION * 2}')
        arq.write(f'return visitor.visit{className}{baseName}(self)')
        arq.write('\n')
            
    
    

    

if __name__ == '__main__':
    generate = GenerateAst()
    generate.main(argv)