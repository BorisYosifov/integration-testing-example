import pytest
from product_module import add_product
from order_module import calculate_total_price

# Фикстура за настройка на тестовите данни
@pytest.fixture
def setup_products():
    add_product(1, "Laptop", 1200)
    add_product(2, "Mouse", 20)
    add_product(3, "Keyboard", 100)

# Тест 1: Поръчка без отстъпка
def test_order_without_discount(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60  # Без отстъпка

# Тест 2: Поръчка с няколко продукта
def test_order_with_multiple_products(setup_products):
    order_items = [(1, 1), (2, 2)]  # 1x Laptop (1200) + 2x Mouse (20 * 2 = 40) = 1240
    total_price = calculate_total_price(order_items)
    assert total_price == 1240

# Тест 3: Поръчка с несъществуващ продукт
def test_order_with_invalid_product(setup_products):
    order_items = [(99, 1)]  # Несъществуващ продукт
    total_price = calculate_total_price(order_items)
    assert total_price == 0  # Няма такъв продукт, цената е 0

# Тест 4: Поръчка, за която се прилага 5% отстъпка
def test_order_with_5_percent_discount(setup_products):
    order_items = [(1, 1), (2, 2)]  # 1x Laptop (1200) + 2x Mouse (20 * 2 = 40) = 1240
    total_price = calculate_total_price(order_items)
    expected_price = 1240 * 0.95  # 5% отстъпка
    assert total_price == expected_price, f"Очаквана цена: {expected_price}, получена цена: {total_price}"

# Тест 5: Поръчка, за която се прилага 10% отстъпка
def test_order_with_10_percent_discount(setup_products):
    order_items = [(1, 1), (2, 2), (3, 1)]  # 1x Laptop (1200) + 2x Mouse (20 * 2 = 40) + 1x Keyboard (100) = 1340
    total_price = calculate_total_price(order_items)
    expected_price = 1340 * 0.90  # 10% отстъпка
    assert total_price == expected_price, f"Очаквана цена: {expected_price}, получена цена: {total_price}"

# Тест 6: Поръчка, за която не се прилага отстъпка (цената е под 500)
def test_order_without_discount_low_value(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60  # Без отстъпка (цената е под 500)
