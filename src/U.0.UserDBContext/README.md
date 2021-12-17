# UserDBContext

## Summary
After aquiring another company, your HR department needs to import the
new accounts into your database. There's a solution in place, but due to a
resource leak only a few of the new accounts actually get inserted.


## Requirements

### Sprint 0
* Add a `try...finally` block to ensure that connections get closed when the database throws an exception.

### Sprint 1
* Implement the context manager protocol so the database connection can be used inside a [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement).



















## Hints
* Add `__enter__()` and `__exit__` to DBConnection
* There's a good tutorial [here](https://realpython.com/python-with-statement/).
* Read up on typing here:
  - https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager
  - https://docs.python.org/3/library/stdtypes.html#typecontextmanager
  - https://stackoverflow.com/questions/61471700/type-hint-where-one-argument-is-the-type-of-another

https://github.com/python/mypy/blob/4996d571272adde83a3de2689c0147ca1be23f2c/mypy/typeshed/stdlib/contextlib.pyi
https://github.com/python/cpython/blob/3.10/Lib/contextlib.py