import paymentcorner
from paymentcorner.error import Error

client = paymentcorner.Client(email='user@domain.com', password='password',
                              client_id='xxxxx-xxxxx-xxxxxx-xxxxxxx', env=paymentcorner.Config.ENV_SANDBOX)

"""
Optional Parameters
ref | fx_tx_status | currency_to_buy | currency_to_sell | fx_tx_id | fx_tx_creation_date_from | fx_tx_creation_date_last |
fx_tx_update_date_from | fx_tx_update_date_last | tx_date_from | tx_date_to | currency_pair | min_amount_to_buy | max_amount_to_buy |
min_amount_to_sell | max_amount_to_sell | date_tx_debit_first | date_tx_debit_last | fx_tx_unique_id | page_nb | result_per_page |
sort_order | sort_asc_to_desc
"""

try:
    result = client.retrieve_fx_transaction({'fx_tx_status': 'FX_deal_settled',
                                             'fx_tx_creation_date_from': '2018-12-04'
                                             })
    print(result)
except Error as e:
    print(e.message)
