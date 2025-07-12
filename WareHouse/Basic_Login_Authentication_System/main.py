'''
Tkinter GUI for login system
Provides interface for registration and authentication
'''
import tkinter as tk
from tkinter import messagebox, ttk
import requests
import threading
class LoginWindow(tk.Tk):
    '''Main login window'''
    def __init__(self):
        super().__init__()
        self.title('Login System')
        self.geometry('300x200')
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.create_widgets()
        self.start_flask_server()
    def create_widgets(self):
        '''Create GUI components'''
        ttk.Label(self, text='Username:').pack(pady=5)
        ttk.Entry(self, textvariable=self.username).pack()
        ttk.Label(self, text='Password:').pack(pady=5)
        ttk.Entry(self, textvariable=self.password, show='*').pack()
        ttk.Button(self, text='Login', command=self.submit_login).pack(pady=10)
        ttk.Button(self, text='Register', command=self.open_register).pack()
    def submit_login(self):
        '''Handle login submission in background thread'''
        threading.Thread(target=self._submit_login, daemon=True).start()
    def _submit_login(self):
        '''Send login request to Flask backend'''
        try:
            response = requests.post(
                'http://localhost:5000/login',
                json={
                    'username': self.username.get(),
                    'password': self.password.get()
                },
                timeout=5
            )
            self.after(0, self.show_result, response.json())
        except Exception as e:
            self.after(0, messagebox.showerror, 'Error', f'Connection failed: {str(e)}')
    def open_register(self):
        '''Open registration window'''
        RegisterWindow(self)
    def show_result(self, result):
        '''Show login result'''
        if result.get('success'):
            messagebox.showinfo('Success', result['message'])
            self.dashboard()
        else:
            messagebox.showerror('Error', result['message'])
    def dashboard(self):
        '''Show simple dashboard window'''
        top = tk.Toplevel(self)
        top.title('Dashboard')
        tk.Label(top, text='Welcome to the Dashboard!').pack(padx=20, pady=20)
    def start_flask_server(self):
        '''Start Flask server in background thread with error handling'''
        def run():
            from app import app
            try:
                app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
            except OSError as e:
                self.after(0, messagebox.showerror, 'Server Error', 
                          f'Port 5000 unavailable: {str(e)}')
        threading.Thread(target=run, daemon=True).start()
class RegisterWindow(tk.Toplevel):
    '''Registration window'''
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Register')
        self.geometry('300x200')
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        '''Create registration components'''
        ttk.Label(self, text='Username:').pack(pady=5)
        ttk.Entry(self, textvariable=self.username).pack()
        ttk.Label(self, text='Password:').pack(pady=5)
        ttk.Entry(self, textvariable=self.password, show='*').pack()
        ttk.Button(self, text='Register', command=self.submit_register).pack(pady=10)
    def submit_register(self):
        '''Handle registration submission in background thread'''
        threading.Thread(target=self._submit_register, daemon=True).start()
    def _submit_register(self):
        '''Send registration request to Flask backend'''
        try:
            response = requests.post(
                'http://localhost:5000/register',
                json={
                    'username': self.username.get(),
                    'password': self.password.get()
                },
                timeout=5
            )
            self.after(0, self.show_result, response.json())
        except Exception as e:
            self.after(0, messagebox.showerror, 'Error', f'Connection failed: {str(e)}')
    def show_result(self, result):
        '''Show registration result'''
        if result.get('success'):
            messagebox.showinfo('Success', result['message'])
            self.destroy()
        else:
            messagebox.showerror('Error', result['message'])
if __name__ == '__main__':
    window = LoginWindow()
    window.mainloop()