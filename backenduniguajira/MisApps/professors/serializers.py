from rest_framework import serializers
from .models import Professors

class ProfessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professors
        fields = '__all__'

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.program = validated_data.get('program', instance.program)
        

        instance.save()
        return instance
