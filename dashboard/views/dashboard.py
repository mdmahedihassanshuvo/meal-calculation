# DJANGO IMPORTS
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

# LOCAL IMPORTS
from member.models import Member
from organogram.models import Group
from bookkeeping.models import Deposit, Expense, Meal


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        user_groups = Group.objects.filter(Member__user=user)

        if user_groups.exists():
            members = Member.objects.filter(groups__in=user_groups).distinct()
            context['show_table'] = True
        else:
            members = Member.objects.none()
            context['show_table'] = False

        context['members'] = members

        deposit_agg = Deposit.objects.aggregate(total=Sum('amount'))
        expense_agg = Expense.objects.aggregate(total=Sum('amount'))
        meal_agg = Meal.objects.aggregate(total=Sum('meal_count'))

        context['total_deposit'] = float(deposit_agg['total']) if deposit_agg['total'] else 0.0 # noqa
        context['total_expense'] = float(expense_agg['total']) if expense_agg['total'] else 0.0 # noqa
        context['total_meal'] = float(meal_agg['total']) if meal_agg['total'] else 0.0 # noqa

        context['member_names'] = [member.name for member in members]
        context['member_deposits'] = [float(member.total_deposit_amount) if member.total_deposit_amount else 0.0 for member in members] # noqa
        context['member_expenses'] = [float(member.total_expense_amount) if member.total_expense_amount else 0.0 for member in members] # noqa
        context['member_meals'] = [float(member.total_meal) if member.total_meal else 0.0 for member in members] # noqa

        return context
