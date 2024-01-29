inputs = eval(input())
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
  def new_function(*args):
    print(f"You called {function.__name__}{(inputs[0],inputs[1],inputs[2])}\nIt returned: {function(args[0], args[1], args[2])}")
  return new_function

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])