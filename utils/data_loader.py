import tushare as ts
import pandas as pd

# ⚠️ 使用前请替换为你自己的 Tushare Token
ts.set_token('YOUR_TUSHARE_TOKEN_HERE')
pro = ts.pro_api()

def load_daily(ts_code: str, start_date: str, end_date: str = None) -> pd.DataFrame:
    """
    获取 A 股日线数据
    示例: df = load_daily('000001.SZ', '20200101')
    """
    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    if df.empty:
        raise ValueError(f"No data found for {ts_code}")
    
    df['trade_date'] = pd.to_datetime(df['trade_date'])
    df = df.sort_values('trade_date').set_index('trade_date')
    return df[['open', 'high', 'low', 'close', 'vol']]
