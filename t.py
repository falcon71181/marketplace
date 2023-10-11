import random

def rfun(n):
    items = []

    for i in range(1, n):
        item = {
            'id': i,
            'name': random.choice(['Phone', 'Laptop', 'Keyboard']),
            'barcode': ''.join(str(random.randint(0, 9)) for _ in range(12)),
            'price': random.randint(50, 1000)
        }
        items.append(item)
    return items
