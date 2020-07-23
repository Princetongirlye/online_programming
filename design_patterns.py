# 状态模式
class state:
    pass


class morning(state):
    def dothings(self, w):
        if w.hour >= 9 and w.hour <= 12:
            print("现在{}点了，是正常上班干活中".format(w.hour))
        else:
            pass


class flow():
    def __init__(self, state):
        self.state = state
        self.hour = 0

    def set_state(self, state):
        self.state = state

    def dothings(self):
        self.state.dothings(self)
# 单例模式
# 确保一个类只有一个实例，并提供全局访问点
# 比如，某个服务器程序的配置信息存放在一个文件中，
# 客户端通过一个 AppConfig 的类来读取配置文件的信息。
# 如果在程序运行期间，有很多地方都需要使用配置文件的内容，
# 也就是说，很多地方都需要创建 AppConfig 对象的实例，
# 这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，
# 尤其是在配置文件内容很多的情况下。事实上，
# 类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象
class singl:
    def __new__(cls, *args, **kwargs):
        if not hasattr(singl, "_instance"):
            singl._instance = super().__new__(cls)
        return singl._instance

    def __init__(self):
        pass

    def dothings(self):
        print("doghintgs")

# 发布订阅模式（观察者模式）
"""
    在对象之前定义一对多的依赖，当一个对象改变状态，依赖它的对象都会受到通知，并自动更新
"""
class Observer:
    """
        观察者
    """
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(self.name + "收到信息：" + msg)


class Subject:
    """
        主题
    """
    def __init__(self):
        self.observers = []

    # 添加的是Observer实例
    def add_observers(self, observer):
        self.observers.append(observer)
        return self
    def remove_observers(self, observer):
        self.observers.remove(observer)
        return self
    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)