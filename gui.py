import tkinter as tk
from analyzer import analyze_password
from wordlist_generator import generate_variants, save_wordlist

def check_password():
    password = entry.get()
    score, feedback = analyze_password(password)
    result_label.config(text=f"Score: {score}/4\n{feedback}")

def generate_list():
    info = info_entry.get()
    words = generate_variants(info.split(","))
    save_wordlist(words)
    result_label.config(text="Wordlist saved to wordlist.txt")

root = tk.Tk()
root.title("Password Tool")

tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Analyze", command=check_password).pack()

tk.Label(root, text="Enter Info (comma separated):").pack()
info_entry = tk.Entry(root)
info_entry.pack()

tk.Button(root, text="Generate Wordlist", command=generate_list).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
