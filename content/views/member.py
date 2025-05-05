# DJANGO IMPORTS
from django.views.generic import TemplateView


class MemberTemplateView(TemplateView):
    template_name = 'content/member.html'
