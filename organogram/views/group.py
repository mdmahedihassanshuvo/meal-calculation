# organogram/views/group.py
# DJANGO IMPORTS
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import Group as AuthGroup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404

# LOCAL IMPORTS
from organogram.models import Group
from organogram.forms import GroupForm
from member.models import Member


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'organogram/group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.has_perm('organogram.member_management'):
            return Group.objects.all()
        else:
            member = getattr(user, 'member_profile', None)
            return Group.objects.filter(
                Q(created_by=user) |
                Q(Member=member)
            ).distinct()


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'organogram/group_form.html'
    success_url = reverse_lazy('organogram:group_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)

        try:
            creator_member = get_object_or_404(Member, user=self.request.user)

            form.instance.Member.add(creator_member)

            creator_member.is_manager = True
            creator_member.is_member = False
            creator_member.save()

            manager_group, created = AuthGroup.objects.get_or_create(name='manager') # noqa
            self.request.user.groups.add(manager_group)

            messages.success(self.request, f'Group "{form.instance.group_name}"created successfully!') # noqa

        except Exception as e:
            messages.error(self.request, f'Group created but there was an error: {str(e)}') # noqa

        return response


class GroupMemberListView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'organogram/group_member_list.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.get_object()
        members = group.Member.all()
        context['members'] = members
        return context
