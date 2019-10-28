import enum


class ThreadStatus(enum.Enum):
    NEW = 1, "创建"
    RUNNABLE = 2, "可运行"
    WAITING = 3, "等待"
    BLOCKING = 4, "阻塞"
    DESTROY = 5, "销毁"

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    @property
    def getCode(self):
        return self.code

    @property
    def getMessage(self):
        return self.message

    def getThreadStatusByCode(code: int):
        for threadStatus in ThreadStatus.__members__.items():
            if threadStatus[1].getCode is code:
                return threadStatus


print(ThreadStatus.NEW)
print(ThreadStatus.NEW.getCode)
print(ThreadStatus.NEW.getMessage)

for value in ThreadStatus.__members__.items():
    print(value)

print(ThreadStatus.getThreadStatusByCode(1))
