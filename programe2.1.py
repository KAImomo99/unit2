#我们已经知道n = 42 是合法的。那么42 = n 呢？

#会出现SyntaxError: cannot assign to literal 数字不能被当做变量来赋值
#x = y = 1 合法吗？
x=y=1
print(x,y)#合法的
#在某些编程语言中，每个语句都是以分号; 结束的。如果你在一个 Python 语句后也以分号结尾，会发生什么？
for n in range(0,10);#会显示错误语法
    print(n)
#如果在语句最后带上分号呢？
#在数学记法中，你可以将 x 和 y 像这样相乘：xy 。如果你在 Python 中也这么写的话，会发生什么？
x=1,y=2
print(xy)# name 'xy' is not defined 显示名称错误 计算机无法识别xy与x,y的区别



