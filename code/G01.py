#总市值大于等于100亿人民币元。
#拥有良好且持续的自由现金流量。
#稳定持续的营收成长率。
#较好的流动比率。
#较高的资产回报率。


import pandas as pd
import numpy as np
import datetime
import math

# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    context.buy_list=[]
    context.max_num_stocks = 20
    context.s1 = '000905.XSHG'

    #开盘前运行，选股
    scheduler.run_monthly(before_trading_stocks,5)

    #开盘时运行，交易
    scheduler.run_monthly(trading_stocks,5)


def before_trading_stocks(context,bar_dict):


    # 获取可交易股票池
    temp_list = get_stock_list(context)

    #获推荐股票池
    get_trade_list(context,temp_list)



#总股票池
def get_stock_list(context):
    temp_list = index_components('000300.XSHG', date=None)

    return_list = []
    # 过滤停牌和ST
    for stock in temp_list:
        suspended =  is_suspended(stock, count=1)
        is_st = is_st_stock(stock, count=1)

        if not is_st and not suspended:
            return_list.append(stock)

    return return_list


def get_trade_list(context,stock_list):
    # 获取当前时间的前一天
    now_time = context.now + datetime.timedelta(days=-1)
    now_time = now_time.strftime('%Y%m%d')
    
    # 1 近4季度经营现金流净额为正
    q = query(fundamentals.eod_derivative_indicator.market_cap,fundamentals.cash_flow.cash_from_operating_activities,fundamentals.cash_flow.cash_paid_for_operation_activities).filter(financials.stockcode.in_(stock_list))
    cash_df = get_fundamentals(q ,now_time,'4q',report_quarter = True)
    count = 0 
    index1 = []
    for item in cash_df.minor_axis:
        df = cash_df.minor_xs(item)
        df["flow"] =  df["cash_from_operating_activities"] - df["cash_paid_for_operation_activities"]
        if (df["flow"]>0).all():
            count = count +1 
            index1.append(item)
    print("index1 count",count)

    #2 近4季度主营增长都大于8，小于100%
    q = query(fundamentals.financial_indicator.inc_operating_revenue).filter(fundamentals.eod_derivative_indicator.market_cap_2>5000000000)
    pe_df = get_fundamentals(q ,now_time,'4q')
    count = 0 
    index2 = []
    for item in pe_df.minor_axis:
        df = pe_df.minor_xs(item)
        if (df["inc_operating_revenue"]>8).all()and (df["inc_operating_revenue"]<100).all() : 
            count = count +1 
            index2.append(item)
    print("index 2 count",count)

    #3 近4季度净利润增长都大于8，小于100%
    q = query(fundamentals.financial_indicator.inc_adjusted_net_profit).filter(financials.stockcode.in_(stock_list))
    np_df = get_fundamentals(q ,now_time,'4q')
    count = 0 
    index3 = []
    for item in np_df.minor_axis:
        df = np_df.minor_xs(item)
        is_good = is_good_enough(df)
        if (is_good):
            index3.append(item)
    print("index 3 count",len(index3))


    stock_list_temp =list(set(index2) ) 
    print("stock_list_temp lens:",len(stock_list_temp))

 
    #查询流动比率,高于优化后的平均流动比率
    if len(stock_list_temp) == 0:
        return
    current_ratio_lf_df = get_factor(stock_list_temp,"current_ratio_lf")
    df = current_ratio_lf_df[current_ratio_lf_df>0]
    df_mean = df.mean()
    df = df[df>df_mean]

    stock_list_temp = df.index
    qeury_stock_list = []
    for stock in stock_list_temp:
        suspended =  is_suspended(stock, count=1)
        is_st = is_st_stock(stock, count=1)

        if not is_st and not suspended:
            qeury_stock_list.append(stock)


    q = query(fundamentals.financial_indicator.return_on_equity).filter(financials.stockcode.in_(qeury_stock_list)).order_by(fundamentals.financial_indicator.return_on_asset.desc()).limit(context.max_num_stocks)
    market_cap_df = get_fundamentals(q ,now_time)

    context.buy_list = market_cap_df.columns
    print(context.buy_list)



def handle_bar(context, bar_dict):
    pass    

    

def trading_stocks(context, bar_dict):
   
    for stock in context.portfolio.positions:
        if stock not in context.buy_list:
            order_target_percent(stock, 0)
            
    # context.buy_list = [stock for stock in context.buy_list
    #                   if stock in bar_dict and bar_dict[stock].is_trading  ]
   
    if len(context.buy_list) == 0:
        print("lens = 0")
        return
    
    weight = 1.0/len(context.buy_list)
    
    for stock in context.buy_list:
        order_target_percent(stock, weight)

def is_good_enough(increase_number):
    is_good = 0
    increase_number_items = increase_number.inc_adjusted_net_profit
    for i, v in increase_number_items.items():
#         print(v)
        if v> 8 and v < 100:
            is_good = is_good + 1
    if is_good == 4:
        return True
    else:
        return False  
