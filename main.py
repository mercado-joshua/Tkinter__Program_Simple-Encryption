#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

from random import choice

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.withdraw()
        self.resizable(True, True)
        self.title('Secret Messages')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        while True:
            task = self.get_task()
            if task == 'encrypt':
                message = self.get_message()
                encrypted = self.encrypt(message)

                mb.showinfo('Ciphertext of the secret message is:', encrypted)
            elif task == 'decrypt':
                message = self.get_message()
                decrypted = self.decrypt(message)
                mb.showinfo('Plaintext of the secret message is:', decrypted)
            else:
                break

    # INSTANCE ---------------------------------
    def get_task(self):
        """Encrypt or decrypt"""
        task = sd.askstring('Task', 'Do you want to encrypt or decrypt?')
        return task

    def get_message(self, ):
        """Get the message"""
        message = sd.askstring('Message', 'Enter the secret message:')
        return message

    def _is_even(self, number):
        return number % 2 == 0

    def get_even_letters(self, message):
        even_letters = []
        for counter in range(0, len(message)):
            if self._is_even(counter):
                even_letters.append(message[counter])
        return even_letters

    def get_odd_letters(self, message):
        odd_letters = []
        for counter in range(0, len(message)):
            if not self._is_even(counter):
                odd_letters.append(message[counter])
        return odd_letters

    def swap_letters(self, message):
        letter_list = []
        if not self._is_even(len(message)):
            message = message + 'x'
        even_letters = self.get_even_letters(message)
        odd_letters = self.get_odd_letters(message)

        for counter in range(0, int(len(message) / 2)):
            letter_list.append(odd_letters[counter])
            letter_list.append(even_letters[counter])

        new_message = ''.join(letter_list)
        return new_message

    def decrypt(self, message):
        even_letters = self.get_even_letters(message)
        new_message = ''.join(even_letters)
        return new_message

    def encrypt(self, message):
        encrypted_list = []
        fake_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'r', 's', 't', 'u', 'v']
        for counter in range(0, len(message)):
            encrypted_list.append(message[counter])
            encrypted_list.append(choice(fake_letters))
        new_message = ''.join(encrypted_list)
        return new_message


#===========================
# Start GUI
#===========================

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()