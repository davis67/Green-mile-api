from django.urls import path
from .views import PackagesView, PackageView,OrdersView,InvoicesView,OrderView, InvoiceView


urlpatterns = [
    path('packages', PackagesView.as_view(), name = "packages"),
    path('orders', OrdersView.as_view(), name = "orders"),
    path('invoices', InvoicesView.as_view(), name = "invoices"),
    path('packages/<int:pk>', PackageView.as_view(), name = "packages-details"),
    path('orders/<int:pk>', OrderView.as_view(), name = "orders-details"),
    path('invoices/<int:pk>', InvoiceView.as_view(), name = "invoice-details")
]
