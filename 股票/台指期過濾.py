from FinMind.data import DataLoader

dl=DataLoader()
future_data=dl.taiwan_futures_daily(futures_id="TX",start_date="2020-01-01")  #下載台指期代碼
print(future_data.columns) #顯示欄位名稱
future_data=future_data[(future_data.trading_session=="position")] #刪除盤後資料
future_data=future_data[(future_data.settlement_price>0)] #刪除沒有結算價的資料
future_data=future_data[(future_data["contract_date"]==future_data.groupby("date")["contract_date"].transform("min"))]


print(future_data)
future_data.to_csv("tx.csv")