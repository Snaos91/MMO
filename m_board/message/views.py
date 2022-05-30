from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .filters import MessageFilter
from .forms import MessageForm, ReactionForm, AuthUserForm, RegisterUserForm
from .models import Message, Reaction


class MessagesListView(ListView):
    model = Message
    template_name = 'messages_list.html'
    context_object_name = 'message'
    queryset = Message.objects.order_by('-created_at')


class MessagesPersonalView(ListView):
    model = Message
    template_name = 'message_personal.html'
    context_object_name = 'message'

    def get_queryset(self):
        user = self.request.user
        message = Message.objects.filter(user=user)
        return message


class MessageCreateView(CreateView):
    permission_required = ('news.message_create',)
    template_name = 'message_create.html'
    form_class = MessageForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(MessageCreateView, self).form_valid(form)


class MessageUpdateView(UpdateView):
    permission_required = (PermissionRequiredMixin, 'news.message_update',)
    template_name = 'message_create.html'
    form_class = MessageForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Message.objects.get(pk=id)


class MessageDeleteView(DeleteView):
    template_name = 'message_delete.html'
    queryset = Message.objects.all()
    success_url = '../personal'


class ReactionCreateView(CreateView):
    form_class = ReactionForm
    permission_required = ('news.reaction_create',)
    template_name = 'reaction_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.message_id = self.request.GET.get('id')
        return super(ReactionCreateView, self).form_valid(form)


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(MessageDetailView, self).get_context_data(**kwargs)
        context['reaction'] = Reaction.objects.filter(message=pk, published=True)
        return context


class ReactionView(FilterView):
    model = Reaction
    template_name = 'reaction_list.html'
    context_object_name = 'reaction'
    filterset_class = MessageFilter

    def get_queryset(self):
        user = self.request.user
        messages = Message.objects.filter(user=user)
        qs = Reaction.objects.filter(message__in=messages)
        return qs


def to_publish(request, **kwargs):
    reaction_id = kwargs['pk']
    reaction = Reaction.objects.filter(pk=reaction_id)
    reaction.update(published=True)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def del_reaction(request, **kwargs):
    reaction_id = kwargs['pk']
    reaction = Reaction.objects.filter(pk=reaction_id)
    reaction.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


class BoardLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('messages_list')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(UserCreationForm):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login/')
    success_msg = 'Вы успешно зарегистрировались!'


class BoardLogout(LogoutView):
    next_page = reverse_lazy('')
