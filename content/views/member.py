# DJANGO IMPORTS
from django.views.generic import (
    TemplateView, ListView, DetailView
)

# LOCAL IMPORTS
from member.models import Member


class MemberTemplateView(TemplateView):
    template_name = 'content/member.html'


class MemberListView(ListView):
    model = Member
    template_name = 'content/member_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Member.objects.all()
        context['objects'] = queryset
        return context


class MemberDetailsView(DetailView):
    model = Member
    template_name = 'content/member_details.html'
    context_object_name = 'member'
