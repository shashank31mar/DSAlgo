#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:22:41 2018

@author: shashankgupta
"""

from enum import Enum

class City(Enum):
    Mumbai = "Mumbai"
    Bangalore = "Bangalore"

class EmpTypes(Enum):
    CITY_MANAGER = "CityManager"
    FLEET_MANAGER = "FleetManager"
    DELIVERY_MANAGER = "DeliveryManager"

class Position(Enum):
    DE = "DE"
    FM = "FM"
    CM = "CM"

class Employee:
    def __init__(self,name,id,position,salary=0,rating=0):
        #print("Employee")
        self.name = name
        self.id = id
        self.salary = salary
        self.rating = rating
        self.bonus = 0.0
        self.position = position
    
    def printDetails(self,space=""):
        '''
        print("Name : {}, ID : {}, salary : {}, rating: {}, position : {}, bonus : {}"\
              .format(self.name,self.id,self.salary,\
                      self.rating,self.position,self.bonus),end=" ")
        '''
        print(space + "Name : {}".format(self.name))
        print(space + "ID : {}".format(self.id))
        print(space + "salary : {}".format(self.salary))
        print(space + "rating : {}".format(self.rating))
        print(space + "position : {}".format(self.position))
        print(space + "bonus : {}".format(self.bonus))
        
    def getBelowEmps(self):
        #print("base not implemented!!!")
        return None
    
    def setBelowEmps(self):
        print("base impl not done!!")
    
    def getAboveEmp(self):
        print("base impl not done!!")
        return None
    
    def update(self):
        print("base impl not done!!")
    
class CityManager(Employee):
    def __init__(self,name,id,city="ABC",salary=0.1,rating=0):
        print("{} created!!!".format(Position.CM.value))
        Employee.__init__(self,name,id,Position.CM.value,salary,rating)
        self.city = city
        #Rating:[FM List]
        self.fm_dic = {}
        self.fm_rating_dic = {}
        self.fm_list = []
        self.position = Position.CM.name
    
    def setUpFMDic(self):
        for fm in self.fm_list:
            self.fm_dic[fm.name + "_" + str(fm.id)] = fm.rating
            try:
                if fm.rating:
                    self.fm_rating_dic[fm.rating].append(fm.name + "_" + str(fm.id))
            except:
                if fm.rating:
                    self.fm_rating_dic[fm.rating] = [fm.name + "_" + str(fm.id)]
    
    def setBelowEmps(self,fm_list):
        self.fm_list = fm_list
        self.setUpFMDic()

    def printFMs(self):
        for fm in self.fm_list:
            fm.printDetails()
            print()

    def getFMRatings(self):
        return self.fm_dic
    
    def getBelowEmps(self):
        return self.fm_list
          
    def printDetails(self):
        Employee.printDetails(self,"")
        
    def getAboveEmp(self):
        return None
    
    def remove(self,emp):
        self.fm_list.remove(emp)
        
    def add(self,emp):
        self.fm_list.append(emp)
        
class FleetManager(Employee):
    def __init__(self,name,id,city="ABC",cm=None,salary=0.1,rating=0):
        print("{} created!!!".format(Position.FM.value))
        Employee.__init__(self,name,id,Position.FM.value,salary,rating)
        self.currCM = cm
        self.de_dic = {}
        self.de_rating_dic = {}
        self.de_list = []
        self.position = Position.FM.name
        self.city = self.currCM.city
        
    def setUpDEDic(self):
        for de in self.de_list:
            try:
                self.de_dic[de.name + "_" + de.id].append(de.rating)
                if de.rating:
                    self.de_rating_dic[de.rating].append(de.name + "_" + str(de.id))
            except:
                if de.rating:
                    self.de_rating_dic[de.rating] = [de.name + "_" + str(de.id)]
    
    def update(self,newCM):
        self.currCM = newCM
    
    def setBelowEmps(self,de_list):
        self.de_list = de_list
        self.setUpDEDic()
        
    def getDMRatings(self):
        return self.de_dic
    
    def getBelowEmps(self):
        return self.de_list
    
    def printDetails(self):
        space = "   "
        Employee.printDetails(self,space)
        print(space + "city : {}".format(self.city))
        
    def getAboveEmp(self):
        return self.currCM
    
    def remove(self,emp):
        self.de_list.remove(emp)
        
    def add(self,emp):
        self.de_list.append(emp)
    
class DeliveryExecutives(Employee):
    def __init__(self,name,id,city="ABC",fm=None,salary=0.1,rating=0):
        print("{} created!!!".format(Position.DE.value))
        self.currFM = fm
        Employee.__init__(self,name,id,Position.DE.value,salary,rating)
        self.position = Position.DE.name
        self.city = self.currFM.city
    
    def update(self,newFM):
        self.currFM = newFM
    
    def setBelowEmps(self,fm):
        if self.currFM and self.currFM != fm:
            print("Curr FM is already set, do you want to update FM?")
        else:
            self.currFM = fm
            #cascade above
            
    def printDetails(self):
        print()
        space = "      "
        Employee.printDetails(self,space)
        print(space + "city : {}".format(self.city))
        
    def getAboveEmp(self):
        return self.currFM
    
class SDFManagement:
    def __init__(self,city_dic):
        self.city_dic = city_dic
    
    def printHierarchy(self,emp=None):
        if type(emp).__name__ == EmpTypes.CITY_MANAGER.value:
            for city,value in self.city_dic.items():
                #print(value.keys())
                if Position.CM.value in value:
                    cms = value[Position.CM.value]
                    if emp in cms:
                        print(emp.printDetails())
                        self.printHierarchyUtil(emp.getBelowEmps())
                else:
                    print("No such employee exists...")
                    
        if type(emp).__name__ == EmpTypes.FLEET_MANAGER.value:
            for city,value in self.city_dic.items():
                #print(value.keys())
                if Position.FM.value in value:
                    cms = value[Position.FM.value]
                    if emp in cms:
                        print(emp.printDetails())
                        self.printHierarchyUtil(emp.getBelowEmps())
                else:
                    print("No such employee exists...")
        if type(emp).__name__ == EmpTypes.DELIVERY_MANAGER.value:
            for city,value in self.city_dic.items():
                #print(value.keys())
                if Position.DE.value in value:
                    cms = value[Position.DE.value]
                    if emp in cms:
                        print(emp.printDetails())
                        self.printHierarchyUtil(emp.getBelowEmps())
                else:
                    print("No such employee exists...")

    def printHierarchyUtil(self,emps):
        if not emps:
            return
        for cm in emps:
            cm.printDetails()
            self.printHierarchyUtil(cm.getBelowEmps())
            
    def distributeBonus(self,bonus,city="Bangalore"):
        if city in self.city_dic:
            self.city_dic[city][Position.CM.value][0].bonus = bonus
            fms = self.city_dic[city][Position.FM.value]
            self.distributeBonusUtil(fms,bonus,city)
        
    def distributeBonusUtil(self,emps,bonus,city):
        if not emps:
            return
        
        emp_bonus_split = self.splitMoney(emps,bonus)
        for emp, emp_bonus in zip(emps,emp_bonus_split):
            emp.bonus = round(emp_bonus,2)
            self.distributeBonusUtil(emp.getBelowEmps(),emp_bonus,city)
    
    def splitMoney(self,emps, bonus):
        ratings = []
        for emp in emps:
            ratings.append(emp.rating)
            
        sum_rating = sum(ratings)
        
        bonus_split = [bonus*rating/sum_rating for rating in ratings]
        return bonus_split
    
    def topKDEs(self,k=5):
        print("Top {} DEs are :".format(k),end=" ")
        ratios = []
        des = []
        for _, lis in self.city_dic.items():
            des.extend(lis[Position.DE.value])
            
        for de in des:
            ratios.append((de.name,round(de.bonus/de.salary,2)))
            
        ratios = sorted(ratios,key = lambda x:x[1], reverse=True)
        for i,tup in enumerate(ratios):
            if i == k:
                break
            if i == k-1:
                print(tup[0])
            else:
                print(tup[0],end=",")
                
    def transferEmployee(self,emp1,emp2):
        if emp1 != emp2:
            old_emp = emp2.getAboveEmp()
            old_emp.remove(emp2)
            emp2.update(emp1)
            emp1.add(emp2)
        else:
            print("cant transfer to the same employee :)")
        
    def promoteEmployee(self,emp,pos,city=None):
        if pos == Position.CM.name:
            if city in self.city_dic:
                print("cant have two CM in one city")
            else:
                new_emp = CityManager(emp.name,emp.id,salary = 100000,rating=4,city=city)
                self.city_dic[city][Position.CM.name] = [new_emp]
                above_emp = emp.getAboveEmp()
                above_emp.remove(emp)
                emp = None
        elif pos == Position.FM.name:
            pass
        
def main():
    cm1 = CityManager("CM1",1,salary= 100000,rating = 5,city=City.Mumbai.value)
    cm2 = CityManager("CM2",13,salary= 100000,rating = 5,city=City.Bangalore.value)
    fm1 = FleetManager("fm1",2,cm = cm1,salary= 10000,rating = 5)
    fm2 = FleetManager("fm2",3,cm = cm1,salary= 10001,rating = 5)
    fm3 = FleetManager("fm3",4,cm = cm2,salary= 10002,rating = 5)
    fm4 = FleetManager("fm4",5,cm = cm2,salary= 10003,rating = 5)
    de1 = DeliveryExecutives("de1",6,fm =fm1,salary= 100,rating = 3)
    de2 = DeliveryExecutives("de2",7,fm =fm1,salary= 101,rating = 2)
    de3 = DeliveryExecutives("de3",8,fm =fm2,salary= 102,rating = 1)
    de4 = DeliveryExecutives("de4",9,fm =fm2,salary= 103,rating = 5)
    de5 = DeliveryExecutives("de5",10,fm =fm2,salary= 104,rating = 3)
    de6 = DeliveryExecutives("de6",11,fm =fm3,salary= 1,rating = 5)
    de7 = DeliveryExecutives("de7",12,fm =fm4,salary= 106,rating = 4)
    #des = [de1,de2,de3,de4,de5,de6,de7]
    #fms = [fm1,fm2,fm3,fm4]
    #cms = [cm1,cm2]
    #de1.setBelowEmps(fm3)
    cm1.setBelowEmps([fm1,fm2])
    cm2.setBelowEmps([fm3,fm4])
    fm1.setBelowEmps([de1,de2])
    fm2.setBelowEmps([de3,de4,de5])
    fm3.setBelowEmps([de6])
    fm4.setBelowEmps([de7])
    
    city_dic = {}
    city_dic[City.Mumbai.value] = {Position.CM.value:[cm1],\
                                    Position.FM.value:[fm1,fm2],\
                                    Position.DE.value:[de1,de2,de3,de4,de5]}
    
    city_dic[City.Bangalore.value] = {Position.CM.value:[cm2],\
                                    Position.FM.value:[fm3,fm4],\
                                    Position.DE.value:[de6,de7]}
    sdfm = SDFManagement(city_dic)
    bonus = 1000
    #sdfm.printHierarchy(fm1)
    sdfm.distributeBonus(bonus,city=City.Mumbai.value)
    sdfm.distributeBonus(bonus,city=City.Bangalore.value)
    sdfm.printHierarchy(cm1)
    sdfm.printHierarchy(cm2)
    sdfm.transferEmployee(fm3,fm3)
    #sdfm.printHierarchy(cm2)
    #sdfm.promoteEmployee(de7,Position.CM.value,"Kolkata")
    sdfm.topKDEs()
    
if __name__ == "__main__":
    main()