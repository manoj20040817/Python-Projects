'''
encapulation:
wrapping of varibles methods in a single
unit is called as encapulation
*public
*private __
*protected _
'''
class demo():
    def __init__(self,a,b):
       self.__a=a#private
       self._b=b#protected
    # print(__a)
    # print(_b)
class demo2(demo):
    def output(self):
        print(self._b)
d=demo2(8,9)
d.output()









