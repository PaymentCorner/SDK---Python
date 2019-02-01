import paymentcorner
from paymentcorner.error import Error

client = paymentcorner.Client(email='user@domain.com', password='password',
                              client_id='xxxxx-xxxxx-xxxxxx-xxxxxxx', env=paymentcorner.Config.ENV_SANDBOX)

"""
Required Parameters
path | new_date_fx_tx
"""

try:
    result = client.change_fx_conversion_delivery_date_quotation({'path': 'e5cce1bf-af7e-4633-b6ae-bae4b8bcaf36',
                                                                  'new_date_fx_tx': '2019-01-30'
                                                                  })
    print(result)
except Error as e:
    print(e.message)
