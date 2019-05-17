# -*- coding: UTF-8 -*-

class Employee:
    employee = 0

    def initTwo(self, name, salary):
        self.name = name
        self.salary = salary

        print("这个是实例方法")
        print("名字是：" + self.name)
        print("工资是：" + self.salary)

    @staticmethod
    def initThree(name, salary):
        name = name
        salary = salary

        print ("这个是静态方法")
        print ("名字是：" + name)
        print ("工资是：" + salary)


@classmethod
def initOne(cls, name, salary):
    name = name

    salary = salary

    Employee.employee = 1

    print ("这个是类方法")
    print ("名字是：" + name)
    print ("工资是：" + salary)
