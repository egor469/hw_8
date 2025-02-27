"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(0) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(1600) is False
        # assert product.check_quantity(-1) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        total_quantity = product.quantity
        buy_quantity = 123
        product.buy(buy_quantity)
        assert product.quantity == total_quantity - buy_quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_product_add_cart(self, product, cart):
        with pytest.raises(ValueError, match= "Необходимо добавить количество товара"):
            cart.add_product(product, 0)

        cart.add_product(product, 1)
        assert cart.products[product] == 1

        cart.add_product(product, 2)
        assert cart.products[product] == 3

    def test_remove_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 3)
        assert cart.products[product] == 2

    def test_remove_all_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, product, cart):
        cart.add_product(product, 10)
        cart.clear()
        assert product not in cart.products

    def test_get_total_price_empty_cart(self, cart):
        assert cart.get_total_price() == 0

    def test_get_total_price(self,product, cart):
        cart.add_product(product, 10)
        assert cart.get_total_price() == product.price * 10


    def test_cart_buy_more(self, product, cart):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

    def test_cart_buy(self, product, cart):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900

