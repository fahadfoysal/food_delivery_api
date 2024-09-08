from django.db import models

class Resturant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.location})"

class Category(models.Model):
    name = models.CharField(max_length=50)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f"{self.name} ({self.resturant.name})"
    
class Menu(models.Model):
    name = models.CharField(max_length=50)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return f"{self.name} ({self.resturant.name})"
    
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} - {self.menu.name}"
    
class Modifier(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='modifiers')

    def __str__(self):
        return f"{self.name} ({self.price})"
    
class Order(models.Model):
    PAYMENT_CHOICES = (
        ('card', 'Card'),
        ('cash', 'Cash'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(Item, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cash')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    modifiers = models.ManyToManyField(Modifier, blank=True)

    def __str__(self):
        return f"{self.item.name} x{self.quantity} for Order #{self.order.id}"