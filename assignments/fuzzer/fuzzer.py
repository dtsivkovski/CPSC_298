import random

def generate_variable():
    return chr(random.randint(97, 122))  # Lowercase letters

def generate_expression():
    if random.random() < 0.3:  # Probability of generating a variable
        return generate_variable()
    elif random.random() < 0.6:  # Probability of generating an abstraction
        var = generate_variable()
        body = generate_expression()
        return ['λ', var, '.', body] 
    else:  # Probability of generating an application
        function = generate_expression()
        argument = generate_expression()
        return ['(', function, argument, ')']

def print_expression(expression):
    for element in expression:
        if isinstance(element, list):
            print_expression(element)  # Recurse for nested structures
        else:
            print(element, end=' ')
    print()

# Example usage
for _ in range(5):  # Generate 5 random expressions
    expression = generate_expression()
    print_expression(expression) 
