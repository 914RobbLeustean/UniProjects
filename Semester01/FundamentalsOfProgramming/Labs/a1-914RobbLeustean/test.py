def fact (n : int) -> int:
   if n == 0:
      return 1
   return n * fact(n-1)

#print(fact(5))
def fib(n : int ) -> int:
   if n < 2:
      return n
   return fib(n-2) + fib(n-1)

#print(fib(10))

def fib_iter(n : int ) -> int:
   x = 0
   y = 1
   for i in range(n):
      z = x + y
      x = y
      y = z
   return x


#print(fib_iter(10))

def test_fib():
   for i in range(10):
      assert fib(i) == fib_iter(i)