from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import MessageForm, ReactionForm
from .models import Message, Reaction


class MessagesListView(ListView):
    model = Message
    template_name = 'messages_list.html'
    context_object_name = 'message'
    queryset = Message.objects.order_by('-created_at')


class MessageCreateView(CreateView):
    permission_required = ('news.message_create',)
    template_name = 'message_create.html'
    form_class = MessageForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(MessageCreateView, self).form_valid(form)


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


class ReactionListView(ListView):
    model = Reaction
    template_name = 'reaction_list.html'
    context_object_name = 'reaction'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(ReactionListView, self).get_context_data(**kwargs)
        context['reaction'] = Reaction.objects.filter(user=user)
        return context


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
