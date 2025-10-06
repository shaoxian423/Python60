import itertools
import math

# 定义牌面
SUITS = ['♠', '♥', '♦', '♣']           # 黑红方块梅花
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def make_deck():
    """返回 52 张牌的列表，格式如 'A♠', '10♦', 'K♣'"""
    return [f"{r}{s}" for s in SUITS for r in RANKS]


def five_card_combinations(deck=None):
    """
    返回一个迭代器，生成从 deck 中选出的所有 5 张牌组合（无序、不重复）。
    deck 为 None 时使用标准 52 张牌。
    使用 itertools.combinations，返回的是 tuples，例如 ('A♠','2♠','3♠','4♠','5♠')
    """
    if deck is None:
        deck = make_deck()
    return itertools.combinations(deck, 5)


# ---------- 常用示例 ----------
if __name__ == "__main__":
    # 牌堆与组合总数验证
    deck = make_deck()
    print("牌数:", len(deck))
    print("理论组合数 C(52,5):", math.comb(len(deck), 5))

    # 得到一个迭代器
    combos = five_card_combinations(deck)

    # 打印前 5 个组合（示例）
    for i, combo in enumerate(itertools.islice(combos, 5), 1):
        print(f"{i:2d}:", combo)

    # 如果想统计总数（注意会遍历整个迭代器，耗时较久）
    # 重新创建迭代器再计数，或者直接使用 math.comb
    total = math.comb(len(deck), 5)
    print("总组合数（用 math.comb）:", total)

    # 如果需要把所有组合写到文件（注意文件会很大 ~ 数百万行）
    # with open("5card_combinations.txt", "w", encoding="utf-8") as f:
    #     for combo in five_card_combinations(deck):
    #         f.write(",".join(combo) + "\n")
