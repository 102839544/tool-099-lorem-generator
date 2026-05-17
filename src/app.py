#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, filedialog

class App:
    def __init__(self, root):
        self.root = root
        root.title("假文生成器 v1.0")
        root.geometry("700x500")
        
        tk.Label(root, text="🔧 假文生成器", font=("Arial", 16, "bold")).pack(pady=50)
        
        tk.Button(root, text="开始使用", command=lambda: messagebox.showinfo("提示", "功能开发中"),
                  bg="#4CAF50", fg="white", padx=30, pady=15).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
