from rest_framework import serializers
from .models import Programsdir

class ProgramsdirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programsdir
        fields = '__all__'