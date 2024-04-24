from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'address',
                  'phone_number',
                  'date_joined',
                  'last_login']
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
            }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)

        if not password:
            raise serializers.ValidationError('Password is required')

        account = self.Meta.model(**validated_data)
        account.set_password(password)
        account.save()

        return account
