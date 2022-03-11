from tabnanny import verbose
import time
from django.db import models
from pytz_deprecation_shim import timezone
from .base_model import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator




class Transaction(BaseModel):

    CURRENCY_CHOICES = (
        ("NGN", "NGN"),
        ("GHS", "GHS"),
        ("ZAR", "ZAR"),
        ("USD", "USD"),
    )

    BEARER_CHOICES = (
        ("ACCOUNT", "ACCOUNT"),
        ("SUBACCOUNT", "SUBACCOUNT"),
    )

    amount = models.IntegerField(
        _("Amount"),
        help_text=_(
            "Amount of transaction. If NGN, unit is kobo; if GHS, unit is pesewas"
        ),
        blank=False,
    )
    email = models.EmailField(
        _("Customer Email"),
        max_length=254,
        blank=False,
        null=False,
    )
    currency = models.CharField(
        _("Currency"),
        help_text=_("Currency of transaction"),
        max_length=4,
        choices=CURRENCY_CHOICES,
        default="NGN",
        blank=False,
        null=False,
    )
    reference = models.CharField(
        _("Reference"),
        help_text=_("Reference of transaction"),
        max_length=100,
        blank=False,
        null=False,
    )
    callback_url = models.URLField(
        _("Callback URL"),
    )

    plan = models.ForeignKey("Plan", on_delete=models.CASCADE)
    invoice_limit = models.IntegerField(
        _("Invoice Limit"),
        help_text=_(
            "Invoice limit of transaction. Number of times to charge customer during subscription to plan"
        ),
        null=True,
        default=1,
        blank=True,
    )
    metadata = models.CharField(
        _("Metadata"),
        help_text=_("Metadata of the transaction. JSON converted to string"),
        null=True,
        blank=True,
    )
    channels = models.ArrayField(
        _("Channels"),
        help_text=_(
            "Channels to be used for transaction. They include ['card', 'bank', 'ussd', 'qr', 'mobile_money', 'bank_transfer']"
        ),
    )
    split_code = models.CharField(
        _("Split Code"),
        help_text=_("The split code of the transaction split. e.g. SPL_98WF13Eb3w"),
    )
    subaccount = models.CharField(
        _("Subaccount"),
        help_text=_(
            "The code for the subaccount that owns the payment. e.g. ACCT_8f4s1eq7ml6rlzj"
        ),
    )
    transaction_charge = models.IntegerField(
        _("Transaction Charge"),
        help_text=_("Transaction charge of the transaction"),
    )
    bearer = models.CharField(
        _("Bearer"),
        help_text=_(
            "Bearer of the transaction. can either be 'subaccount' or 'account'"
        ),
        choices=BEARER_CHOICES,
    )
    
    def __str__(self):
        return f"{self.email} {self.reference} - {self.amount} {self.currency}"
    
    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")



class Plan(BaseModel):

    CURRENCY_CHOICES = {
        ("NGN", "NGN"),
        ("GHS", "GHS"),
        ("ZAR", "ZAR"),
        ("USD", "USD"),
    }

    name = models.CharField(
        _("Plan name"),
        max_length=200,
        help_text=_(
            "Name of the be in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR"
        ),
    )

    interval = models.CharField(
        _("Interval"),
        help_text=_(
            "Interval in words. Valid intervals are: daily, weekly, monthly,biannually, annually"
        ),
    )

    description = models.TextField(
        _("Description"), help_text=_("A description for this plan")
    )

    send_invoices = models.Boolean(
        _("Send invoice to User"),
        default=False,
        help_text=_(
            "Set to false if you don't want invoices to be sent to your customers"
        ),
    )

    send_sms = models.Boolean(
        _("Send SMS"),
        default=False,
        help_text=_(
            "Set to false if you don't want text messages to be sent to your customers"
        ),
    )

    currency = models.CharField(
        _("Currency"),
        max_length=50,
        choices=CURRENCY_CHOICES,
        help_text=_(
            "Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD"
        ),
    )

    invoice_limit = models.IntegerField(
        _("Invoice Limit"),
        default=1,
        help_text=_(
            "Number of invoices to raise during subscription to this plan. Can be overridden by specifying an invoice_limit while subscribing."
        ),
    )

    def __str__(self):
        return f"{self.name} for {self.interval}"

    class Meta:
        verbose_name = _("Plan")
        verbose_name_plural = _("Plans")


class Subscription(BaseModel):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    authorization = models.ForeignKey("Authorization", on_delete=models.SET_NULL)
    start_date = models.DateTimeField(timezone.now())

    def __str__(self):
        return f"{self.customer} subscribed to {self.plan}"


    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")




class VirtualAccounts(BaseModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    account_name = models.CharField(
        _("Account Name"),
        help_text=_("Name of the account"),
        max_length=100,
    )
    assigned = models.BooleanField(
        _("Assigned"),
        help_text=_("Whether the account is assigned to a user"),
        default=False,
    )
    
    account_number = models.CharField(
        _("Account Number"),
        help_text=_("Account number of the virtual account"),
        max_length=50,
    )
    currency = models.CharField(
        _("Currency"),
        help_text=_("Currency of the virtual account"),
        max_length=50,
    )
    balance = models.IntegerField(
        _("Balance"),
        help_text=_("Balance of the virtual account"),
    )
    
    active = models.BooleanField(
        _("Active"),
        help_text=_("Whether the account is active"),
    )
    customer_id = models.CharField(
        _("Customer ID"),
        help_text = _("Customer ID of the virtual account"),
    )
    
    assignee_id = models.CharField(
        _("Assignee ID"),
        help_text = _("Assignee ID of the virtual account"),
    )
    
    account_type = models.CharField(
        _("Account Type"),
        help_text = _("Account type of the virtual account"),
    )
    
    assigned_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.customer} virtual account {self.account_number}"

    class Meta:
        verbose_name = _("Virtual Account")
        verbose_name_plural = _("Virtual Accounts")
