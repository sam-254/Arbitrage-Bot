from datetime import datetime, timezone, timedelta
from .models import Dex, Setting
from .abi import *
import pandas as pd

pool_abi = ''

# web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/4b1db8d17da142f3861622b56cfdb3e7'))
web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/OCil3oXAMGtrFeptBPchZAL7CoYRAFJf'))


def get_coins_pair_price(pair):
    """
    :param tuple with pairs info params:
    :return:
        pair_price
    """
    dexes = Dex.objects.all()
    result = {}
    for swap in dexes:
        contract = web3.eth.contract(address=swap.address, abi=swap.abi)
        if swap.name == 'OneSplit':
            try:
                response_result = result_by_get_expected_return(address_1=pair[0], address_2=pair[1],
                                                                amount=int(pair[3]), decimal=pair[-1],
                                                                contract=contract)
            except Exception as e:
                pass
        elif swap.name == 'Balancer':
            try:
                response_result = result_by_view_split_exact_out(address_1=pair[0], address_2=pair[1],
                                                                 amount=int(pair[3]), contract=contract)
            except Exception as e:
                pass

        elif swap.name == 'Kyber':
            try:
                response_result = result_by_get_expected_rate(address_1=pair[0], address_2=pair[1],
                                                              amount=int(pair[3]), contract=contract)
            except Exception as e:
                pass
        elif swap.name == 'Curve':
            try:
                response_result = result_by_get_estimated_swap_amount(address_1=pair[0], address_2=pair[1],
                                                                      amount=int(pair[3]), decimal=pair[-1],
                                                                      contract=contract)
            except Exception as e:
                pass
        else:

            try:
                response_result = result_by_get_amounts_out(address_1=pair[0], address_2=pair[1],
                                                            amount=int(pair[3]), decimal=pair[-1], contract=contract)
            except Exception as e:
                pass

        result[swap.name] = float(response_result)
    result['pair'] = pair[-3]

    return result


def get_time_now_in_local_timezone(timezone_offset=0.4):
    """

    :param timezone_offset:
    :return: datetime in string representation
    """
    timezone_info = timezone(timedelta(hours=timezone_offset))

    return datetime.now(timezone_info)


def make_settings_changes():
    setting_object = Setting.objects.all()[0]
    contract = web3.eth.contract(address='0x9Ad0b9bf2e211Ac2d2A41749c9eF433dA943FFc2',
                                 abi=pool_abi)
    contract.functions.changeMaxDepositAmount(setting_object.max_deposit_amount)
    contract.functions.changeMinDepositAmount(setting_object.min_deposit_amount)
    contract.functions.changeTreasure(setting_object.taxation_address)
    contract.functions.changeTreasurePercentage(setting_object.taxation_address)


def make_whitelist_changes():
    df = pd.read_csv('uploads/accounts.csv')
    print(df)

    # contract = web3.eth.contract(address='0x9Ad0b9bf2e211Ac2d2A41749c9eF433dA943FFc2',
    #                              abi=pool_abi)
    # for account in df:
    #     contract.functions.AddToWhitelist(user='address',
    #                                   contract=contract)

