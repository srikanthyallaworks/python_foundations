# UserDBContext

## Summary
After aquiring another company, your HR department needs to import the
new accounts into your database. There's a solution in place, but due to a
resource leak only a few of the new accounts actually get inserted.


## Requirements

### Sprint 0
* Add a `try...finally` block to ensure that connections get closed when the database throws an exception.

### Sprint 1
* Implement a context manager so the database connection can be used inside a [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement).



















## Hints
* Add `__enter__()` and `__exit__` to DBConnection
* There's a good tutorial [here](https://realpython.com/python-with-statement/).
