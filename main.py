import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.decisions.simple_decision.comparison_operators as comparison_operators
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.if_ as if_
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function
import basics.modules.guess_the_number as guess_the_number
import basics.output.ascii_art as ascii_art
import basics.output.ascii_robot as ascii_robot
import basics.output.data_types as data_types
import basics.output.escape_characters as escape_characters
import basics.output.review as review
import basics.output.string_operator as string_operator
import basics.output.user_input as user_input


def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "comparison_operators":
        comparison_operators.run()
    elif response == "counter":
        counter.run()
    elif response == "if_":
        if_.run()
    elif response == "if_elif_else":
        if_elif_else.run()
    elif response == "if_else":
        if_else.run()
    elif response == "modulo_operator":
        modulo_operator.run()
    elif response == "ascii_character":
        ascii_character.run()
    elif response == "ascii_code":
        ascii_code.run()
    elif response == "function_calls":
        function_calls.run()
    elif response == "function_with_loop":
        function_with_loop.run()
    elif response == "function_with_nesting":
        function_with_nesting.run()
    elif response == "function_with_parameter":
        function_with_parameter.run()
    elif response == "function_with_parameters":
        function_with_parameters.run()
    elif response == "multiple_functions":
        multiple_functions.run()
    elif response == "return_values":
        return_values.run()
    elif response == "simple_function":
        simple_function.run()
    elif response == "guess_the_number":
        guess_the_number.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "data_types":
        data_types.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "review":
        review.run()
    elif response == "string_operator":
        string_operator.run()
    elif response == "user_input":
        user_input.run()


def run():
    while True:
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")


run()
