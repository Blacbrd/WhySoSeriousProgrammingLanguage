from frontend.parser import Parser
import json

def repl():

    parser = Parser()

    print("Repl v0.1")

    while True:
        prompt = input("> ")

        if not prompt:
            print("Ending")
            return
        
        # Need .getJSON otherwise we just print out the program class location rather than what it contains
        program = parser.produceAST(prompt)
        
        formattedProgram = json.dumps(program.getJSON(), indent=4)

        print(formattedProgram)

        with open("ast.json", "w") as file:
            json.dump(program.getJSON(), file, indent=4)

repl()
