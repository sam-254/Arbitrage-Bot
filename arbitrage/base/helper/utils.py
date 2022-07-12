from web3 import Web3
from datetime import datetime, timezone, timedelta
from .abis import *
from ..models import Dex

# web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/42e6751ff02140b5aadcab261c210362'))
web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/OCil3oXAMGtrFeptBPchZAL7CoYRAFJf'))


# connects to smart_contract and gets pair price for given swap
# def get_coins_pair_price(swap_address, swap_abi, from_coin, to_coin, proc_num, return_dict):
def get_coins_pair_price(pair):
    """
    :param tuple with pairs info params:
    :return:
        pair_price
    """
    dexes = Dex.objects.all()
    result = {}
    # from_price = 0
    for dex in dexes:
        contract = web3.eth.contract(address=dex.address, abi=dex.abi)
        if dex.name == 'OneSplit':
            try:
                response_result = result_by_get_expected_return(address_1=pair[0], address_2=pair[1],
                                                                amount=int(pair[3]), decimal=pair[-1],
                                                                contract=contract)
            except Exception as e:
                pass
        elif dex.name == 'Balancer':
            try:
                response_result = result_by_view_split_exact_out(address_1=pair[0], address_2=pair[1],
                                                                 amount=int(pair[3]), contract=contract)
            except Exception as e:
                pass

        elif dex.name == 'Kyber':
            try:
                response_result = result_by_get_expected_rate(address_1=pair[0], address_2=pair[1],
                                                              amount=int(pair[3]), contract=contract)
            except Exception as e:
                pass
        elif dex.name == 'Curve':
            try:
                response_result = result_by_get_estimated_dex_amount(address_1=pair[0], address_2=pair[1],
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
        result[dex.name] = float(response_result)

        # result['from_coin'] = from_price
    result['pair'] = pair[-3]
    return result




# connects to smart_contract and gets pair price for given dex
def get_time_now_in_local_timezone(timezone_offset=0.4):
    """

    :param timezone_offset:
    :return: datetime in string representation
    """
    timezone_info = timezone(timedelta(hours=timezone_offset))

    return datetime.now(timezone_info)