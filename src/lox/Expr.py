from abc import ABC,abstractmethod
from typing import Any
from tokenn import Tokenn



class ExprVisitor(ABC):

    @abstractmethod
    def visitBinaryExpr(self,expr: 'Expr'):
        pass

    @abstractmethod
    def visitGroupingExpr(self,expr: 'Expr'):
        pass

    @abstractmethod
    def visitUnaryExpr(self,expr: 'Expr'):
        pass

    @abstractmethod
    def visitTernaryExpr(self,expr: 'Expr'):
        pass

    @abstractmethod
    def visitLiteralExpr(self,expr: 'Expr'):
        pass


class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: ExprVisitor):
        pass



class Binary(Expr):
    def __init__(self,left: Expr ,operator: Tokenn ,right: Expr) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor) -> None:
        return visitor.visitBinaryExpr(self)



class Grouping(Expr):
    def __init__(self,expression: Expr) -> None:
        self.expression = expression

    def accept(self, visitor: ExprVisitor) -> None:
        return visitor.visitGroupingExpr(self)



class Unary(Expr):
    def __init__(self,operator: Tokenn,right: Expr) -> None:
        self.operator = operator
        self.right = right

    def accept(self, visitor: ExprVisitor) -> None:
        return visitor.visitUnaryExpr(self)



class Ternary(Expr):
    def __init__(self,condition: Expr,thenCond: Expr,elseCond: Expr) -> None:
        self.condition = condition
        self.thenCond = thenCond
        self.elseCond = elseCond

    def accept(self, visitor: ExprVisitor) -> None:
        return visitor.visitTernaryExpr(self)



class Literal(Expr):
    def __init__(self,value: Any) -> None:
        self.value = value

    def accept(self, visitor: ExprVisitor) -> None:
        return visitor.visitLiteralExpr(self)

