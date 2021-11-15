def get_percent(sum_deposit, period):
    if period not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 6, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= sum_deposit < rate['end_sum']:
            return rate[period]

    return False

def deposit(sum_deposit, period):
    percent = get_percent(sum_deposit, period)
    if not percent:
        print("не походит тариф")

    total = sum_deposit
    for i in range(period):
        profit = sum_deposit * percent / 100 /12
        total += profit

    print(round(total,3))

deposit(1000, 6)

def refill_deposit(sum_deposit, period, refill=0):
    percent = get_percent(sum_deposit, period)
    if not percent:
        print("не походит тариф")

    total = sum_deposit
    for i in range(period):
        profit = sum_deposit * percent / 100 /12
        total += profit
        if i != 0 and i != period - 1:
            total += refill + refill * percent / 100 / 12

    print(round(total,3))

refill_deposit(1000, 6, 100)