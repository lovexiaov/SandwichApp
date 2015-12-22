import sys
if sys.version_info < (3, 0):
    import Tkinter as tk
else:
    import tkinter as tk
    
root = tk.Tk()
root.title("Sandwich")
tk.Button(root, text='Make me a sandwich').pack()
tk.mainloop()

    
    