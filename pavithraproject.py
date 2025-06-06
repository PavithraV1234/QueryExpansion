import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.corpus import wordnet

nltk.download("wordnet")
nltk.download("omw-1.4")

def expand_query():
    query = entry.get().strip()
    if not query:
        messagebox.showwarning("Warning", "Please enter a query!")
        return
    
    words = query.split()
    expanded_query = set(words)
    
    for word in words:
        synonyms = wordnet.synsets(word)
        for syn in synonyms:
            for lemma in syn.lemmas():
                expanded_query.add(lemma.name().replace('_', ' '))
    
    result_var.set(", ".join(expanded_query))

root = tk.Tk()
root.title("Query Expansion using WordNet for Synonyms")
root.geometry("500x300")

label = tk.Label(root, text="Enter your query:",font=("Arial", 10, "bold"))
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

expand_button = tk.Button(root, text="Expand Query", command=expand_query)
expand_button.pack(pady=10)

title_label = tk.Label(root, text="Expanded Query:", font=("Arial", 10, "bold"))
title_label.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=5)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_box = tk.Text(frame, height=8, width=50, wrap="word", bg="white", state="disabled", yscrollcommand=scrollbar.set)
result_box.pack()

scrollbar.config(command=result_box.yview)

def update_result():
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result_var.get())
    result_box.config(state="disabled")

result_var = tk.StringVar()
result_var.trace("w", lambda *args: update_result())

root.mainloop()
