import threading

x = 'eqw'


def test(arg):
    global x
    x = arg
    print(x)


t = threading.Thread(target=test, args='r')
t1 = threading.Thread(target=test, args='e')
t1.start()
t.start()

