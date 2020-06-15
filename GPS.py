def test(a):
    while a>7:
        while 1:
            a+=1
            if a==5:
                print('跳出啦')
                break
    print('aaa')
if __name__ == '__main__':
    test(0)