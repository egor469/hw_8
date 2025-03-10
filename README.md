Замечания к первому варианту

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


Замечания ко второму варианту

) В сообщения исключений ValueError можно добавлять product.name -- какого именно продукта не хватает. В логах эта информация может быть полезной.

) def test_product_add_cart(self, product, cart):
with pytest.raises(ValueError, match="Необходимо добавить количество товара"):
cart.add_product(product, 0)

cart.add_product(product, 1)
assert cart.products[product] == 1

cart.add_product(product, 2)
assert cart.products[product] == 3

-- когда у нас разные результаты (исключение и нет), тесты лучше разделять.

) В такого рода юнит-тестах надо проверять и удаление полного добавленного количества там где это проверяется.

Вот я иду в cart.remove_product , и делаю замену

f remove_count is None or remove_count > self.products[product]:

Я убрал = из >= .

Логика поменялась, а тесты "мутацию" не поймали. Значит тестов недостаточно.

) Надо проверить и случай когда в корзине несколько продуктов, а не хватает только одного



