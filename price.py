# При создания обьектов класса Price просьба использовать сокращение валют
# такие как предлагаются в таблице на сайте https://bank.gov.ua/ua/markets/exchangerates
# обьязательно верхний регистр
# так же не предусмотрено если если обьект класса rice будет в гривнах(лень писать исключения)

import requests
from bs4 import BeautifulSoup

# функция уменьшает количество чисел после запятой в float
def toFixed(numObj, digits=2):
    return float(f"{numObj:.{digits}f}")

# Парсер который берет текущий курс валют тносительно гривны из сайта
url = "https://bank.gov.ua/ua/markets/exchangerates"

data = requests.get(url)

text_from_site = data.text

bs_text_from_site = BeautifulSoup(text_from_site, "html.parser")

name_valut = bs_text_from_site.find_all(attrs={"data-label": "Код літерний"})
course = bs_text_from_site.find_all(attrs={"data-label": "Офіційний курс"})

# переобразовывает тип всех элементов course из str в float
exchange_rates = []

for course_element in course:
    exchange_rate_str = (
        course_element.text.strip()
    )  # Get the text and remove leading/trailing whitespace
    exchange_rate_float = float(
        exchange_rate_str.replace(",", ".")
    )  # Replace ',' with '.' and convert to float
    exchange_rates.append(exchange_rate_float)


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def __str__(self):
        return "{0} {1}".format(self.amount, self.currency)

    # конвертирует валюты
    # по скольку я использывал курс относительно гривны то снчала я конвертирую в гривны
    # после конвертирую в USD
    # альтернативный вариант, можно было не присваивать amount и currency сразу в self а лишь сделать
    # принты, или ретерн конвертируемой валюты в USD но сделал таким образом что бы легче было
    # перегрузить оператор
    def convert(self):
        i = 0
        if self.currency != "USD":
            for el in name_valut:
                if el.text == self.currency:
                    try:
                        grn = self.amount / exchange_rates[i]

                        self.amount = grn / exchange_rates[7]

                        self.amount = toFixed(self.amount)
                        self.currency = "USD"
                        return self
                    except:
                        print("Ошибка переобраз0вания типов")
                        exit(2)
                i += 1
        else:
            return None

    # перегрузка оператора для класса
    # так же оператор конвертирует валюты которые не были доларами США(USD), поэтому после использования метода и повторного
    # принта слагаемых они уже будут конертированы в USD
    def __add__(self, other):
        if isinstance(other, Price):
            if self.currency == "USD" and other.currency == "USD":
                res = self.amount + other.amount
                return "{0} {1}".format(res, self.currency)
            elif self.currency == "USD" and other.currency != "USD":
                other.convert()
                res = self.amount + other.amount
                return "{0} {1}".format(res, self.currency)
            elif self.currency != "USD" and other.currency == "USD":
                self.convert()
                res = self.amount + other.amount
                return "{0} {1}".format(res, self.currency)
            else:
                self.convert()
                other.convert()
                res = self.amount + other.amount
                return "{0} {1}".format(res, self.currency)
        else:
            print("объект other не является объектом класса Price")
            exit(3)

a1 = Price(100, "DKK")
a2 = Price(100, "HKD")
a3 = Price(500,"RUB")

print(a3.convert())