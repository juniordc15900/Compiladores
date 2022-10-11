from tokenn import Tokenn
from TokenType import TokenType
from Expr import *

class AstPrinter(ExprVisitor):
    def print(self, expr: Expr):
        return expr.accept(self)

    def parenthesize(self, name: str, *exprs: Expr) -> str:
        content = ' '.join(expr.accept(self) for expr in exprs)

        return f'({name} {content})'

    def visitBinaryExpr(self, expr: Binary) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGroupingExpr(self, expr: Grouping) -> str:
        return self.parenthesize('group', expr.expression)

    def visitLiteralExpr(self, expr: Literal) -> str:
        return str(expr.value)

    def visitUnaryExpr(self, expr: Unary) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)

if __name__ == '__main__':
    exp = Binary(
        Unary(
            Tokenn(TokenType.MINUS, '-', '', 1),
            Literal(123)
        ),
        Tokenn(TokenType.STAR, '*', '', 1),
        Grouping(Literal(45.67))
    )

    printer = AstPrinter()
    print(printer.print(exp))