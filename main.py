import tkinter as tk
from tkinter import ttk

class FlightTicketCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор стоимости билета на самолет")

        # Переменные для хранения данных пользователя
        self.baggage_var = tk.IntVar()
        self.class_var = tk.StringVar()
        self.total_price_var = tk.StringVar()

        # Создание и размещение элементов управления
        self.label_baggage = ttk.Label(master, text="Выберите опции багажа:")
        self.label_baggage.grid(row=0, column=0, padx=10, pady=10)

        self.baggage_options = [("Без багажа", 0), ("До 20 кг", 20), ("До 30 кг", 30)]
        for option, weight in self.baggage_options:
            ttk.Radiobutton(master, text=option, variable=self.baggage_var, value=weight).grid(row=0, column=self.baggage_options.index((option, weight))+1, padx=5, pady=10)

        self.label_class = ttk.Label(master, text="Выберите класс обслуживания:")
        self.label_class.grid(row=1, column=0, padx=10, pady=10)

        self.class_options = [("Эконом", "Economy"), ("Бизнес", "Business"), ("Первый класс", "First Class")]
        for option, class_type in self.class_options:
            ttk.Radiobutton(master, text=option, variable=self.class_var, value=class_type).grid(row=1, column=self.class_options.index((option, class_type))+1, padx=5, pady=10)

        self.button_calculate = ttk.Button(master, text="Рассчитать", command=self.calculate)
        self.button_calculate.grid(row=2, column=0, columnspan=3, pady=10)

        self.label_result = ttk.Label(master, textvariable=self.total_price_var)
        self.label_result.grid(row=3, column=0, columnspan=3, pady=10)

    def calculate(self):
        # Цены на опции
        baggage_prices = {0: 0, 20: 1500, 30: 3500}
        class_prices = {"Economy": 1000, "Business": 3200, "First Class": 6400}

        # Получение выбранных опций от пользователя
        selected_baggage = self.baggage_var.get()
        selected_class = self.class_var.get()

        # Рассчет общей стоимости билета
        total_price = baggage_prices[selected_baggage] + class_prices[selected_class]

        # Отображение результата
        result_text = f"Общая стоимость билета: {total_price} рублей."
        self.total_price_var.set(result_text)

def main():
    root = tk.Tk()
    app = FlightTicketCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
