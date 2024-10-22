# Debugging Tips

1. Describe the problem
2. Reproduce the bug
3. Pretend youre a computer going through the program
4. Fix the errors
5. Make print statements to see where things are going wrong
6. Use the debugger
   
Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.
Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.
Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.
Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.

7. Take a break
8. Ask a friend to look through the code
9. Run your code often.
10. Everyone gets bugs, it's not embarrasing.