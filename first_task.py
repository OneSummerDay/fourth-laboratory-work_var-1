import tkinter as tk

def convert_weight():
    try:
        weight_in_kg = float(entry.get())

        weight_in_grams = weight_in_kg * 1000
        weight_in_pounds = weight_in_kg * 2.20462
        weight_in_ounces = weight_in_kg * 35.274

        result_label.config(text=f"Вага в грамах: {weight_in_grams:.2f}\n"
                                 f"Вага в фунтах: {weight_in_pounds:.2f}\n"
                                 f"Вага в унціях: {weight_in_ounces:.2f}")

    except ValueError:
        result_label.config(text="Будь ласка, введіть коректне число для ваги.")


window = tk.Tk()
window.title("Конвертер ваги")

entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, padx=10, pady=10)

convert_button = tk.Button(window, text="Конвертувати", command=convert_weight)
convert_button.grid(row=1, column=0, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, pady=10)

window.mainloop()
