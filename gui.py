import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Style
from minproject import recommend_movies,similarity_matrix

# Function to recommend a movie based on genre selection
def recommend_movie():
     movie = movie_entry.get()
     recommendation = recommend_movies(int(movie),similarity_matrix)
     movie_list.config(text="\n".join(recommendation))


# Create the main window
window = tk.Tk()
window.title("Movie Recommendation")
window.geometry("900x600")
window.resizable(False, False)

# Create a style for a modern look
style = Style()
style.configure("TButton",
                font=("Segoe UI", 12),
                padding=10)

style.configure("TLabel",
                font=("Segoe UI", 12))

# Create a label and entry for the input
label = tk.Label(window, text="Enter a number:")
label.pack(pady=10)

movie_entry = tk.Entry(window)
movie_entry.pack()

# Create a button to recommend a movie
recommend_button = tk.Button(window, text="Recommend Movie", command=recommend_movie)
recommend_button.pack()

movie_list_label = tk.Label(window, text="Recommended Movies:", font=("Segoe UI", 12, "bold"))
movie_list_label.pack()

movie_list = tk.Label(window, font=("Segoe UI", 12))
movie_list.pack()

# Run the main event loop
window.mainloop()
