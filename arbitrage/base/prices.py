import pandas as pd
import numpy as np
import gspread
from gspread_dataframe import set_with_dataframe
from .helper.utils import get_time_now_in_local_timezone
from .helper.utils import get_coins_pair_price
from .models import CoinPair, Dex


def get_pairs_matrix():
    """
    Using multiprocessing with Pool
    :return: result of pair prices in different swaps
    """
    coin_pair = CoinPair.objects.all()
    pair_info = [(pair.coin_1.address, pair.coin_2.address, '-'.join((pair.coin_1.name, pair.coin_2.name)),
                  pair.coin_1.decimals, pair.coin_2.decimals)
                 for pair in coin_pair]

    results = []

    for i in range(len(pair_info)):
        results.append(get_coins_pair_price(pair_info[i]))
    return results


def sort_pair_price_result():
    """
    :return:
        dictionary_with_final_info
    """
    prices_result = np.array(get_pairs_matrix())
    # print('///////////////',prices_result)
    DEX = Dex.objects.all()
    data_collector = []

    for price_list in prices_result:
        only_dexs = dict(list(price_list.items())[:len(DEX)])
        sorted_prices = {k: v for k, v in sorted(only_dexs.items(), key=lambda item: item[1])}

        data_collector.append((
            price_list['pair'],
            '-'.join([list(sorted_prices)[0], list(sorted_prices)[-1]]),
            get_time_now_in_local_timezone(4.0).strftime("%m/%d/%Y, %H:%M:%S"),
            '{:.4f}'.format(price_list[list(sorted_prices)[-1]] - price_list[list(sorted_prices)[0]]),
            *(f'{k}({v})' for k, v in sorted_prices.items()),

        ))

    for i in data_collector:
        collected_data = pd.DataFrame(data_collector,
                                      columns=['coin_pair', 'dex_pair', 'date_added', 'price_defference',
                                               *[f'dex_{i + 1}' for i in range(len(DEX))]])

    return collected_data


def result_to_google_sheets():
    google_sheet_id = '1eDB4_C7hNmM-28DZgWxsjzx_qVN_wgeTMenq8VrsR0E'

    service_account_filename = 'test1-316510-624349e4ac61.json'
    prices_result = get_pairs_matrix()
    data_collector = list()

    sorted_result = sort_pair_price_result()
    for price_list in prices_result:
        only_dexs = dict(tuple(price_list.items())[:-1])
        final_result = {k: v for k, v in sorted(only_dexs.items(), key=lambda item: item[1])}

        data_collector.append(
            (get_time_now_in_local_timezone(4.0).strftime("%m/%d/%Y"),
             tuple(final_result.keys())[0],
             tuple(final_result.keys())[-1],
             price_list['pair'],
             round(100 - (float(final_result[tuple(final_result.keys())[0]]) /
                          float(final_result[tuple(final_result.keys())[-1]])) * 100, 2),
             'xxx'
             )
        )
    curr_df = pd.DataFrame(sorted_result, columns=(
        'coin_pair', 'dex_pair', 'date_added', 'price_defference', 'dex_1', 'dex_2', 'dex_3', 'dex_4', 'dex_5',
        'dex_6'))
    gc = gspread.service_account(filename=service_account_filename)
    sh = gc.open_by_key(google_sheet_id)
    current_worksheet = sh.worksheet("New Results")

    set_with_dataframe(current_worksheet, curr_df, 1, 1)


def get_percentage():
    sorted_data = sort_pair_price_result()
    for index, row in sorted_data.iterrows():
        percentage = round((float(row['dex_1'].split('(')[-1][:-1]) / float(row['dex_2'].split('(')[-1][:-1])) / 100, 5)

    return percentage
