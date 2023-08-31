# Debugging in Visual Studio Code

Debugging is a crucial part of the development process. Visual Studio Code provides powerful debugging tools to help you identify and fix issues in your code. Here's a step-by-step guide to debugging in VS Code:

1. **Open Your Project:**
   Open your project folder in Visual Studio Code.
![Alt text](/images/vs_debug1.png)
2. **Set Breakpoints:**
   In your source code, set breakpoints by clicking in the gutter area next to the line numbers where you want to pause execution.
![Alt text](/images/vs_debug2.png)
![Alt text](/images/vs_debug3.png)
3. **Select Debugger:**
   Click on the Debug icon in the Activity Bar on the side of the window. Make sure you set your breakpoints! If you don't see it, you can also use the keyboard shortcut `Ctrl + Shift + D`.
![Alt text](/images/vs_debug4.png)
4. **Start Debugging:**
   In the Debug sidebar, select the configuration you want to use from the dropdown menu. Click the green play button (▶️) or press `F5` to start debugging.
![Alt text](/images/vs_debug5.png)
![Alt text](/images/vs_debug6.png)
5. **Observe Breakpoints:**
   When your code reaches a breakpoint, it will pause execution, and you can inspect variables, step through code, and analyze the call stack. You can use the controls in the top of the Debug sidebar to navigate through your code.
![Alt text](/images/vs_debug7.png)
6. **Inspect Variables:**
   In the Debug sidebar, you can see the values of variables. Hover over a variable to see its value, and click on it to add it to your Watch list for real-time monitoring.
![Alt text](/images/vs_debug8.png)
7. **Debug Console:**
   The Debug Console at the bottom of the screen allows you to execute commands, evaluate expressions, and print messages for debugging purposes.
![Alt text](/images/vs_debug9.png)
8.  **Step Into:**
    "Step Into" (F11) allows you to move to the next line of code and, if the current line has a function call, it will take you inside that function, allowing you to debug its execution. Notice how we stepped into greetAndSum and then stepped into again into greet which prints 'Hello World!'.
![Alt text](/images/vs_debug10.png)
![Alt text](/images/vs_debug11.png)
9.  **Step Over:**
    "Step Over" (F10) lets you move to the next line of code without diving into function calls. If the current line has a function call, the function will be executed, but the debugger won't take you inside it. Let's start from when we stepped into greetAndSum only this time,  we will **step over** the function greet() and this time **step into** sum.
![Alt text](/images/vs_debug10.png)
![Alt text](/images/vs_debug12.png)
![Alt text](/images/vs_debug13.png)
10. **Continue Execution:**
    To continue execution after a breakpoint or a step, click the green play button in the Debug toolbar or press `F5`.

11. **Stop Debugging:**
    Click the red square stop button (⏹️) in the Debug toolbar or press `Shift + F5` to stop debugging.

12. **Review and Iterate:**
    Use debugging to identify issues, test hypotheses, and improve your code. Iteratively add and adjust breakpoints as needed.

Debugging in Visual Studio Code significantly streamlines the process of finding and fixing errors in your code. By utilizing the debugging tools effectively, you can save time and enhance the quality of your software.

Remember, the exact steps and options might vary based on the programming language and environment you're working with.
