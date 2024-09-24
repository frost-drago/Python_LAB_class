def uni(list_A = [], list_B = []):
    ''' Arguments:
         list_A, list_B : any lists.
        Returns the union of two lists as a list. '''
    return list(set(list_A).union(set(list_B)))

def elongate(pattern, text):
    ''' Arguments:
         pattern    : tuple containing integers. maps the text.
         text       : string. must have the same length as pattern.
        Returns a string, where text[index] is repeated pattern[index] times.
        '''

    # Input filtering
    if len(pattern) != len(text):
        raise ValueError("Mismatch in tuple length and text length")
    
    # Main part of the elongate function
    value = ""
    i = 0
    for character in text:
        value += (character * pattern[i])
        i += 1
    return value

#=======================#
### COPIED CODE START ###
#=======================#
def fibonacci_iterative(n):
  """Calculates the nth Fibonacci number using iteration.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 1:
    return n

  fib_prev = 0
  fib_curr = 1

  for _ in range(2, n+1):
    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next

  return fib_curr

def fibonacci_recursive(n):
  """Calculates the nth Fibonacci number using recursion.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#=======================#
###  COPIED CODE END  ###
#=======================#

# MAIN PROGRAM
try:
    a = [1,3,5]
    b = [1,2,3]
    print(uni(a,b))


    c = (1,2,3,4)
    d = "alex"
    print(elongate(c,d))

except Exception as error_msg:
    print(f"ERROR: {error_msg}")
