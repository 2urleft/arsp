from tokens import Token, TokenType
from lexer import Lexer
from parser import Parser

if __name__ == "__main__":
    with open("simple.arsp", "r", encoding="utf-8") as f:
        lexer = Lexer(f.read())
        lexer.lex()
        
        parser = Parser(lexer.tokens)
        parser.parse()
        print(parser.program_tree)