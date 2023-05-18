import inspect
import unittest

source_code = inspect.getsource(unittest.result)
print(source_code)
