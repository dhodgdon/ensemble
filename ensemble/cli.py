import sys
from .ens_lexer import MusicLexer
from .ens_parser import MusicParser
from .ens_interpreter import MusicInterpreter

def run_ensemble_file(file_path):
    try:
        # Read the content of the Ensemble file
        with open(file_path, 'r') as file:
            code = file.read()

        # Initialize lexer and parser
        lexer = MusicLexer()
        parser = MusicParser()

        # Tokenize and parse the code
        tokens = lexer.tokenize(code)
        # for token in tokens:
        #     print(token)
        ast = parser.parse(tokens)

        # Initialize interpreter and execute the code
        interpreter = MusicInterpreter()
        interpreter.interpret(ast)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print("Error:", e)

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ensemble <file_path>")
        sys.exit(1)

    # Get the file path from the command-line arguments
    file_path = sys.argv[1]

    # Run the Ensemble file
    run_ensemble_file(file_path)

if __name__ == "__main__":
    main()