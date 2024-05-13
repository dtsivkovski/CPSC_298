# Fuzzer Assignment

The goal for the final assignment was to build a fuzzer that generates random values for lambda calculus and then tests them using the designated functions:

## Functional Methods

- `generate_variable()` - Generates a random char for the lambda calculus
- `generate_expression(max_depth)` - Generates an expression for lambda calculus with a distinct maximum depth for that expression. Continues recursively until depth 0 is reached or random conditions are met
- `stringify_expression(expression)` - Creates a string from an expression.
- `print_expression(expression)` - Prints the expression

## Testing Methods

- `fuzz_lambda_expression(max_depth)` - Creates the stringified lambda expression with a max depth (default 5).
- `test_lambda_function(func, num_tests, max_depth)` - Takes in a specific function for lambda calculus expressions, and proceeds to test it a specific number of times with different expressions.

## Lambda Calculus Methods (for testing the fuzzer)

- `example_lambda_function(expression_string)` - Simply prints out the expression and does nothing further.
- `identity_function(expression_string)` - Interprets the expression with an identity function, simply returning its input.

### Sample Output

```
Invalid lambda expression for identity: b
Invalid lambda expression for identity: λe.λw.λj.w
Invalid lambda expression for identity: λv.λj.λw.((yo)h)
Invalid lambda expression for identity: a
Identity function applied to λx.(λo.λf.(pi)e). Result: (λo.λf.(pi)e)
Invalid lambda expression for identity: λi.λh.λs.λg.(jt)
Invalid lambda expression for identity: λu.λv.(rk)
Invalid lambda expression for identity: t
Invalid lambda expression for identity: λj.λi.(λd.aλw.λe.f)
Invalid lambda expression for identity: h
Invalid lambda expression for identity: λt.λu.p
```