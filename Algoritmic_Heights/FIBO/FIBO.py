from functools import lru_cache

a = int(input())

@lru_cache(maxsize=128) 
def fib(a):
	if a == 0:
		return 0
	if a == 1:
		return 1
	return fib(a - 1) + fib(a - 2)

print(fib(a))