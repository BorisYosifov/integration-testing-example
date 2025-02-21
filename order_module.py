# order_module.py

from product_module import get_product
from discount_module import apply_discount  # Импортиране на функцията за отстъпки

def calculate_total_price(order_items):
    """
    Изчислява общата цена на поръчка и прилага отстъпка, ако е необходимо.
    order_items е списък от tuples (product_id, quantity).
    """
    total = 0
    for product_id, quantity in order_items:
        product = get_product(product_id)
        if product:
            total += product["price"] * quantity

    # Приложи отстъпка, ако е необходимо
    total_with_discount = apply_discount(total)
    
    return total_with_discount

