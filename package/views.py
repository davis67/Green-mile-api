from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .serializers import PackageSerializers, OrderSerializers, InvoiceSerializers
from .models import Package, Order, Invoice
from .renderers import PackageRenderer


class PackagesView(ListCreateAPIView):
    serializer_class = PackageSerializers
    renderer_classes = (PackageRenderer, )
    queryset = Package.objects.all()


class PackageView(RetrieveUpdateDestroyAPIView):
    serializer_class = PackageSerializers

    permission_classes = (permissions.IsAuthenticated,)

    renderer_classes = (PackageRenderer, )

    queryset = Package.objects.all()

    lookup_url_kwarg = "pk"

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = get_object_or_404(queryset, pk = pk)
        return obj


class OrdersView(ListCreateAPIView):
    serializer_class = OrderSerializers
    renderer_classes = (PackageRenderer, )
    queryset = Order.objects.all()


class OrderView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializers

    permission_classes = (permissions.IsAuthenticated,)

    renderer_classes = (PackageRenderer, )

    queryset = Order.objects.all()

    lookup_url_kwarg = "pk"

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = get_object_or_404(queryset, pk = pk)
        return obj

class InvoicesView(ListCreateAPIView):
    serializer_class = InvoiceSerializers
    renderer_classes = (PackageRenderer, )
    queryset = Invoice.objects.all()


class InvoiceView(RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializers

    permission_classes = (permissions.IsAuthenticated,)

    renderer_classes = (PackageRenderer, )

    queryset = Invoice.objects.all()

    lookup_url_kwarg = "pk"

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = get_object_or_404(queryset, pk = pk)
        return obj


