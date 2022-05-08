# Lisp Interpreter

The idea and instruction taken from: [PLC-HW1](https://tinman.cs.gsu.edu/~raj/4330/sp22/hw1/)

When a user writes an input, it first goes to Lexical Analyzer, i.e., LISPLexer, which tokenizes the given string input into a sequence of tokens. Once it's finished with the lexer and no error occurs, the given input string is syntactically correct.

Then, it goes to the parsing stage inside the LISPParser, where it recursively checks whether the given input is semantically correct or not, and if there are no grammatical mistakes, it generates an AST. So, at this stage, we know that the input is syntactically valid.

The AST tree is used for applying functions and operations.

### Available Comparison Operations:
```
(>)  : Greater than
(>=) : Greater than or equal to
(<)  : Less than
(<=) : Less than or equal to
(=)  : Equal to
(<>) : Not equal to
```

### Available Arithmetic Operations:
```
(+)  : Addition
(-)  : Subtraction
(*)  : Multiplication
(/)  : Division
```

### Available Bitwise Operator:
```
and : Logical and operator 
or  : Logical or operator
not : Logical not operator
```

### Available Functions:
```
(cdr List) : 
    input := List
    output := List
    operation:= remove head element of the list

(cons expression List) :
    input := LISP Expression and List
    output := List
    operation:= adds Lisp Expression to the head of the list 
```

Sample Run:
```bash
LISP: (> 3 4);  
False
LISP: (<> 4 5);
True
LISP: (/ 100 25);
4.0
LISP: (or (and true false) (not true)); 
False
LISP: (cons 2 (3 4));  
(2.0 3.0 4.0)
LISP: (cons (+ 2 2) (3 4)); 
(4.0 3.0 4.0)
LISP: (cdr (1 2 3)); 
(2.0 3.0)
```
