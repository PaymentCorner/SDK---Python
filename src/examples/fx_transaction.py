import paymentcorner
from paymentcorner.error import Error

client = paymentcorner.Client(email='user@domain.com', password='password',
                              client_id='xxxxx-xxxxx-xxxxxx-xxxxxxx', env=paymentcorner.Config.ENV_SANDBOX)

"""
Required Parameters
currency_to_buy | currency_to_sell | side_of_fx_tx | amount | fx_tx_gtc

Optional Parameters 
fx_tx_date | amount_to_buy	| amount_to_sell | fx_tx_unique_id
"""

try:
    result = client.fx_transaction({'currency_to_buy': 'EUR',
                                    'currency_to_sell': 'USD',
                                    'side_of_fx_tx': 'sell',
                                    'amount': 10,
                                    'fx_tx_gtc': True,
                                    })
    print(result)
except Error as e:
    print(e.message)
