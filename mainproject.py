import tkinter as tk

# Example resistor values for a 6 V supply.
# Assumes Vf = 2 V red, 3.2 V green/blue.
# Check your LED's specifications before wiring.
resistors = {
    "Blue":   ("Off", "Off", "300 Ω"),
    "Green":  ("Off", "300 Ω", "Off"),
    "Yellow": ("430 Ω", "300 Ω", "Off"),
    "Red":    ("430 Ω", "Off", "Off"),
    "Pink":   ("430 Ω", "1,500 Ω", "680 Ω"),
    "Purple": ("820 Ω", "Off", "300 Ω"),
}


def show_resistors(color):
    red, green, blue = resistors[color]

    result.config(
        text=f"{color} LED — 6 V supply\n\n"
             f"Red channel: {red}\n"
             f"Green channel: {green}\n"
             f"Blue channel: {blue}"
    )

    preview.config(bg=color.lower())


# Create the window.
window = tk.Tk()
window.title("RGB LED Color Selector")
window.geometry("440x470")

heading = tk.Label(
    window,
    text="Choose your LED color",
    font=("Arial", 18)
)
heading.pack(pady=15)

# Create a button for each color.
button_frame = tk.Frame(window)
button_frame.pack()

for index, color in enumerate(resistors):
    button = tk.Button(
        button_frame,
        text=color,
        width=10,
        command=lambda selected=color: show_resistors(selected)
    )
    button.grid(
        row=index // 3,
        column=index % 3,
        padx=5,
        pady=5
    )

preview = tk.Label(window, text="Color preview", width=20, height=3)
preview.pack(pady=15)

result = tk.Label(
    window,
    text="Click a color to see its resistor values.",
    font=("Arial", 13)
)
result.pack(pady=10)

note = tk.Label(
    window,
    text="Example values for a 6V power supply; check your LED specifications.\n"
         "Mixed colors and the preview are approximate.\n"
         "Off means disconnected. Use one resistor per active channel.",
    wraplength=400
)
note.pack(pady=15)

# Keep the window open and respond to clicks.
window.mainloop()