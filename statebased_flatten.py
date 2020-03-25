
class flatenSmart:
    '''Iterrator based, Supports Reverse Iteration,State Management of Iteration.e.g Saving,Copying,Resuming Iteration State'''
    __list=list()
    __cls=None
    def copy(self):return self.__class__(self.__list,list(self.__counter),self.__cls)
    def getState(self):return list(self.__counter),self.__direction
    def setState(self,state=([0],1)):self.__counter,self.__direction=state
    def __init__(self,obj,unwrp=list,direction=-1):
        self.__cls=unwrp
        self.__list=obj
        self.__direction=1 if direction>0 else -1
        self.__counter=[0 if direction>0 else -1]
        if not hasattr(obj, '__iter__'):raise "Base Object is needs to have a __iter__ method defined."
        elif not type(obj)==unwrp:raise "Base Object should be the instance of Unwrappable class"
    def __iter__(self,sub=None):
        return self
    def __next__(self):
        direction=self.__direction
        el=self.__list
        elprev=el
        if len(self.__counter)==0:raise StopIteration
        for each in self.__counter:
            elprev=el
            try:el=el[each]
            except IndexError:
                self.__counter.pop()
                if len(self.__counter)>0:self.__counter[-1]+=1 if direction>0 else -1
                return next(self)

        else:
            if type(el)==list:
                self.__counter.append(0 if direction>0 else -1)
                return next(self)
            self.__counter[-1]+=1 if direction>0 else -1
            return el
        
