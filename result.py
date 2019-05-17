#!/usr/bin/python
# -*- coding: UTF-8 -*-

from inherit import initOne
# from inherit import initThree
from inherit import Employee

class Result(Employee):

    name = raw_input('请输入姓名:')

    salary = raw_input('请输入工资:')

    # initOne(name,salary)
    #
    #
    # r = Employee()
    # r.initTwo(name,salary)
    # r.initThree(name, salary)
    # r.initOne(name,salary)
    # initThree(name, salary)

    def getResult(self):


        self.initTwo(self,name,salary)




