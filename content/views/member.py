# DJANGO IMPORTS
from django.views.generic import (
    TemplateView, ListView, DetailView
)
from django.db.models import Sum

# LOCAL IMPORTS
from member.models import Member
from bookkeeping.models import Meal, Expense


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = self.object

        # Get totals (handle None cases)
        total_expense = Expense.objects.aggregate(
            total=Sum('amount')
        )['total'] or 0
        total_meal = Meal.objects.aggregate(
            total=Sum('meal_count')
        )['total'] or 0

        # Calculate meal rate
        meal_rate = round(
            total_expense / total_meal, 3
        ) if total_meal > 0 else 0

        # Get member's meal total
        member_meal_total = Meal.objects.filter(
            member=member
        ).aggregate(total=Sum('meal_count'))['total'] or 0

        # Calculate member's expense
        get_expense = round(
            meal_rate * member_meal_total, 3
        ) if member_meal_total else 0

        context['meal_rate'] = meal_rate
        context['get_expense'] = get_expense
        context['member_meal_total'] = member_meal_total
        context['deposit_amount'] = member.total_deposit_amount
        context['expense_amount'] = get_expense

        return context
