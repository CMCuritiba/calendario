from rest_framework import serializers
from .objects import Calendario

class CalendarioSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	start = serializers.DateTimeField()
	end = serializers.DateTimeField()
	url = serializers.CharField(max_length=40)
	title = serializers.CharField(max_length=500)
	setor = serializers.IntegerField(read_only=True)
	pessoa = serializers.IntegerField(read_only=True)
	cclass = serializers.CharField(max_length=60)

	def create(self, validated_data):
		return Calendario(id=None, **validated_data)

	def update(self, instance, validated_data):
		for field, value in validated_data.items():
			setattr(instance, field, value)
		return instance
