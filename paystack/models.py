from tabnanny import verbose
import time
from django.db import models
from time import timezone
from .base_model import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from .customer import Customer


CURRENCY_CHOICES = {
    ("NGN", "NGN"),
    ("GHS", "GHS"),
    ("ZAR", "ZAR"),
    ("USD", "USD"),
}


class Transaction(BaseModel):

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
    metadata = models.JSONField(
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
        help_text=_("Customer ID of the virtual account"),
    )

    assignee_id = models.CharField(
        _("Assignee ID"),
        help_text=_("Assignee ID of the virtual account"),
    )

    account_type = models.CharField(
        _("Account Type"),
        help_text=_("Account type of the virtual account"),
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.customer} virtual account {self.account_number}"

    class Meta:
        verbose_name = _("Virtual Account")
        verbose_name_plural = _("Virtual Accounts")


class Subaccount(BaseModel):
    business_name = models.CharField(
        _("Business Name"), help_text="Name of business for subaccount", max_length=255
    )

    settlement_bank = models.CharField(
        _("settlement_bank"),
        help_text=_(
            "Bank Code for the bank. You can get the list of Bank Codes by calling the List Banks endpoint"
        ),
        max_length=50,
    )

    account_number = models.IntegerField(
        _("Account number"), help_text="Bank Account Number"
    )

    percentage_charge = models.FloatField(
        _("Percentage charge"),
        help_text=_(
            "The default percentage charged when receiving on behalf of this subaccount"
        ),
    )

    description = models.TextField(
        _("description"),
        help_text=_("A description for this subaccount"),
    )

    primary_contact_email = models.EmailField(
        _("Primary Contact Email"), help_text=_("A contact email for the subaccount")
    )

    primary_contact_phone = models.CharField(
        _("primary_contact_phone"),
        help_text=_("A phone number to call for this subaccount"),
        max_length=20,
    )

    metadata = models.JSONField(
        _("metadata"),
        help_text=_(
            "Stringified JSON object. Add a custom_fields attribute which has an array of objects if you would like the fields to be added to your transaction when displayed on the dashboard"
        ),
        null=True,
        blank=True,
    )


class Refund(BaseModel):

    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    amount = models.IntegerField(
        _("amount"),
        help_text=_(
            """
            Amount ( in kobo if currency is NGN, pesewas,
            if currency is GHS, and cents, if currency is ZAR ) to be refunded  to the customer.
            Amount is optional(defaults to original transaction amount) and cannot be more than the original transaction amount
            """
        ),
    )

    currency = models.CharField(
        _("Currency"),
        choices=CURRENCY_CHOICES,
        max_length=3,
        help_text=_(
            "Three-letter ISO currency. Allowed values are: NGN, GHS, ZAR or USD"
        ),
    )

    customer_note = models.TextField(_("Customer Note"), help_text=_("Customer reason"))

    merchant_note = models.TextField(_("Merchant Note"), help_text=_("Merchant reason"))

    def __str__(self):
        return f"Refund for {self.transaction} amounted to {self.amount}"


class Invoice(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    amount = models.IntegerField(
        _("amount"),
        help_text=_(
            """
            Amount ( in kobo if currency is NGN, pesewas,
            if currency is GHS, and cents, if currency is ZAR ) to be refunded  to the customer.
            Amount is optional(defaults to original transaction amount) and cannot be more than the original transaction amount
            """
        ),
    )

    description = models.TextField(
        _("description"),
        help_text=_("A description for this subaccount"),
    )

    due_date = models.DateTimeField(
        _("Due Date"),
        help_text=_("ISO 8601 representation of request due date"),
        auto_now=True,
    )

    tax = models.ArrayField(
        _("Tax"),
        help_text=_(
            'Array of taxes to be charged in the format [{"name":"VAT", "amount":2000}]'
        ),
    )

    currency = models.CharField(
        _("Currency"),
        choices=CURRENCY_CHOICES,
        default="NGN",
        max_length=3,
        help_text=_(
            "Three-letter ISO currency. Allowed values are: NGN, GHS, ZAR or USD"
        ),
    )

    send_notification = models.BooleanField(
        _("Send notification"),
        help_text=_(
            "Indicates whether Paystack sends an email notification to customer. Defaults to true"
        ),
        default=True,
    )

    draft = models.BooleanField(
        _("Draft"),
        help_text=_(
            "Indicate if request should be saved as draft. Defaults to false and overrides send_notification"
        ),
        default=False,
    )
    has_invoice = models.BooleanField(
        _("Has Invoice"),
        help_text=_(
            "Set to true to create a draft invoice (adds an auto incrementing invoice number if none is provided) even if there are no line_items or tax passed"
        ),
        default=False,
    )

    invoice_number = models.IntegerField(
        _("Invoice Number"),
        default=1,
        help_text=_(
            "Numeric value of invoice. Invoice will start from 1 and auto increment from there. This field is to help override whatever value Paystack decides. Auto increment for subsequent invoices continue from this point."
        ),
    )

    split_code = models.CharField(
        _("Split Code"),
        max_length=100,
        help_text=_("The split code of the transaction split. e.g. SPL_98WF13Eb3w"),
    )

    def __str__(self):
        return str(self.customer)


class Wallet(BaseModel):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    wallet_id = models.CharField(
        _("Wallet Id"),
        max_length=50,
        help_text=_("A unique identifier for the Wallet of a particular customer"),
    )

    balance = models.IntegerField(
        _("Wallet Balance"), default=0, help_text=_("Balance of a customer wallet")
    )
