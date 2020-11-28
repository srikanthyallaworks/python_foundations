"""

# Lab: Fizz Buzz - Text Edition

## Summary: 

Surprisingly, lots of professional programmers can't really 
code[1]. FizzBuzz is a classic interview question for sussing-out 
the non-skilled. 
                  
Here it is:
    Write a program that prints the numbers from 1 to 100. 
    But--
      * For multiples of 3 print “Fizz” instead of the number 
      * For the multiples of 5 print “Buzz”. 
      * For numbers which are multiples of both 3 and 5 print “FizzBuzz”.

## Requirements
* Implement toText method.
* Write the correct output--described above-- to the console.
* Write specs to document and test.

Notes:
1. https://blog.codinghorror.com/why-cant-programmers-program/

"""



def toText(n):
    divisibleBy3 = n % 3 == 0
    divisibleBy5 = n % 5 == 0
    if divisibleBy3 and divisibleBy5:
        return "fizzbuzz"
    if divisibleBy3:
        return "fizz"
    if divisibleBy5:
        return "buzz"
    return str(n)


def main():
    for i in range(1,101):
        print(toText(i))


if __name__ == "__main__":
    main()


