偏函数（partial）
  #把一个函数的某些参数固定住（设置默认值），返回一个新的函数   调用这个新函数会更简单
    from functools import partial           
    
    int2 = partial(int, base=2)             # int默认转为十进制整形， int（str， 2）转为二进制整形
    
    max()
    
    max2 = partial(max, 10)                 
    max2(1, 2, 12)                          # 求 1，2，12，10的最大值


functools.wraps
  # 如果不使用wraps，原始函数的__name__和__doc__都会丢失（__doc__直接获取不到，为None    __name__会被替换为wrap）
    from functools import wraps
    
    def my_decorator(f):
        # @wraps(f)                                     # 装饰wrap
        def wrap(*args, **kwargs):
            print('decorator function called')
            return f(*args, **kwargs)
        return wrap
    
    @my_decorator
    def func():
        '''func docs'''
        print('func function called')
    
    if __name__ == '__main__':
        func()
        print(func.__doc__, func.__name__)
