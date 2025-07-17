'''
【演習】

以下の手順で、関数の定義と関数の呼び出しの処理を完成させてください。

01.関数を定義する
balance_calculation
・仮引数：principal_amount, interest_rate, deposit_period
・戻り値：balance

principal_amount：元金
interest_rate：金利
deposit_period：預入期間
balance：残高

02.関数 balance_calculation を呼び出す。
・実引数："蒲田太郎", 20

（参考）1年複利の例
元金：1,000,000
金利：1.0%
預入期間：3 年

① 1 年目残高：1,000,000 × 0.01 + 1,000,000 = 1,010,000
② 2 年目残高：1,010,000 × 0.01 + 1,010,000 = 1,020,100
③ 3 年目残高：1,020,100 × 0.01 + 1,020,100 = 1,030,301
'''

#######################################################
# 関数の定義
#######################################################
def balance_calculation(principal_amount, interest_rate, deposit_period):

  balance = principal_amount

  for _ in range(deposit_period):
    balance = balance + (balance * (interest_rate / 100))

  return balance

#######################################################
# 関数の呼び出し
#######################################################
balance = balance_calculation(1000000, 1.0, 3)
print(balance)

