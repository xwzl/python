class MetaSchool(type):

    def __new__(cls, name, bases, attrs):
        attrs['descriptions'] = lambda self: print(self.description)
        attrs['printAddress'] = lambda self: print("学校地址：%s" % self.address)
        return super().__new__(cls, name, bases, attrs)


class TsinguaUniversity(metaclass=MetaSchool):

    def __init__(self, address, description):
        self.address = address
        self.description = description

    def setAddress(self, address):
        self.address = address
        print(address)

    def getAddress(self):
        print(self.address)
        return self.address

    add = property(getAddress, setAddress)


one = TsinguaUniversity("北京市清华大学", "清华大学")

one.descriptions()
one.printAddress()
