from django.urls import path


from .views import MessagesListView, MessageCreateView, MessageDetailView, ReactionListView, to_publish, del_reaction, \
    ReactionCreateView

urlpatterns = [
    path('', MessagesListView.as_view(), name='messages_list'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('reaction/', ReactionListView.as_view(), name='reaction_list'),
    path('publish/<int:pk>', to_publish, name='to_publish'),
    path('del_reaction/<int:pk>', del_reaction, name='del_reaction'),
    path('new_reaction/', ReactionCreateView.as_view(), name='reaction_create'),
]
