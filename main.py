# Alexandra Floriano - 761771

import sys
sys.path.append('output_dir')
from antlr4 import *
from LAParserLexer import LAParserLexer
from LAParserParser import LAParserParser
from antlr4.error.ErrorListener import ErrorListener


class SyntaxErrorListener(ErrorListener):
    def __init__(self, output_file):
        super().__init__()
        self.output_file = output_file
        self.error_found = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if not self.error_found:
            with open(self.output_file, "w") as file:
                if offendingSymbol.text == '"':
                    file.write(f"Linha {line}: cadeia literal não fechada\n")
                    file.write("Fim da compilacao\n")
                elif offendingSymbol.text == '{':
                    file.write(f"Linha {line}: comentario nao fechado\n")
                    file.write("Fim da compilacao\n")
                elif offendingSymbol.type == LAParserLexer.ErrorChar:
                    file.write(f"Linha {line}: {offendingSymbol.text} - simbolo nao identificado\n")
                    file.write("Fim da compilacao\n")
                else:
                    file.write(f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}\n")
                    file.write("Fim da compilacao\n")
            self.error_found = True

def main(input_file, output_file):
    # Inicializar o analisador léxico e sintático
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = LAParserLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LAParserParser(stream)
    listener = SyntaxErrorListener(output_file)
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    # Chamar a regra inicial da gramática
    tree = parser.program()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python meu_analisador.py <arquivo_de_entrada> <arquivo_de_saída>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
