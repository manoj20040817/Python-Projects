'''
single inheritance
multilevel inheritance
multiple inheritance
hierachical inheritance

 '''
#single inheratence

# class parent():
#     def output(self):
#         print("i am the parent")
# class child(parent):
#     def out(self):
#         print("i am the child")        
# c=child()
# c.out()# child method
# c.output()#parent method

#multilevel inheritance

# class grandparent():
#     def outputgp(self):
#         print("i am the grandparent")
# class parent(grandparent):
#     def output(self):
#         print("i am the parent")
# class child(parent):
#     def out(self):
#         print("i am the child")        
# c=child()
# c.out()# child method
# c.output()#parent method
# c.outputgp()#grandparent method

#multiple inheritance

# class mother():
#     def outputm(self):
#         print("i am the mother")
# class father():
#     def output(self):
#         print("i am the father")
# class child(father,mother):
#     def out(self):
#         print("i am the child of them ")        
# c=child()
# c.out()# child method
# c.output()#father method
# c.outputm()# mother method

#herarchical inheritance

class father():
    def outputf(self):
        print("i am the father")
class child1(father):
    def output(self):
        print("i am the child1")
class child2(father):
    def out(self):
        print("i am the child2")        
c1=child1()
c2=child2()
c1.output()# method child1
c1.outputf()#father of child1 method
c2.out()# child2 method
c2.outputf()#father of child2 method








