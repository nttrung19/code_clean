# 1. Whitespace
#
# • Vertical whitespace: Adds whitespace between functions, classes, and code blocks for better readability.
#
# • Horizontal whitespace: Adjusts the whitespace between operators and elements in statements.


def my_function(x, y):
    return x + y


# 2. Function and method calls
#
# • Split parameters in a function or method call into multiple lines if they are too long.
#
# • Ensures that parameters are neatly formatted and easy to read.


def my_function(*args):
    return sum(args)


first_parameter, second_parameter, third_parameter, fourth_parameter = (1, 2, 3, 4)

result = my_function(
    first_parameter, second_parameter, third_parameter, fourth_parameter
)


# 3. Conditional structures
#
# • Format conditional blocks (if, else, elif) to ensure that they follow a consistent style.
#
# • Adjusts the whitespace and indentation of blocks within conditional structures.

if 1 == 2:
    print("Equal")
else:
    print("Not Equal")


class MyClass:
    def method(self):
        print("Method")


# 4. Data types
#
# • Format lists, tuples, and dictionaries so that their elements are organized and easy to read.

my_list = [1, 2, 3, 4, 5]
my_dict = {"key1": "value1", "key2": "value2"}


# 5. Strings and Text
#
# • Make sure that line length does not exceed the limit (default is 88 characters, can be changed).

print(
    "This is a very long line that will exceed the 88-character limit, and it needs to be broken down."
)
