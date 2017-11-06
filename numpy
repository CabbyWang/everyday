numpy.genfromtxt()
numpy.clip()
numpy.fabs()     #绝对值
numpy.pow(a,b)   #a**b

a.atleast_xd() #保证数组至少有 x 维
a.squeeze()  #返回一个将所有长度为1的维度去除的新数组
a.flatten()  #将多维数组转化为1维数组   
a.ravel()    #返回1维数组（高效）
b = a.flat   #相当于返回了所有元组组成的一个迭代器(改变b的值会影响a)


import matplotlib.pyplot as plt
fig, axes = plt.subplots(figsize=(8,6))
axes.plot(x, y, 'r', linewidth=3)
axes.set_xlabel('Time(ps)')
axes.set_ylabel('Amplitude[a.u.]')
fig.savefig("triangular.png", dpi=600)


a.diagonal(offset=0)  #对角线（数组）  offset为偏移量
i = [0,1,2]
a[i,i]     和a.diagonal()类似


fromstring()    #string转array
tostring()    #array转string

对于文本文件，推荐使用
loadtxt
genfromtxt
savetxt
对于二进制文本文件，推荐使用
save
load
savez

# np.choose() 
control = np.array([[1,0,1],
                    [2,1,0],
                    [1,2,2]])
np.choose(control, [10,11,12])  #用后面的数组来填充control
【out】 array([[11, 10, 11],
       [12, 11, 10],
       [11, 12, 12]])
将数组中所有小于 10 的值变成 10，大于 15 的值变成 15。
a = np.array([[ 0, 1, 2], 
              [10,11,12], 
              [20,21,22]])

lt = a < 10
gt = a > 15

choice = lt + 2 * gt         # True代表1，False代表0。a再10-15之间，lt和gt两个都为False，choice的值为0；a<10，lt=1，gt=0，choice=1；
                             # a>15，lt=0,gt=1,choice=2
choice----》array([[1, 1, 1],
                   [0, 0, 0],
                  [2, 2, 2]])    
np.choose(choice,(a,10,15))     #choice=0，取a的值;choice=1,取10；choice=2,取15
