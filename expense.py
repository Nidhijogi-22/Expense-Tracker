from logging import root
import tkinter
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title("Expense Tracker")

tk.Label(root, text="Date (DD/MM/YY):").grid(row=0, column=0, padx=5, pady=5)
date_entry=tk.Entry(root, font=("Arial", 14), width=20)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
amount_entry=tk.Entry(root, font=("Arial", 14), width=20)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Category:").grid(row=2, column=0, padx=5, pady=5)
category_entry=tk.Entry(root, font=("Arial", 14), width=20)
category_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Payment Method:").grid(row=3, column=0, padx=5, pady=5)
payment_entry=tk.Entry(root, font=("Arial", 14), width=20)
payment_entry.grid(row=3, column=1, padx=5, pady=5)

expenses=[]
total_expenses=0
budget=500

columns=("Date", "Amount", "Category", "Payment method")
tree=ttk.Treeview(root, columns=columns, show="headings")
tree.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=350)
    
def get_input():
    global total_expenses

    try:
        date=date_entry.get()
        amount=float(amount_entry.get())
        category=category_entry.get()
        payment=payment_entry.get()

        if not date or not amount or not category or not payment:
            messagebox.showwarning("error", "All labels must be filled")

        # print(f"Date: {date}, Amount: {amount}, Category: {category}, Payment Method: {payment}")

        expenses.append({"Date": date, "Amount": amount, "Category": category, "Payment": payment})

        tree.insert("", "end", values=(date, amount, category, payment))


        total_expenses+=amount
        print(f"Total expenses: {total_expenses}")

        if total_expenses>budget:
           print("Budget Alert!")

        date_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        payment_entry.delete(0, tk.END)

    except:
       messagebox.showerror("Invalid Input") 

button=tk.Button(root, text="Add Expense", command=get_input)
button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
