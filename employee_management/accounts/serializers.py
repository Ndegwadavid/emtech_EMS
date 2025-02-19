from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Admin
        fields = ('id', 'username', 'email', 'password', 'phone_number')
        
    def create(self, validated_data):
        admin = Admin.objects.create_user(**validated_data)
        return admin
