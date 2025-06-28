import datetime
from decimal import Decimal
from django.contrib.auth import authenticate
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Transaction, Account

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"error": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        if today.month < 4:
            fiscal_year_start = datetime.date(today.year - 1, 4, 1)
        else:
            fiscal_year_start = datetime.date(today.year, 4, 1)
        fiscal_year_end = datetime.date(fiscal_year_start.year + 1, 3, 31)
        total_revenue_data = Transaction.objects.filter(date__range=(fiscal_year_start, fiscal_year_end), account__account_type=Account.AccountTypes.REVENUE).aggregate(total=Sum('credit'))
        total_expenses_data = Transaction.objects.filter(date__range=(fiscal_year_start, fiscal_year_end), account__account_type=Account.AccountTypes.EXPENSE).aggregate(total=Sum('debit'))
        total_revenue = total_revenue_data['total'] or Decimal('0.00')
        total_expenses = total_expenses_data['total'] or Decimal('0.00')
        net_profit = total_revenue - total_expenses
        summary_data = {'fiscal_year': f"{fiscal_year_start.year}-{fiscal_year_start.year + 1}", 'total_revenue': total_revenue, 'total_expenses': total_expenses, 'net_profit': net_profit}
        return Response(summary_data, status=status.HTTP_200_OK)
