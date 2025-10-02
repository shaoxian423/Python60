# trade_portfolio.py
import pandas as pd
import os

DATA_DIR = "data"  # 指向 data 目录
TRADES_FILE = os.path.join(DATA_DIR, "trades.csv")


def load_trades(file_path=TRADES_FILE):
    df = pd.read_csv(file_path)
    return df


def calculate_portfolio(trades):
    portfolio = {}
    for _, row in trades.iterrows():
        stock = row['stock']
        action = row['action']
        qty = row['quantity']
        price = row['price']

        if stock not in portfolio:
            portfolio[stock] = {'quantity': 0, 'book_cost': 0}

        if action == 'buy':
            portfolio[stock]['quantity'] += qty
            portfolio[stock]['book_cost'] += qty * price
        elif action == 'sell':
            # 卖出时减少数量和账面成本（简单处理）
            portfolio[stock]['quantity'] -= qty
            portfolio[stock]['book_cost'] -= min(qty,
                                                 portfolio[stock]['quantity'] + qty) * price

    # 计算平均成本
    for stock in portfolio:
        q = portfolio[stock]['quantity']
        portfolio[stock]['average_cost'] = round(
            portfolio[stock]['book_cost']/q, 2) if q else 0
    return portfolio


def get_portfolio_summary(portfolio, market_prices):
    summary = []
    total_market_value = sum(
        portfolio[s]['quantity']*market_prices.get(s, 0) for s in portfolio)
    for stock, data in portfolio.items():
        qty = data['quantity']
        book_cost = data['book_cost']
        avg_cost = data['average_cost']
        market_value = qty * market_prices.get(stock, 0)
        gain_loss = market_value - book_cost
        pct = round(market_value/total_market_value *
                    100, 2) if total_market_value else 0
        summary.append({
            "Stock": stock,
            "Quantity": qty,
            "Market Value": round(market_value, 2),
            "Gain/Loss": round(gain_loss, 2),
            "Average Cost": avg_cost,
            "Book Cost": round(book_cost, 2),
            "Portfolio %": pct
        })
    return summary
