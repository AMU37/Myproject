import tkinter as tk
from tkinter import messagebox

# إنشاء النافذة الرئيسية
window = tk.Tk()
window.title("برنامج الترحيب")
window.geometry("300x200")

# دالة عند الضغط على الزر
def say_hello():
    name = name_entry.get()
    if name:
        messagebox.showinfo("ترحيب", f"أهلاً بك يا {name}!")
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال الاسم أولاً")

# مكونات الواجهة
label = tk.Label(window, text="أدخل اسمك:")
label.pack(pady=10)

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

greet_button = tk.Button(window, text="تحية", command=say_hello)
greet_button.pack(pady=20)

# تشغيل التطبيق
window.mainloop()
