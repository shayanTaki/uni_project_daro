import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# تابع بررسی اعتبار اطلاعات ورود
def check_credentials():
    # دریافت نام کاربری و رمز عبور وارد شده توسط کاربر
    username = username_entry.get()
    password = password_entry.get()

    # خواندن نام کاربری و رمز عبور ذخیره شده از فایل
    with open("credentials.txt", "r") as f:
        saved_username = f.readline().strip().split(": ")[1]
        saved_password = f.readline().strip().split(": ")[1]

    # بررسی درستی اطلاعات ورود
    if username == saved_username and password == saved_password:
        messagebox.showinfo("تایید", "ورود موفق")
        show_text_window()
    else:
        messagebox.showerror("اشتباه میزنی !", "رمز یا نام انبار صحیح نیست ")

# تابع نمایش صفحه ثبت‌نام
def register():
    # تابع ذخیره اطلاعات کاربر
    def save_credentials():
        # دریافت نام کاربری و رمز عبور و تأیید رمز عبور وارد شده توسط کاربر
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        confirm_password = reg_confirm_password_entry.get()

        # بررسی درستی رمز عبور و تأیید رمز عبور
        if password != confirm_password:
            messagebox.showerror("مشکله", "رمزت غلطه")
            return

        # ذخیره نام کاربری و رمز عبور در فایل
        with open("credentials.txt", "w") as f:
            f.write(f"username: {username}\n")
            f.write(f"password: {password}\n")

        # نمایش پیغام موفقیت ثبت‌نام و بستن پنجره ثبت‌نام
        messagebox.showinfo("تایید شد", "ثبت انبار با موفقیت انجام شد")
        register_window.destroy()

    # ایجاد پنجره ثبت‌نام
    register_window = tk.Toplevel(root)
    register_window.title("ایجاد انبار دارو ")
    register_window.geometry("300x200")

    # اضافه کردن المان‌های مربوط به نام کاربری
    ttk.Label(register_window, text="نام انبار دارو:").pack(pady=10)
    reg_username_entry = ttk.Entry(register_window)
    reg_username_entry.pack()

    # اضافه کردن المان‌های مربوط به رمز عبور
    ttk.Label(register_window, text="پسوورد:").pack(pady=10)
    reg_password_entry = ttk.Entry(register_window, show='*')
    reg_password_entry.pack()

    # اضافه کردن المان‌های مربوط به تأیید رمز عبور
    ttk.Label(register_window, text="تکرار پسوورد:").pack(pady=10)
    reg_confirm_password_entry = ttk.Entry(register_window, show='*')
    reg_confirm_password_entry.pack()

    # اضافه کردن دکمه ثبت‌نام
    ttk.Button(register_window, text="ایجاد انبار  :)", command=save_credentials).pack(pady=10)

# تابع نمایش صفحه متن‌ها
def show_text_window():
    # تابع ذخیره متن جدید
    def save_text():
        # دریافت متن وارد شده توسط کاربر
        text = text_entry.get("1.0", tk.END).strip()
        if text:
            # ذخیره متن در فایل
            with open("texts.txt", "a") as f:
                f.write(text + "\n")
            update_text_list()

    def update_text_list():
        text_list.delete(0, tk.END)
        try:
            with open("texts.txt", "r") as f:
                for line in f:
                    text_list.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

    text_window = tk.Toplevel(root)
    text_window.title("دارو ها ")
    text_window.geometry("400x300")

    ttk.Label(text_window, text="نام و مشخصات دارو را وارد کنید").pack(pady=10)
    text_entry = tk.Text(text_window, height=5)
    text_entry.pack()

    ttk.Button(text_window, text="ذخیره", command=save_text).pack(pady=10)

    ttk.Label(text_window, text="دارو های موجود:").pack(pady=10)
    text_list = tk.Listbox(text_window)
    text_list.pack(fill=tk.BOTH, expand=True)

    update_text_list()

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

with open("style.tcl", "r") as f:
    style = f.read()
    root.tk.eval(style)

ttk.Label(root, text="نام انبار:").pack(pady=10)
username_entry = ttk.Entry(root)
username_entry.pack()

ttk.Label(root, text="پسوورد:").pack(pady=10)
password_entry = ttk.Entry(root, show='*')
password_entry.pack()

ttk.Button(root, text="ورود به انبار", command=check_credentials).pack(pady=10)
ttk.Button(root, text="ایجاد انبار", command=register).pack(pady=10)

root.mainloop()
