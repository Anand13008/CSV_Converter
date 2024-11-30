import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class CSVtoExcelConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV to Excel Converter")

        # Create a button to select CSV file
        self.select_button = tk.Button(master, text="Select CSV File", command=self.select_csv)
        self.select_button.pack(pady=20)

        # Create a button to convert
        self.convert_button = tk.Button(master, text="Convert to Excel", command=self.convert_to_excel)
        self.convert_button.pack(pady=20)

        self.csv_file = None

    def select_csv(self):
        # Open a file dialog to select a CSV file
        self.csv_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.csv_file:
            messagebox.showinfo("Selected File", f"Selected: {self.csv_file}")

    def convert_to_excel(self):
        if self.csv_file:
            # Define the output Excel file name
            excel_file = self.csv_file.rsplit('.', 1)[0] + '.xlsx'
            try:
                # Read the CSV file and write to Excel
                data = pd.read_csv(self.csv_file)
                data.to_excel(excel_file, index=False)
                messagebox.showinfo("Success", f"Converted to: {excel_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("No File Selected", "Please select a CSV file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVtoExcelConverter(root)
    root.mainloop()
