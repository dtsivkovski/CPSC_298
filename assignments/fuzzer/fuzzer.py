import random
import string

# --- Lambda Calculus Expression Generator ---

def generate_variable():
    return chr(random.randint(97, 122))

def generate_expression(max_depth=5):
    if max_depth == 0 or random.random() < 0.3:  # Base case or probability of variable
        return generate_variable()
    elif random.random() < 0.6:  # Abstraction
        var = generate_variable()
        body = generate_expression(max_depth - 1)
        return ["λ", var, ".", body]
    else:  # Application
        function = generate_expression(max_depth - 1)
        argument = generate_expression(max_depth - 1)
        return ["(", function, argument, ")"]

def stringify_expression(expression):
    if isinstance(expression, str):
        return expression
    else:
        return "".join(stringify_expression(e) for e in expression)
   
def print_expression(expression):
    for element in expression:
        if isinstance(element, list):
            print_expression(element) 
        else:
            print(element, end='')
    print()


# --- Fuzz Testing with Lambda Calculus ---

def fuzz_lambda_expression(max_depth=5):
    return stringify_expression(generate_expression(max_depth))


def test_lambda_function(func, num_tests=100, max_depth=5):
    """Test a function that processes lambda calculus expressions."""
    for _ in range(num_tests):
        expr = fuzz_lambda_expression(max_depth)
        try:
            func(expr)
        except Exception as e:
            print(f"Error caught for expression '{expr}': {e}")


# --- Example Function to Test (Modify as needed) ---

def example_lambda_function(expression_string):
    """This is a placeholder. You'd replace this with your actual lambda 
       calculus interpreter or function that needs testing."""
    print(f"Processing expression: {expression_string}")
    # ... (Your actual lambda calculus processing logic here) ...
 
def identity_function(expression_string):
    """Lambda calculus identity function interpreter."""

    # Very basic parsing (just to illustrate)
    if expression_string.startswith("λx."):
        body = expression_string[3:]
        if body == "x":
            print(f"Identity function applied to {expression_string}. Result: x")
        else:
            print(f"Identity function applied to {expression_string}. Result: {body}")
    else:
        print(f"Invalid lambda expression for identity: {expression_string}")


# --- Main Execution ---

if __name__ == "__main__":
    # Test the example function (or your real function)
    test_lambda_function(identity_function) # testing with identity function
