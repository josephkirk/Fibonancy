from time import time

class Fibonanci(object):
    _sequence = {0:0,1:1,2:1}

    def __init__(self,n=100,method='topDown'):
        self.method = {
            'topDown': self.topDown,
            'bottomUp': self.bottomUp
        }
        self.n = n
        self.method[method](n)

    def __repr__(self):
        return "{}:{}".format(self.__class__.__name__, ' '.join([str(num) for id, num in self._sequence.iteritems()]))

    def topDown(self, n):
        if n in self._sequence:
            return self._sequence[n]
        if n<=2:
            f = 1
        else:
            f = self.topDown(n-1)+self.topDown(n-2)
            self._sequence[n] = f
        return f

    def bottomUp(self, n):
        for k in range(n):
            if k <=2:
                f = 1
            else:
                f = self._sequence[n-1] + self._sequence[n-2]
            self._sequence[k]=f
        return self._sequence[n]
    @property
    def sequence(self):
        return self._sequence[self.n]

    @sequence.setter
    def sequence(self,n):
        self.__class__(n)
        self.n = n

if __name__ == '__main__':
    fib = Fibonanci()
    fib.sequence = 102
    print fib.sequence

