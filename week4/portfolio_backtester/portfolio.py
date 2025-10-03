import itertools


def generate_combinations(tickers, combo_size):
    if combo_size > len(tickers):
        return []
    return list(itertools.combinations(tickers, combo_size))
