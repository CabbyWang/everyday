去除list重复元素      l1 = ['a', 'b', 'c', 'd', 'a', 'b']
  l1 = list(set(l1))  # 会改变l1的顺序
  
  l1 = {}.fromkeys(l1).keys()   # 返回的是一个dict_keys对象，可迭代   排序会变
  
  l1 = sorted(set(l1), key=l1.index)      # 先获取set，然后按l1的顺序排序
  
  l2 = []
  [l2.append(i) for i in l1 if i not in l2]   #列表生成式， 可以保证顺序不变
