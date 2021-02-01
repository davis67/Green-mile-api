from rest_framework import serializers
from .models import Package, Invoice, Order
from authentication import serializers as users_serializers

class PackageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Package

        fields ="__all__"

    def to_representation(self, instance):
       ret = super().to_representation(instance)
       ret['supplier'] = users_serializers.MemberSerializer(instance.supplier).data
       return ret

class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order

        fields = "__all__"

    def to_representation(self, instance):
       ret = super().to_representation(instance)
       ret['package'] = PackageSerializers(instance.package).data
       return ret


class InvoiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Invoice

        fields = "__all__"

    def to_representation(self, instance):
       ret = super().to_representation(instance)
       ret['order'] = OrderSerializers(instance.order).data
       return ret
