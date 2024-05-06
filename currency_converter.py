import tkinter as tk


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]['rate']
        amount = round(amount * self.rates[to_currency]['rate'], 2)
        return amount


# Курсы валют (относительно USD) с полными названиями
rates = {
    'USD': {'name': 'Доллар США', 'rate': 1},
    'EUR': {'name': 'Евро', 'rate': 0.92827},
    'JPY': {'name': 'Японская йена', 'rate': 153.79},
    'GBP': {'name': 'Фунт стерлингов', 'rate': 0.79523},
    'KZT': {'name': 'Казахстанский тенге', 'rate': 439.50},
    'UAH': {'name': 'Украинская гривна', 'rate': 39.29},
    'AUD': {'name': 'Австралийский доллар', 'rate': 1.51},
    'CAD': {'name': 'Канадский доллар', 'rate': 1.37},
    'CHF': {'name': 'Швейцарский франк', 'rate': 0.9053},
    'CNY': {'name': 'Китайский юань', 'rate': 7.21},
    'HKD': {'name': 'Гонконгский доллар', 'rate': 7.82},
    'NZD': {'name': 'Новозеландский доллар', 'rate': 1.66},
    'RUB': {'name': 'Русский рубль', 'rate': 91.31},
    'TRY': {'name': 'Турецкая лира', 'rate': 8.50},
    'BRL': {'name': 'Бразильский реал', 'rate': 5.07},
    'SGD': {'name': 'Сингапурский доллар', 'rate': 1.35},
    'RON': {'name': 'Румынский лей', 'rate': 4.62}
}


def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    converter = CurrencyConverter(rates)
    converted_amount = converter.convert(amount, from_currency, to_currency)

    result_label.config(
        text=f"{amount} {rates[from_currency]['name']} = {converted_amount} {rates[to_currency]['name']}")

# Создание главного окна
root = tk.Tk()
root.title("Конвертер валют")

# Создание и настройка виджетов
amount_label = tk.Label(root, text="Сумма:")
amount_label.grid(row=0, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

from_currency_label = tk.Label(root, text="Из валюты:")
from_currency_label.grid(row=1, column=0)

from_currency_var = tk.StringVar(root)
from_currency_var.set("USD")
from_currency_menu = tk.OptionMenu(root, from_currency_var, *rates.keys())
from_currency_menu.grid(row=1, column=1)

to_currency_label = tk.Label(root, text="К валюте:")
to_currency_label.grid(row=2, column=0)

to_currency_var = tk.StringVar(root)
to_currency_var.set("EUR")
to_currency_menu = tk.OptionMenu(root, to_currency_var, *rates.keys())
to_currency_menu.grid(row=2, column=1)

convert_button = tk.Button(root, text="Перевести", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Запуск главного цикла обработки событий
root.mainloop()
