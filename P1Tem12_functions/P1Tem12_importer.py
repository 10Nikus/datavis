import pandas as pd
from tkinter import filedialog, messagebox

def import_csv():
    """
    Import data from a CSV file using a file dialog.
    Returns a DataFrame if the file is successfully loaded, otherwise returns None.
    """
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return None
        df = pd.read_csv(file_path)
        file_path = file_path[file_path.rfind('/') + 1:] 
        return df, file_path
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return None
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "No data in the file.")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None
    

       