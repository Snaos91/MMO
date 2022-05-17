from django.forms import ModelForm
from .models import Message, Reaction


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['category', 'title', 'content', ]


class ReactionForm(ModelForm):
    class Meta:
        model = Reaction
        fields = ['text']
