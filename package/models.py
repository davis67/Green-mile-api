from django.db import models
from authentication.models import User

class Package(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    supplier = models.ForeignKey(User, related_name='packages', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255, db_index=True)
    client_email = models.CharField(max_length=255,  db_index=True)
    client_phone_number = models.CharField(max_length=255,  db_index=True)
    client_shippment_address = models.CharField(max_length=255, db_index=True)
    delivery_fee = models.CharField(max_length=255)
    packaging_fee = models.CharField(max_length=255)
    is_delivered = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    date_of_delivery = models.DateTimeField()
    date_of_shipment = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering:["-date_of_delivery"]


class Order(models.Model):
    ORDER_STATUS_OPTIONS = [
    ('PENDING', 'PENDING'),
    ('SHIPPED', 'SHIPPED'),
    ('DELIVERED', 'DELIVERED'),
    ];
    order_id = models.CharField(max_length=255, unique=True, db_index=True)
    status = models.CharField(choices = ORDER_STATUS_OPTIONS, max_length=255)
    package = models.OneToOneField(Package, related_name='order', on_delete=models.CASCADE)
    date_of_payment = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
    INVOICE_PAYMENT_OPTIONS = [
    ('PENDING', 'PENDING'),
    ('PAID', 'PAID'),
    ];
    invoice_id = models.CharField(max_length=255, unique=True, db_index=True)
    status = models.CharField(choices = INVOICE_PAYMENT_OPTIONS, max_length=255)
    order = models.OneToOneField(Order, related_name='invoice', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
