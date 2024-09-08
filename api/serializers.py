from rest_framework import serializers
from .models import Resturant, Menu, Item, Category, Modifier, Order, OrderItem


class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant
        fields = ['id', 'name', 'location']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'resturant']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'resturant']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'category', 'menu']

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = ['id', 'name', 'price', 'item']

class OrderItemSerializer(serializers.ModelSerializer):
    modifiers = ModifierSerializer(many=True, read_only=True)
    modifiers_ids = serializers.PrimaryKeyRelatedField(queryset=Modifier.objects.all(), many=True, write_only=True, source='modifiers')

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'item', 'quantity', 'modifiers', 'modifiers_ids']

    def create(self, validated_data):
        modifiers = validated_data.pop('modifiers', [])
        order_item = super().create(validated_data)
        order_item.modifiers.set(modifiers)
        return order_item

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    items_data = serializers.ListField(write_only=True, child=serializers.DictField())

    class Meta:
        model = Order
        fields = ['id' , 'resturant', 'items', 'items_data', 'total_price', 'payment_method', 'status', 'created_at']
        read_only_fields = ['id', 'created_at', 'total_price', 'status']

    def create(self, validated_data):
        items_data = validated_data.pop('items_data')
        order = Order.objects.create(**validated_data)

        total_price = 0
        for item_data in items_data:
            item = Item.objects.get(id=item_data['item_id'])
            order_item = OrderItem.objects.create(order=order, item=item, quantity=item_data['quantity'])
            order_item.modifiers.set(item_data.get('modifiers', []))
            total_price += item.price * order_item.quantity
            for modifier in order_item.modifiers.all():
                total_price += modifier.price

        order.total_price = total_price
        order.save()
        return order
