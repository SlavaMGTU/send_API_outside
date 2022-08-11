from rest_framework import serializers

from polls.models import Delivary, Message, Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'phone', 'code_phone', 'teg', 'time_zone']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'date_time_send', 'status']

class DelivarySerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = Delivary
        fields = ['id', 'text', 'filter_code', 'filter_teg', 'count_send_yes', 'count_send_no', 'messages']

   def create(self, validated_data):
        # достаем связанные данные для других таблиц
        messages = validated_data.pop('messages')
        # создаем сообщение по его параметрам
        message = super().create(validated_data)
        for message in messages:
            Message.objects.create(message=message, **messages)
        return message

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        messages = validated_data.pop('messages')
        # добавляем рассылку
        message = super().update(instance, validated_data)
        # здесь вам надо обновить связанные таблицы
        for message in messages:
            Message.objects.create(message=message, **messages)
        return message

