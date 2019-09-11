class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    @property
    def c(self):
        return self.a + self.b


if __name__ == '__main__':
    t = A()
    print(t.c)
    t.a = 5
    print(t.c)
