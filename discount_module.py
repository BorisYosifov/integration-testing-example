# discount_module.py

def apply_discount(total_price):
    """
    Приложи отстъпка върху общата цена на поръчката.

    :param total_price: Общата цена на поръчката.
    :return: Общата цена след прилагане на отстъпката.
    """
    if total_price > 1000:
        # 10% отстъпка, ако цената е над 1000
        discount = 0.10
    elif total_price > 500:
        # 5% отстъпка, ако цената е над 500, но не надвишава 1000
        discount = 0.05
    else:
        # Няма отстъпка, ако цената е 500 или по-малко
        discount = 0.00

    # Приложи отстъпката
    discounted_price = total_price * (1 - discount)
    return discounted_price
