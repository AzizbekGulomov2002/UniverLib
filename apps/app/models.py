import datetime
from django.db import models
from dateutil.relativedelta import relativedelta
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
class Trade(models.Model):
    TypePay = (
        ("Dollar", "Dollar"),
        ("So'm", "So'm"),
    )
    type_pay = models.CharField(max_length=223, default='Dollar', choices=TypePay, null=True)
    client_num = models.CharField(max_length=13)
    client_name = models.CharField(max_length=200)
    client_passport = models.CharField(max_length=9, null=True, blank=True)
    imeika = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    price = models.FloatField()
    profit = models.FloatField()
    # surcharge = models.FloatField() #noqa
    dedline = models.IntegerField()
    
    start = models.DateField()
    desc = models.TextField(null=True, blank=True)
    next_pay = models.DateField()
    # class TradeQuerySet(models.QuerySet):
    #     def annotate_common_payment(self):
    #         return self.annotate(
    #             a_common_payment=models.Sum(
    #                 "payments__summa"
    #             )
    #         )
    #     def annotate_debt_balance(self):
    #         return self.annotate(
    #             a_debt_balance=models.F("total") - models.F("a_common_payment")
    #         )
    #     def annotate_status(self):
    #         today = timezone.localdate()
    #         return self.annotate(
    #             a_status=models.Case(
    #                 models.When(debt_balance=0, then=models.Value("Shartnoma yakunlangan")),
    #             )
    #         )
    # objects = TradeQuerySet.as_manager()
    @property
    def end(self):
        return self.start + relativedelta(months=self.dedline)
    @property
    def monthly_pay(self):
        return (self.price + self.profit) / self.dedline
    @property
    def debt_balance(self):
        return (self.total-self.common_payment)
    @property
    def common_payment(self):
        payments = self.payments.all()
        total_sum = sum(payment.summa for payment in payments)
        return total_sum
    def status(self):
        today = timezone.localdate()
        if self.debt_balance == 0:
            return "Shartnoma yakunlangan"
        elif self.debt_balance > 0 and self.next_pay < today:
            days_overdue = (today - self.next_pay).days
            if days_overdue > 0:
                return f"Qarzdorlik"
            else:
                return f"Qarzdorlik {self.monthly_pay*100} / {self.debt_balance}"  
        else:
            return "To'langan"
        
        
    # def debt_profit(self):
    #     today = timezone.localdate()
    #     # yigindi = sum(self.monthly_pay * 100) / sum(self.total - self.common_payment)
    #     if self.debt_balance > 0 and self.next_pay < today:
    #         return f"{(self.monthly_pay* 100) / (self.total-self.common_payment)}  %"
    #         # return yigindi
    # @property
    # def debt_profit(self):
    #     today = timezone.localdate()
    #     if self.debt_balance > 0 and self.next_pay < today:
    #         total_monthly_pay = sum(trade.monthly_pay for trade in Trade.objects.all())
    #         total_debt_balance = sum(trade.debt_balance for trade in Trade.objects.all())
    #         if total_debt_balance > 0:
    #             return total_monthly_pay * 100 / total_debt_balance
    #     return None
    
        
    # def calculate_price(self):
    #     days_passed = (timezone.now().date() - self.next_pay).days
    #     multiplier = (days_passed // 30) + 1
    #     calculated_price = self.monthly_pay * multiplier
    #     return calculated_price
    
    def calculate_dollar(self):
        days_passed = (timezone.now().date() - self.next_pay).days
        if self.type_pay == "Dollar":
            multiplier = (days_passed // 30) + 1
            calculated_price = self.monthly_pay * multiplier
            return f"$ {calculated_price} "
        else:
            return None
        
    def calculate_sum(self):
        days_passed = (timezone.now().date() - self.next_pay).days
        if self.type_pay == "So'm":
            multiplier = (days_passed // 30) + 1
            calculated_price = self.monthly_pay * multiplier
            return f"$ {calculated_price} so'm"
        else:
            return None
    

    def pay_day(self):
        today = timezone.localdate()
        if (self.next_pay - today).days < 0:
            return f"{0 - (self.next_pay - today).days}"
        else:
            return f"{(self.next_pay - today).days}"
     
    @property
    def total(self):
        return (self.price + self.profit)
    def __str__(self):
        return f"{self.client_name} "
    class Meta:
        ordering = ['-id']
class Payments(models.Model):
    PayType = (
        ("Oylik to'lov", "Oylik to'lov"),
        ("Tugatish", "Tugatish"),
        ("Maxsus to'lov", "Maxsus to'lov"),
    )
    pay_type = models.CharField(max_length=223, default='Davom etish', choices=PayType, null=True)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name="payments")
    summa = models.FloatField()
    date = models.DateField()
    finish = models.DateField(null=True, blank=True)
    desc = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.trade}"
    
    class Meta:
        ordering = ['-id']
