money=0
def bank(mz,id,mon):
    global money
    print("账户人名字为"+mz)
    print("账号id为"+str(id))
    print("该账户余额为"+str(mon))
    print("开户成功")
    def menu():
        global money
        print("============================================")
        print("此时余额为:"+str(money))
        print("存钱请按1，取钱请按2，查询余额请按3，退卡请按4")
        def inp(num):
            global money
            money+=num
            print("此时余额为:"+str(money))
            menu()
        def omoney(num):
            global money
            money -= num
            print("此时剩余余额为:" +str(money))
            menu()
        def check():
            global money
            print("此时卡内余额为:"+str(money))
            menu()
        a=input()
        if a=='1':
            print("请输入要存多少钱")
            b=int(input())
            inp(b)
        elif a=='2':
            print("请输入要取出多少钱")
            b=int(input())
            omoney(b)
        elif a=='3':
            check()
        else:
            print("退卡成功")
            quit()
    menu()
bank("Crh",1,200)

