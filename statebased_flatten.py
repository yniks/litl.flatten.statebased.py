class flaten:
    '''Generator based'''
    __list=list()
    __cls=None
    def __init__(self,obj,unwrp=list):
        self.__cls=unwrp
        self.__list=obj
        if not hasattr(obj, '__iter__'):raise "Base Object is needs to have a __iter__ method defined."
        elif not type(obj)==unwrp:raise "Base Object should be the instance of Unwrappable class"
    def __iter__(self,sub=None):
        if not sub:sub=self.__list
        for each in sub:
            if type(each)==self.__cls:
                for each in self.__iter__(each):
                    yield each
            else:
                yield each


class PowerFlattenIterator:

    '''Flatten Iterator,
        It Itterates over leaves of a tree
         Supports 
            -Reverse Iteration,
            -State Management of Iteration
             e.g Saving,Copying,Resuming Iteration State
    '''
    __list=list()
    __cls=None
    __direction=int()
    __counter=list()

    from Symetrical_list import SymtricalList
    class Iterator_State(list):
        def __init__(self,state=([0],1)):
            self.extend(state)
        def __gt__(self, value):
            if len(value[0])>len(self[0]):return True
            else:return value[0]>self[0]

    #StateManagement
    def copy(self):
        obj=self.__class__(self.__list,self.__cls)
        obj.setState=self.getState()
        return obj
    def getState(self):return Iterator_State((self.__counter.copy(),self.__direction,self.__def_direction))
    def setState(self,state=([0],1)):self.__counter,self.__direction,self.__def_direction=state
        
    #Initialization
    def __init__(self,obj,unwrp=SymtricalList,direction=1):
        self.__cls=unwrp
        self.__list=obj
        self.__direction=1 if direction>0 else -1
        self.__counter=[0]
        if not hasattr(obj, '__getitem__'):raise BaseException("Base Object needs to have a __getItem__ method defined.")
        if not type(obj)==unwrp:raise BaseException("Base Object should be the instance of Unwrappable class")     
    
    #Iterator Stuff
    def __iter__(self,sub=None):return self
    def __prev__(self):return self.__next__(-self.__direction)
    def __next__(self,direction=None):
        direction=direction or self.__direction
        if len(self.__counter)==0:raise StopIteration
        else:self.__counter[-1]+=direction

        element=self.__list
        for each in self.__counter:
            try:element=element[each]
            except IndexError:
                self.__counter.pop()
                return self.__next__(direction)
        else:
            if type(element)==self.__cls:
                self.__counter.append(0)
                return self.__next__(direction)
            else:return element


        
# ##DEMO
# from Symetrical_list import SymtricalList
# #Simple
# walker=PowerFlattenIterator(SymtricalList([1,2,3]))
# print(*walker)

# #Tree
# walker=PowerFlattenIterator(SymtricalList([1,2,3,[1,0,[9,786,53,[536,66452]]]]))
# print(*walker)


# #Demonstrating __prev__ with __next__
# walker=PowerFlattenIterator(SymtricalList([1,2,3]))
# print(next(walker),next(walker),next(walker),walker.__prev__(),next(walker),walker.__prev__(),next(walker),walker.__prev__(),next(walker),walker.__prev__(),next(walker),walker.__prev__())
