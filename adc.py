import tkinter as tk
from tkinter import ttk


def adc():
    n = int(n_entry.get())
    AIV = int(AIV_entry.get())
    RV = int(RV_entry.get())

    if n < 0:
        DO_label.config(text="Digital output: 0")
        BDO_label.config(text="Binary digital output: 0")
        return

    if RV == 0:
        DO_label.config(text="Digital output: infinity")
        BDO_label.config(text="Binary digital output: infinity")
        return

    DO = int((2**n) * AIV / RV)
    BDO = str(bin(int(DO)))

    if BDO[0] == "-":
        DO_text = f"Digital output: {DO}"
        BDO_text = f"Binary digital output: -{BDO[3:]}"
    else:
        DO_text = f"Digital output: {DO}"
        BDO_text = f"Binary digital output: {BDO[2:]}"

    DO_label.config(text=DO_text)
    BDO_label.config(text=BDO_text)


root = tk.Tk()
root.title("ADC Simulation")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


n_entry = ttk.Entry(mainframe, width=7)
n_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
AIV_entry = ttk.Entry(mainframe, width=7)
AIV_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
RV_entry = ttk.Entry(mainframe, width=7)
RV_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))


ttk.Label(mainframe, text="Number of bits:").grid(column=1, row=1, sticky=tk.W)
ttk.Label(mainframe, text="Analog input voltage:").grid(column=1, row=2, sticky=tk.W)
ttk.Label(mainframe, text="Reference voltage:").grid(column=1, row=3, sticky=tk.W)


ttk.Button(mainframe, text="Calculate", command=adc).grid(column=2, row=4, sticky=tk.W)


DO_label = ttk.Label(mainframe, text="Digital output: ")
DO_label.grid(column=1, row=5, columnspan=2, sticky=tk.W)
BDO_label = ttk.Label(mainframe, text="Binary digital output: ")
BDO_label.grid(column=1, row=6, columnspan=2, sticky=tk.W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.mainloop()
