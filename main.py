# 2i code challenge, assume all inputs are positive integers
# A Python code that iterates in multiples of A until X, then in multiples of A + 1 until 2X, then multiples of A + 2 until 3X.
def main():
  A = int(input("Enter value A: "))
  X = int(input("Enter value X: "))
  for a in range (A, X+1, A):
      print(a)
  for a in range (A+1, 2*X, A+1):
      print(a)
  for a in range (A+2, 3*X, A+2):
      print(a)
