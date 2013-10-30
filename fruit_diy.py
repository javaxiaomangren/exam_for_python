#/usr/bin/evn python
#coding: utf8

#水果类型和价格
FRUIT_SALE_PRICE = {"apple": 5.0, "orange": 4.0, "banana": 2.5, "pear": 3.0}


class PriceStrategy:
    """
        定义水果diy价格计算策略，　默认策略是水果价格的平均值
    """
    def get_price(self, diy=None):
        _prices = filter(bool, [FRUIT_SALE_PRICE.get(key, 0) for key in diy.keys()])
        return sum(_prices) / len(_prices)


class WeightedAvgPrice(PriceStrategy):
    """
        diy:{key:value}, key=水果名-->value=该水果在这个diy篮子里所占的比重(权重)
        加权平均策略，sum(水果价格*水果权重 +..)
    """
    def get_price(self, diy=None):
        _price = lambda x: FRUIT_SALE_PRICE.get(x, 0.0) * diy[x]
        return sum(map(_price, diy.keys()))


class StaticPrice(PriceStrategy):
    """
    固定价格
    """
    def __init__(self, price):
        self.price = price

    def get_price(self, diy=None):
        return self.price


class ChargeStrategy:
    """
        收银策略
    """
    def get_cost(self, money):
        return money


class Discount(ChargeStrategy):
    """
        打折策略
    """
    def __init__(self, discount):
        self.discount = discount

    def get_cost(self, money):
        if self.discount > 0 and (self.discount <= 1):
            return money * self.discount


class ReturnCash(ChargeStrategy):
    """
        返现策略
    """
    def __init__(self, total, ret):
        self.total = total
        self.ret = ret

    def get_cost(self, money):
        if money >= self.total:
            return money - self.ret
        return money


class Calculation:
    """
        计算水果diy价格
    """
    def __init__(self, price_strategy, discount_strategy):
        self.ps = price_strategy
        self.ds = discount_strategy

    def get_cash(self, diy, weight):
        return self.ds.get_cost(self.ps.get_price(diy) * weight)


def main():
    diy = {"apple": 0.75, "orange": 0.25}
    weight = 10
    cal1 = Calculation(PriceStrategy(), ChargeStrategy())
    cal2 = Calculation(WeightedAvgPrice(), ReturnCash(100, 10))
    cal3 = Calculation(WeightedAvgPrice(), Discount(0.9))
    cal4 = Calculation(StaticPrice(7.0), Discount(0.7))
    print cal1.get_cash(diy, weight)
    print cal2.get_cash(diy, weight)
    print cal3.get_cash(diy, weight)
    print cal4.get_cash(diy, weight)

if __name__ == "__main__":
    main()
