# we need serializers to convert django format to json to send it over web
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User
from ..models import Farm, Product

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FarmSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Farm
        fields = ['id', 'user', 'ime', 'prezime', 'naziv_opg', 'adresa', 'telefon', 'email']

class ProductSerializer(ModelSerializer):
    farm = FarmSerializer(many=False, read_only=True)
    # If you want to include the string representation of the category choice, you could define a method field
    category_display = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'farm', 'name', 'category', 'category_display', 'detail']

    def get_category_display(self, obj):
        return obj.get_category_display()