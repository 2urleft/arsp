from tokens import Token, TokenType
import re

KWOP = {
    "func": TokenType.KW_FUNC,
    "if": TokenType.KW_IF,
    "ifelse": TokenType.KW_IFELSE,
    "let": TokenType.KW_LET,
    
    "set": TokenType.OP_SET,
    "incr": TokenType.OP_INCR,
    "decr": TokenType.OP_DECR,
    
    "pls": TokenType.OP_PLUS,
    "mns": TokenType.OP_MINUS,
    "mul": TokenType.OP_MUL,
    "div": TokenType.OP_DIV,
    
    "lt": TokenType.OP_LT,
    "gt": TokenType.OP_GT,
    "le": TokenType.OP_LE,
    "ge": TokenType.OP_GE,
    
    "or": TokenType.OP_OR,
    "and": TokenType.OP_AND,
    "not": TokenType.OP_NOT,
    
    "true": TokenType.T_BOOL,
    "false": TokenType.T_BOOL, # literals
    "lst": TokenType.T_LST, # macro denoting atom
    "nil": TokenType.T_NIL # literal
}

class Lexer():
    def __init__(self, source:str):
        self.source = source
        self.tokens:list[Token] = []
        
    def _add_token(self, ttype, lexeme):
        self.tokens.append(Token(
            ttype, lexeme
        ))
        
    def _process_lexemes(self, lexemes):
        for lexeme in lexemes:
            if lexeme == "(": self._add_token(TokenType.LPAREN, lexeme)
            elif lexeme == ")": self._add_token(TokenType.RPAREN, lexeme)
            elif (KWOPtype := KWOP.get(lexeme, None)):
                self._add_token(KWOPtype, lexeme)
            elif lexeme[0] == ';': continue
            elif lexeme[0] == '"' and lexeme[-1] == '"':
                self._add_token(TokenType.T_STRING, lexeme)
            elif lexeme.isdigit():
                self._add_token(TokenType.T_NUMBER, lexeme)
            else:
                self._add_token(TokenType.IDENT, lexeme)
    
    def lex(self):
        pattern = re.compile(r'''
        (
            "(?:\\.|[^"\\])*"            # Strings
          | ;[^\n]*                      # Comments
          | [-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?  # Numbers
          | [()]                         # Parentheses
          | [^\s()"';]+                  # Symbols
        )
        ''', re.VERBOSE)
        lexemes = pattern.findall(self.source)
        self._process_lexemes(lexemes)