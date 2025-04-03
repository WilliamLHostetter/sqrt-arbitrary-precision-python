'''
Python implementation of the Newton-Raphson method to find square root of an 
input floating point number to an arbitrary precision.
Includes a GUI dialog box to enter the input number and precision. The output is 
displayed in scrollable text box that can be highlighted and copied. 
'''

import tkinter as tk
from tkinter import scrolledtext, messagebox
import decimal
import time



def squareRootNewtonRaphson(input_number, precision_num_digits):
    '''Function to return the square root of a number using Newton-Raphson's method'''
    decimal_precision = precision_num_digits + len(str(int(input_number))) + 1
    decimal.getcontext().prec = decimal_precision
    n = decimal.Decimal(input_number)
    tolerance = decimal.Decimal(10) ** decimal.Decimal(-precision_num_digits)
    # Initial guess of the sqrt(n) as n/2
    estimate = n/decimal.Decimal(2)
    # To count the number of iterations to report in output
    iterations = 0
    while True:
        iterations += 1
        # Calculate closer approximation of root
        root = decimal.Decimal(0.5) * (decimal.Decimal(estimate) + (decimal.Decimal(n) / decimal.Decimal(estimate))) 
        # Check for closeness 
        if (abs(estimate - root) < tolerance):
            break
        # Refine initial estimate 
        estimate = root
    result = round(root, precision_num_digits)
    return result, iterations


def readInputsAndCompute(input_window, input1_var, input2_var):
    input_x_str = input1_var.get()    
    input_precision_n_digits_str = input2_var.get()
    
    try:
        input_number = float(input_x_str)
        assert input_number > 0
        print("Input number =", input_number)
    except Exception :
        error_msg = "Enter a positive number for x"
        messagebox.showerror("Input Error", error_msg)
        return None
    
    try:
        precision_num_digits = int(input_precision_n_digits_str)
        assert precision_num_digits >= 0
        print("Input precision number of digits =", precision_num_digits)
    except Exception :
        error_msg = "Enter a positive integer n for precision"
        messagebox.showerror("Input Error", error_msg)
        return None
    
    start_time = time.perf_counter()
    result, iterations = squareRootNewtonRaphson(input_number, precision_num_digits)
    end_time = time.perf_counter()
    result_str = f"sqrt({input_number}) = {result:.{precision_num_digits}f}"
    iterations_str = f"Number of Iterations = {iterations}"
    print(result_str)

    elapsed_time = end_time - start_time # in seconds
    if elapsed_time >= 1.0:
        elapsed_time_str = f"Computation time = {elapsed_time:.4f} s"
    else:
        elapsed_time_str = f"Computation time = {elapsed_time*1000:.4f} ms"
    print(elapsed_time_str)

    # output results to text window
    results_window = tk.Toplevel(input_window)
    results_window.title("Output")
    scrolledText = scrolledtext.ScrolledText(results_window, width=60, height=8) # width and height units are number of characters
    output_text_str = result_str + "\n\n" + elapsed_time_str + "\n" + iterations_str
    scrolledText.insert(tk.INSERT, output_text_str)
    scrolledText.pack(fill=tk.BOTH, expand=True)
    # Right click menu for copy and select all
    menu = tk.Menu(scrolledText, tearoff=0)
    # Menu options
    menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: scrolledText.event_generate("<<Copy>>"))
    menu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: scrolledText.event_generate("<<SelectAll>>"))
    # Make menu pop up on right click event
    scrolledText.bind("<Button -3>", lambda event: menu.tk_popup(event.x_root, event.y_root))


def main():

    input_window = tk.Tk()
    input_window.title("Input")
    input_window.geometry("400x175")
    input_window.eval('tk::PlaceWindow . center')

    # declaring string variable for storing 2 inputs
    input1_var=tk.StringVar()
    input2_var=tk.StringVar()

    tk.Label(input_window, text="Enter positive floating point number for sqrt()", font=("Segoe UI", 14)).grid(row=0)
    tk.Label(input_window, text="Enter number of digits for precision", font=("Segoe UI", 14)).grid(row=2)
    entry1 = tk.Entry(input_window, font=("Arial",14), textvariable = input1_var)
    entry2 = tk.Entry(input_window, font=("Arial",14), textvariable = input2_var)
    
    input_window.columnconfigure(0, weight=1)
    entry1.grid(row=1, column=0, sticky="nsew", padx=(10,10))
    entry2.grid(row=3, column=0, sticky="nsew", padx=(10,10))

    button = tk.Button(input_window, text="Submit", command=lambda: readInputsAndCompute(input_window, input1_var, input2_var))
    input_window.bind('<Return>', lambda event: readInputsAndCompute(input_window, input1_var, input2_var))
    button.grid(row=5,column=0, pady=(20, 20))

    input_window.mainloop()


if __name__ == "__main__":
    main()
