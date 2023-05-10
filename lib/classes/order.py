class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        customer.coffees(coffee)

        #defining price property and setting the price tag
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, price):
        #making sure price is either int or float and also between 1 and 10
        if isinstance(price, int or float) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        # returns customer obj for order which must be of type customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
        
    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, order):
        from classes.order import Order
        if isinstance(order, Order):
            self._order = order
        else:
            raise Exception