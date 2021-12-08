# Wednesday AM

## Agenda
* Housekeeping
  - Polls
  - TODOs outstanding
  - Survey nag
    + https://www.surveymonkey.com/r/WD6DKFM 
  - Review game plan
* Pep talk
  - Kudos
  - Easy day was yesterday
  - When's the spagetti done
* AM Review
* Execute plan


## Game Plan
* Discussion: Comprehensions (Listy)
* Discussion: Exceptions
  - Lab: List Golf (Continued)(?)
* Discuss: Container Potpourri
  - Lab: File fortune
* Discuss: Dictionaries
  - Lab: Dictionary Golf
* Discuss: Functions 'n' Modules
* Discuss: Objects
  - Lab: Dice
* Survey Monkey
* Review Jeopardy



## ToDOs
* Get rid of venv stuff.
* String (immutable) v. list (mutable) review
* Demo linting?
* When to use a class?


## Review (AM)
01. What's the deal with `pass`?
- Create a blank function/class/branch
def no_op():
  pass

class NothingThing:
  pass

02. What's the deal with `range(10,20,2)`?
10..12..14..16..18

03. What's the deal with `if __name__ == '__main__`?
- If I'm being executed directly, do the UI
- If I'm just being imported as a library module, don't do UI stuff


04. What's the deal with `ys = xs[:]` vs `ys = xs[0:len(xs):1]`? 
* Slice to create a duplicate (shallow copy) of x

09. What's the deal with type annotations?

* Set a variable to a specific type
x:bool = True
pi:float = 3.1

* Aka 'type hint'

* No runtime enforcement
* Tools catch errors
  - PyLint
  - PyCharm

* Selling points
  - Clarity of intent
  - Documentation
  - Catch type errors
  - Better intellisence

05. What's the deal with `in`?
* Tests for containment in a container
  - Probably a list

06. What's the deal with `xs += [5]` vs `xs += 'chicken'`?
* Append thing to xs
* Equivalent: xs.extend([5])
  Equivalent: xs.append(5)

07. What's the deal with `print(f'The answer is {37 + 5}!')`?
* Concatening, building up strings
* 'Format string'
* Equivalent
  'The answer is ' + str(37 +5) + '!'

08. What's the deal with _doc strings_?
* Literal string
* Documents
  - function
  - methods
  - classes
  - modules
* Runtime uses this for `help()`
* #this doesn't show up anywhere

10. Wild card: Search for a pattern
* Regex
joe.bloggs@gmail.com
\w+[@]\w+[.](com|org|net)
