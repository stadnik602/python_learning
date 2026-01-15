"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def notebook():
    return Product("notebook", 50, "This is a notebook", 5000)

@pytest.fixture
def pen():
    return Product("pen", 25, "This is a pen", 10000)

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
        equal_quantity = product.quantity
        assert product.check_quantity(equal_quantity)

        less_quantity = product.quantity - 1
        assert product.check_quantity(less_quantity)

        more_quantity = product.quantity + 1
        assert not product.check_quantity(more_quantity)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        equal_quantity = product.quantity
        product.buy(equal_quantity)
        assert product.quantity == 0, 'failed with equal quantity'

        less_quantity = product.quantity - 1
        product.buy(less_quantity)
        assert product.quantity == 1, 'failed with less quantity'

        more_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            assert product.buy(more_quantity) is ValueError, 'failed with quantity more then stock'

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
    def test_add_product(self, pen, cart):
        cart.add_product(pen, 5)
        assert cart.products[pen] == 5, 'failed with adding to empty cart'

        cart.add_product(pen, 100)
        assert cart.products[pen] == 105, 'failed with adding product to in cart'

    def test_remove_product(self, notebook: Product, cart):
        cart.add_product(notebook, 10)
        cart.remove_product(notebook, 1)
        assert cart.products[notebook] == 9, 'failed with removing product from cart'

        cart.clear()
        cart.add_product(notebook, 5)
        cart.remove_product(notebook)
        assert notebook not in cart.products, 'failed with removing product from cart'

        cart.add_product(notebook, buy_count=100)
        cart.remove_product(notebook, 120)
        print()
        # assert notebook not in cart.products, 'failed with removing product from cart'

    def test_get_total_price(self, product, notebook, pen, cart):
        cart.add_product(product, 1)
        cart.add_product(notebook, 2)
        cart.add_product(pen, 4)
        cart.buy()

        assert cart.get_total_price() == 300, 'total price is not correct'
        assert pen.quantity == 9996, 'failed with getting stock quantity'
        assert notebook.quantity == 4998, 'failed with getting stock quantity'
        assert product.quantity == 999, 'failed with getting stock quantity'

    def test_buy_more_then_available(self, notebook: Product, cart: Cart):
        cart.add_product(notebook, notebook.quantity + 1)
        with pytest.raises(ValueError):
            cart.buy()



