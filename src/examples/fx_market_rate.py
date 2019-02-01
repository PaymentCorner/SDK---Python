import paymentcorner
from paymentcorner.error import Error

client = paymentcorner.Client(email='user@domain.com', password='password',
                              client_id='xxxxx-xxxxx-xxxxxx-xxxxxxx', env=paymentcorner.Config.ENV_SANDBOX)

"""
Required Parameters
currency_pair
"""

try:
    result = client.fx_market_rate({'currency_pair': 'EURUSD'})
    print(result)
except Error as e:
    print(e.message)
