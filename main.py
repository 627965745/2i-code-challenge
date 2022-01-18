# 2i code challenge, assume all inputs are positive integers
def main():
  A = int(input("Enter value A: "))
  X = int(input("Enter value X: "))
  for a in range (A, X+1, A):
      print(a)
  for a in range (A, 2*X, A+1):
      print(a)
  for a in range (A, 3*X, A+2):
      print(a)
