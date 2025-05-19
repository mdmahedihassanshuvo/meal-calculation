# DJANGO IMPORTS
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

# LOCAL IMPORTS
from member.models import Member
from bookkeeping.models import Deposit, Expense, Meal


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        members = Member.objects.all()
        context['members'] = members

        # Get aggregation results first
        deposit_agg = Deposit.objects.aggregate(total=Sum('amount'))
        expense_agg = Expense.objects.aggregate(total=Sum('amount'))
        meal_agg = Meal.objects.aggregate(total=Sum('meal_count'))

        # Handle None values and convert to float
        context['total_deposit'] = float(
            deposit_agg['total']
        ) if deposit_agg['total'] else 0.0
        context['total_expense'] = float(
            expense_agg['total']
        ) if expense_agg['total'] else 0.0
        context['total_meal'] = float(
            meal_agg['total']
        ) if meal_agg['total'] else 0.0

        context['member_names'] = [member.name for member in members]

        # For member-specific data
        context['member_deposits'] = []
        context['member_expenses'] = []
        context['member_meals'] = []

        for member in members:
            print(f">>>>>>>>>>>>>> expense: {member.total_expense_amount}")
            # Handle possible None values for each member
            context['member_deposits'].append(float(member.total_deposit_amount) if member.total_deposit_amount else 0.0) # noqa
            context['member_expenses'].append(float(member.total_expense_amount) if member.total_expense_amount else 0.0) # noqa
            context['member_meals'].append(float(member.total_meal) if member.total_meal else 0.0) # noqa

        return context
