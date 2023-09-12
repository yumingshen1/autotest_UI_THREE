import sys

class Hello():
    def hello(self):
        print('the name of class is {}'.format(self.__class__.__name__))

if __name__ == '__main__':
    print(Hello().__class__.__name__)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
