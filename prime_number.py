# coding:utf-8
"""实现一遍廖雪峰官网的素数算法"""


def _not_divisible(n):
    return lambda x: x % n > 0


def _old_iter():
    """
    初步筛选出所有的奇数
    :return: 返回一个生成器
    """
    n = 1
    while True:
        n += 2
        yield n


def prims():
    yield 2
    it = _old_iter()        # 生成器
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    for i in prims():
        if i < 100:
            print(i)
        else:
            break           # 这个要加上, 不然会无限循环下去
