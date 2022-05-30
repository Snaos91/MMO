from django_filters import FilterSet, ModelChoiceFilter
from .models import Message, Reaction


class MessageFilter(FilterSet):
    message_filter = ModelChoiceFilter(
        field_name='message',
        queryset=Message.objects.filter(),
        label='Объявление'
    )

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs
    #     super(ModelChoiceFilter, self).__init__(*args, **kwargs)
    #     choices = Message.objects.filter(related_user=self.user)
    #     self.filters['message'].extra.update(
    #         {
    #             'choices': choices.title
    #         }
    #     )
    #
    #     class Meta:
    #         model = Message
    #         fields = ['title']
