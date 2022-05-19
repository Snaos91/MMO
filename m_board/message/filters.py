from django_filters import FilterSet, ModelChoiceFilter
from .models import Message, Reaction


class MessageFilter(FilterSet):
    message_filter = ModelChoiceFilter(
        field_name='message_id',
        queryset=Message.objects.filter(),
        label='Объявление'
    )

    class Meta:
        model = Message
        fields = []
