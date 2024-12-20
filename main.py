from frontend.parser import Parser
import runtime.values
from runtime.environment import Environment
from runtime.interpreter import evaluate
import json

def repl():
    parser = Parser()
    env = Environment(None)

    env.declareVariable("x", runtime.values.NumberValue(100))

    # Instead of having a null literal, we can declare these as variables before runtime
    env.declareVariable("null", runtime.values.NullValue())
    env.declareVariable("None", runtime.values.NullValue())

    env.declareVariable("true", runtime.values.BooleanValue(True))
    env.declareVariable("false", runtime.values.BooleanValue(False))

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
        result = evaluate(program, env)

        # Display the evaluation result in JSON format
        if hasattr(result, "getJSON"):

            with open("interpret.json", "w") as file:
                json.dump(result.getJSON(), file, indent=4)

        else:

            # Fallback to a generic print if result does not have getJSON
            print("Result:")
            print(result)

repl()

################## GOT TO 15:20 ###################################