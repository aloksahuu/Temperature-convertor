import tkinter as tk

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Create Fahrenheit to Celsius frame
f_to_c_frame = tk.Frame(root)
f_to_c_frame.pack(pady=10)

fahrenheit_label = tk.Label(f_to_c_frame, text="Fahrenheit:")
fahrenheit_label.grid(row=0, column=0)

fahrenheit_entry = tk.Entry(f_to_c_frame)
fahrenheit_entry.grid(row=0, column=1)

f_to_c_button = tk.Button(f_to_c_frame, text="Convert", command=fahrenheit_to_celsius)
f_to_c_button.grid(row=0, column=2)

# Create Celsius to Fahrenheit frame
c_to_f_frame = tk.Frame(root)
c_to_f_frame.pack(pady=10)

celsius_label = tk.Label(c_to_f_frame, text="Celsius:")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(c_to_f_frame)
celsius_entry.grid(row=0, column=1)

c_to_f_button = tk.Button(c_to_f_frame, text="Convert", command=celsius_to_fahrenheit)
c_to_f_button.grid(row=0, column=2)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
