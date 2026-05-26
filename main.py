from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except:
        messagebox.showerror("Error", "Enter valid numbers")

root = Tk()
root.title("BMI Calculator")
root.geometry("400x400")

Label(root, text="Weight (kg)").pack(pady=10)
weight_entry = Entry(root)
weight_entry.pack()

Label(root, text="Height (m)").pack(pady=10)
height_entry = Entry(root)
height_entry.pack()

Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
).pack(pady=20)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()