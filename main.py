from frontend.parser import Parser
from runtime.interpreter import evaluate
import json

def repl():
    parser = Parser()
    print("Repl v0.1")

    while True:
        prompt = input("> ")

        if not prompt:
            print("Ending")
            return

        # Produce the AST
        program = parser.produceAST(prompt)

        # Display the AST in JSON format
        #print("AST (JSON):")
        #print(json.dumps(program.getJSON(), indent=4))

        with open("ast.json", "w") as file:
            json.dump(program.getJSON(), file, indent=4)

        # Evaluate the program
        result = evaluate(program)

        # Display the evaluation result in JSON format
        if hasattr(result, "getJSON"):

            with open("interpret.json", "w") as file:
                json.dump(result.getJSON(), file, indent=4)

        else:

            # Fallback to a generic print if result does not have getJSON
            print("Result:")
            print(result)

repl()
