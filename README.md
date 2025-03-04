) К ValueError стоит добавить полезного сообщения об ошибке, даже можно указать какого товара не хватает.

)

def get_total_price(self) -> float:
total_price = 0
for product, quantity in self.products.items():
total_price = product.price * quantity
return total_price

-- тут, похоже, ошибка, и плохааааая (потому что ошибки на подсчете цены всегда плохие.

) В тестах корзины только один продукт. Чтобы ловить ошибки, надо тестировать корзину минимум с двумя продуктами.

)
def test_product_check_quantity(self, product):
# TODO напишите проверки на метод check_quantity
assert product.check_quantity(500) is True
assert product.check_quantity(1000) is True
assert product.check_quantity(0) is True
assert product.check_quantity(1001) is False
assert product.check_quantity(1600) is False
# assert product.check_quantity(-1) is True

-- в тестировании есть техника граничных значений, применение которой в этом-таком задании, тестовых, будет ожидаться. Стоит с техникой познакомиться.

1000, 1001, 999 - "граничные", а 500 и 1600 -- нет.

)
def test_product_buy_more_than_available(self, product):
# TODO напишите проверки на метод buy,
# которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
pass

-- pass это "заглушка", в наших готовых ДЗ его, как правило, не должно быть.

) Протестировано два случая удаления продукта из корзины.

- с количеством меньше чем добавлено
- без количества

Надо ещё протестировать
- удаляем столько сколько и добавили
- удаляем больше чем добавили (это есть в задании). # hw_8


Замечания к первому варианту