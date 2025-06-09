PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r**2)


def add(a, b):
    return a + b


if __name__ == "__main__":
    test = Math()
    print(test.solv(2))
    print(add(5, 9))
