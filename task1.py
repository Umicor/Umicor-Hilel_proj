import functools


# MODIFY THIS DECORATOR
def reverse_string(func):
  """If output is a string, reverse it. Otherwise, return None."""
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    if isinstance(result, str):
      return result[::-1]  # Reverse the string
    else:
      return None
  return wrapper

# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
  return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() -> int:
  return 1957

# TEST OUPUT
print(
  get_university_name(),
  get_university_founding_year(),
  sep="\n"
)