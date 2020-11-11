import random
class Family():
    def __init__(self, surname, address, income):
        self.surname = surname
        self.address = address
        self.income = income

class Father(Family):
    def __init__(self, name, age):
        super(Family, self).__init__()
        self.name=name
        self.age=age
        self.__secret = '我外面有人'
    def action(self):
        money = random.randint(100,1000)
        return  money

class Mother(Family):
    def __init__(self,name,age):
        super(Family, self).__init__()
        self.name=name
        self.age=age
        self.__secret = '我有很多私房钱'

    def action(self):
        money=random.randint(100,500)
        return  -money

class Son(Family):
    def __init__(self,name,age):
        super(Family,self).__init__()
        self.name=name
        self.age=age
        self.__secret = '我喜欢隔壁小花'

    def action(self):
        money=random.randint(0,100)
        return -money

if __name__ == '__main__':
    family=Family('李','广州',1000)
    father=Father('利海', 25)
    mother=Mother('赫丽', 33)
    son=Son('豪华',10)

    print('这是一个姓'+family.surname+'的家庭,他们生活在'+family.address)
    print('我是父亲-'+family.surname+father.name+'今年'+str(father.age)+'岁')
    print('我是母亲-'+mother.name+'今年'+str(mother.age)+'岁')
    print('我是儿子-'+family.surname+son.name+'今年'+str(son.age)+'岁')

    father_money=father.action()
    family.income+=father_money
    print('父亲今天赚了'+str(father_money)+'元，家庭资产剩余'+str(family.income))

    mother_money=mother.action()
    family.income += mother_money
    print('母亲今天花了' + str(-mother_money) + '元，家庭资产剩余' + str(family.income))

    son_money=son.action()
    family.income += son_money
    print('儿子今天花了' + str(-son_money) + '元，家庭资产剩余' + str(family.income))

    print('父亲告诉你一个小秘密：'+father._Father__secret)
    print('母亲告诉你一个小秘密'+mother._Mother__secret)
    print('儿子告诉你一个秘密'+son._Son__secret)










