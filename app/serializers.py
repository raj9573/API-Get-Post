from rest_framework import serializers

from app.models import *



class studentSerializer(serializers.ModelSerializer):

    class Meta:

        model = stud

        fields = '__all__'