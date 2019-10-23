### 对象的常用方法

    obj = Object()
    
    hasattr(obj,'age') # 判断 obj 中是否有 age 对象
    
    obj.func = MethodType(func,args) # 对象动态绑定参数 
    
### 对象属性的定义

```python
class People:
    
    # 类变量，相当于 Java 的静态变量    
    name = None

    def __init__(self):
          self.name = "实例变量"

People.name # 直接访问类变量
people = People()
people.name # 通过实例变量访问类变量，不推荐
```

### 类方法的定义

参考 ClassFuncDiff

### Python 中的封装

参考 ClassPackage