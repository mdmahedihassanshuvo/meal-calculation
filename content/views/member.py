# DJANGO IMPORTS
from django.views.generic import (
    ListView, DetailView
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

# LOCAL IMPORTS
from member.models import Member
from bookkeeping.models import Meal, Expense


class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    template_name = 'content/member_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Member.objects.all().exclude(
            is_member=False
        )
        context['objects'] = queryset
        return context


class MemberDetailsView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = 'content/member_details.html'
    context_object_name = 'member'

    def get_object(self, queryset=None):
        user_id = self.request.GET.get('user_id')
        if user_id:
            return get_object_or_404(Member, user__id=user_id)
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = self.object

        total_expense = Expense.objects.aggregate(
            total=Sum('amount')
        )['total'] or 0
        total_meal = Meal.objects.aggregate(
            total=Sum('meal_count')
        )['total'] or 0

        meal_rate = round(
            total_expense / total_meal, 3
        ) if total_meal > 0 else 0

        member_meal_total = Meal.objects.filter(
            member=member
        ).aggregate(total=Sum('meal_count'))['total'] or 0

        get_expense = round(
            meal_rate * member_meal_total, 3
        ) if member_meal_total else 0

        context['meal_rate'] = meal_rate
        context['get_expense'] = get_expense
        context['member_meal_total'] = member_meal_total
        context['deposit_amount'] = member.total_deposit_amount
        context['expense_amount'] = get_expense

        return context
