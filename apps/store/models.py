from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[
            MinValueValidator(1),
        ]
    )
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(to=Collection, on_delete=models.PROTECT, related_name='products')
    # Collection -> Parent model
    # Product -> Child model
    # Many Products to One Collection or One Collection has Many Products
    promotions = models.ManyToManyField(to=Promotion, related_name='products')  
    # If not related_name, default will be 'product_set'

    def __str__(self) -> str:
        return f'{self.title} - {self.description}'

class Customer(models.Model):
    class MembershipChoices(models.TextChoices):
        BRONZE = 'B', _('Bronze')
        SILVER = 'S', _('Silver')
        GOLD = 'G', _('Gold')

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MembershipChoices, default=MembershipChoices.BRONZE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(to=Customer, on_delete=models.CASCADE, primary_key=True)


class Order(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = 'P', _('Pending')
        COMPLETE = 'C', _('Complete')
        FAILED = 'F', _('Failed')

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PaymentStatusChoices, default=PaymentStatusChoices.PENDING)
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT, related_name='orders')


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT, related_name='order_items')
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField()
