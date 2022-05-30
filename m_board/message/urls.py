from django.urls import path


from .views import MessagesListView, MessageCreateView, MessageDetailView, ReactionView, to_publish, del_reaction, \
    ReactionCreateView, MessageUpdateView, MessagesPersonalView, MessageDeleteView, BoardLoginView, RegisterUserView, \
    LogoutView

urlpatterns = [
    path('register/', RegisterUserView, name='register'),
    path('login/', BoardLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', MessagesListView.as_view(), name='messages_list'),
    path('personal/', MessagesPersonalView.as_view(), name='message_personal'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('create/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('del_message/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('reaction/', ReactionView.as_view(), name='reaction_list'),
    path('publish/<int:pk>', to_publish, name='to_publish'),
    path('del_reaction/<int:pk>', del_reaction, name='del_reaction'),
    path('new_reaction/', ReactionCreateView.as_view(), name='reaction_create'),

]
