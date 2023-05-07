# python-essentials

## Decorator
A Python decorator is a function that takes in a function and returns it by adding some functionality.
Python中的装饰器其实也是一种函数， 它可以在不修改原函数代码情况下扩展原函数功能。装饰器函数与普通函数不同之处就在于装饰器函数返回了一个函数对象，装饰器利用了闭包的原理来实现。主要用于日志插入，权限管理等等。

### Special Decorators: @staticmethod, @classMethod, @property
- @staticmethod: 
  - 不需要实例化类就能调用的method
  - 无法访问类和对象的数据的
  - 不需要用self，cls，也可以没有arg
- @classmethod: 
  - 不需要实例化类就可以直接调用的方法，第一个参数为cls
  - 可以设置修改类属性，也可以实例化对象
  - 常用于工程模式，或者第三方的libraries

- 共同点：都可用类名直接调用


## Assignment, Shallow Copy, Deep Copy
总结：
1、赋值：简单地拷贝对象的引用，两个对象的id相同。
2、浅拷贝：创建一个新的组合对象，这个新对象与原对象共享内存中的子对象。
3、深拷贝：创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。