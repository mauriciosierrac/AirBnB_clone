# 0x00. AirBnB clone - The console

![Hbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210211T153146Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=607aa513858ddbbed90a251bc932099ed3ff95a3316c4aa0ab7d5396d8831651)


## Resources:books:

Read or watch:
* [Google](https://www.google.com/webhp?q=stack%20and%20queue)
* [How do I use extern to share variables between source files in C?](https://stackoverflow.com/questions/1433204/how-do-i-use-extern-to-share-variables-between-source-files)



---
## Learning Objectives:bulb:
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What do LIFO and FIFO mean
* What is a stack, and when to use it
* What is a queue, and when to use it
* What are the common implementations of stacks and queues
* What are the most common use cases of stacks and queues
* What is the proper way to use global variables

---

### [0. push, pall ](./built_ins.c)
* implement the "push" and "pall" functions.
The push function pushes an element to the stack.
The pall function prints all the values on the stack, starting from the top of the stack.


### [1. pint ](./helpers.c)
* The function pint print the value at the top of the stack, followed by a new line.


### [2. pop ](./built_ins.c)
* The pop function removes the top element of the stack.


### [3. swap ](./built_ins.c)
* The swap function swaps the top two elements of the stack.


### [4. add ](./calculations.c)
* The add function adds the top two elements of the stack.


### [5. nop ](./built_ins.c)
* The nop function doesn't do anything.


---

## How to use it :computer:

### The Monty language

* Monty 0.98 is a scripting language that is first compiled into Monty byte codes (Just like Python). It relies on a unique stack, with specific instructions to manipulate it. The goal of this project is to create an interpreter for Monty ByteCodes files.

### Monty byte code files

Files containing Monty byte codes usually have the .m extension. Most of the industry uses this standard but it is not required by the specification of the language. There is not more than one instruction per line. There can be any number of spaces before or after the opcode and its argument: 

Example monty file 000.m

```
push 0
push 1
push 2
  push 3
                   pall    
push 4
    push 5    
      push    6        
pall

```

---
## Authors :sunglasses:

- Nicolas Herrera C. - https://github.com/nicolasherrerac
- Mauricio Sierra C. - https://github.com/mauriciosierrac
