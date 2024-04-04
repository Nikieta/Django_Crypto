from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'webpage/index.html')

import pandas as pandas
import datetime as databases
import time as t
from pycoingecko import CoinGeckoAPI

cg=CoinGeckoAPI()

cg.ping()

coinList=cg.get_coins_list()
coinDataFrame=pd.DataFrame.from_dict(coinList).sort_values('id').reset_index(drop=True)
coins=['bitcoin','ethereum','dogecoin']

counterCurrencies=cg.get_supported_vs_currencies()
vsCurrencies=['usd','usd','usd']

simplePriceRequest=cg.get_price(ids=coins,vs_currencies='usd')
print(simplePriceRequest)