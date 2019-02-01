import paymentcorner
from paymentcorner.error import Error

client = paymentcorner.Client(email='user@domain.com', password='password',
                              client_id='xxxxx-xxxxx-xxxxxx-xxxxxxx', env=paymentcorner.Config.ENV_SANDBOX)

"""
Required Parameters
path 
"""

try:
    result = client.retrieve_fx_transaction_record({'path': 'e5cce1bf-af7e-4633-b6ae-bae4b8bcaf36'})
    print(result)
except Error as e:
    print(e.message)
