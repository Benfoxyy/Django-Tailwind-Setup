from website.models import ProductModel

class CartSession:
    def __init__(self, session):
        self.session = session
        self.cart = self.session.setdefault('cart',
        {
            'items':[],
            'total_price':0,
            'total_items':0,
        })

    def get_cart(self):
        return self.cart

    def get_cart_items(self):
        for item in self.cart['items']:
            prod_obj = ProductModel.objects.get(id=item['product_id'])
            item.update({'prod_obj': prod_obj})
        
        return self.cart['items']

    def add_prod(self, product_id,quantity=None):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                if not quantity:
                    item['quantity'] += 1
                else:
                    item['quantity'] = quantity
                break
        else:
            new_prod = {
                'product_id': product_id,
                'quantity': 1,
            }
            self.cart['items'].append(new_prod)
        self.save()

    def get_cart_quantity(self):
        return sum(int(item['quantity']) for item in self.cart['items'])


    def save(self):
        self.session.modified = True