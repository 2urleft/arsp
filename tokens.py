from enum import Enum, auto

class TokenType(Enum):
    # essence
    LPAREN = auto()
    RPAREN = auto()
    IDENT = auto()
    
    # types
    T_STRING = auto()
    T_NUMBER = auto()
    T_BOOL = auto()
    T_LST = auto()
    T_NIL = auto()
    
    # keywords
    KW_FUNC = auto()
    KW_IF = auto()
    KW_IFELSE = auto()
    KW_LET = auto()
    
    # operator
    OP_SET = auto()
    OP_INCR = auto()
    OP_DECR = auto()
    
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    
    OP_LT = auto()
    OP_GT = auto()
    OP_LE = auto()
    OP_GE = auto()
    
    OP_OR = auto()
    OP_AND = auto()
    OP_NOT = auto()
    
    # not a token
    NAT = auto()

class Token():
    def __init__(self, ttype:TokenType, lexeme:str=""):
        self.ttype = ttype
        self.lexeme = lexeme
    