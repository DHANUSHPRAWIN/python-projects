#BMI calculator app
import tkinter as tk
import sqlite3

# Initialize the SQLite database
conn = sqlite3.connect('bmi_data.db')
cursor = conn.cursor()

# Create a table for user data (with the category column)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        date TEXT
    )
''')
conn.commit()

# Create a function to calculate BMI and classify it
def calculate_bmi():
    user_name = name_entry.get()
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(text=f'Hello, {user_name}! Your BMI: {bmi:.2f}, Category: {category}')

    # Store the data in the database
    cursor.execute('''
        INSERT INTO user_data (name, weight, height, bmi, category, date)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    ''', (user_name, weight, height, bmi, category))
    conn.commit()

# Create a function to view historical data
def view_data():
    data_window = tk.Toplevel(root)
    data_window.title('Historical Data')

    data_label = tk.Label(data_window, text='Historical BMI Data')
    data_label.pack()

    cursor.execute('SELECT date, bmi, category FROM user_data WHERE name = ?', (name_entry.get(),))
    data = cursor.fetchall()

    for entry in data:
        data_label = tk.Label(data_window, text=f'Date: {entry[0]}, BMI: {entry[1]:.2f}, Category: {entry[2]}')
        data_label.pack()

# Create the main application window
root = tk.Tk()
root.title('BMI Calculator')

name_label = tk.Label(root, text='Your Name:')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

weight_label = tk.Label(root, text='Weight (kg):')
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text='Height (m):')
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text='Calculate BMI', command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

view_button = tk.Button(root, text='View Historical Data', command=view_data)
view_button.pack()

root.mainloop()

# Close the database connection when the application is closed
conn.close()
