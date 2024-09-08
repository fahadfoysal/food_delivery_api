from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Resturant, Menu, Item, Category, Modifier, Order, OrderItem
from .serializers import (
    ResturantSerializer,
    MenuSerializer,
    ItemSerializer,
    CategorySerializer,
    ModifierSerializer,
    OrderSerializer,
    OrderItemSerializer,
)
from .permissions import IsOwnerOrEmployee

class ResturantViewSet(viewsets.ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]


class ModifierViewSet(viewsets.ModelViewSet):
    queryset = Modifier.objects.all()
    serializer_class = ModifierSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

