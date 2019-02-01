import paymentcorner
from paymentcorner.error import Error

client = paymentcorner.Client(email='user@domain.com', password='password',
                              client_id='xxxxx-xxxxx-xxxxxx-xxxxxxx', env=paymentcorner.Config.ENV_SANDBOX)

"""
Required Parameters
currency_to_buy | currency_to_sell | side_of_fx_tx | amount | fx_tx_date

Optional Paramters 
fx_tx_date
"""

try:
    result = client.fx_market_rate_with_markup({'currency_to_buy': 'USD',
                                                'currency_to_sell': 'GBP',
                                                'side_of_fx_tx': 'sell',
                                                'amount': .5,
                                                'fx_tx_date': '2019-05-20'
                                                })
    print(result)
except Error as e:
    print(e.message)
