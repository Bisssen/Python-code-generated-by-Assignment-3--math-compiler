# Import external functions (these most be made manually in the external folder)
from .external.power import *

def call():
	print("Expression of dinny2 is: let x be 2 in (x * let x be 10 in (x * x)) + power(10, 2) + let x be 2 in (let x be 3 in (let x be 4 in (x) + x) + x) = " + str((lambda x = 2: x * (lambda x = 10: x * x)())() + power(10, 2) + (lambda x = 2: (lambda x = 3: (lambda x = 4: x)() + x)() + x)()))
