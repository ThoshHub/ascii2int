# ascii2int

This is a small script that converts english number strings into integers.
For example, if given "four hundred" it will print "400"

__Restrictions__
- This program only works in base 10
- This program cannot handle any number a trillion or above, it is only restricted to one billion and below
- This program does not handle negative integers
- This program accepts American English spelling, but not British English (forty not fourty)
- This program can handle hyphenated strings, for example "forty six" will produce the same output as "forty-six": 46
- This program does not handle commas

__How to run__
This program accepts command line arguments, for example:
> python3 ascii2int forty six
will return a console output of:
> Input:  
> forty six
> Output:
> 46
Quotes for a single argument is not necessary, the program will handle it automatically.

If the user chooses to call the program without any arguments, this program will default to running a built in case. The user may choose the default case by editing the source.

__Running coverage tests__
This project also comes with a tests.py file which can be used to run test cases using coverage.py which will show the code coverage.
The test file can be run with the following command:
> python3 tests.py 
By default, the report will be built in /convhtml of the root directory where the project is located.
