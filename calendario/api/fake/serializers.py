from rest_framework import serializers
from .objects import Calendario

class CalendarioSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	data = serializers.DateTimeField()
	descricao = serializers.CharField(max_length=500)

	def create(self, validated_data):
		return Calendario(id=None, **validated_data)

	def update(self, instance, validated_data):
		for field, value in validated_data.items():
			setattr(instance, field, value)
		return instance
