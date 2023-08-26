import functools
# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
  """Replace the value of a dictionary with a 'masked' version."""
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, dict) and target_key in result:
            result[target_key] = replace_with * len(result[target_key])
        return result
    return wrapper

  return decorator

# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
  return {
    "name": name,
    "age": age
  }

# TEST OUPUT
print(
  get_user(name="Alice", age=30),
  get_user(name="Bob", age=25),
  sep="\n"
)