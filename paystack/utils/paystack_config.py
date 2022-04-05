from paystackapi.paystack import Paystack
from decouple import config

paystack_secret_key = Paystack(config('PAYSTACK_SECRET_KEY'))