
class flatenSmart:
    '''Iterrator based, Supports Reverse Iteration,State Management of Iteration.e.g Saving,Copying,Resuming Iteration State'''
    __list=list()
    __cls=None
    __direction=int()
    __counter==list()
    def copy(self):
        obj=self.__class__(self.__list,self.__cls)
        obj.setState=self.getState()
        return obj
    
    def getState(self):return list(self.__counter),self.__direction
    
    def setState(self,state=([0],1)):self.__counter,self.__direction=state
        
    def __init__(self,obj,unwrp=list,direction=1):
        self.__cls=unwrp
        self.__list=obj
        self.__direction=1 if direction>0 else -1
        self.__counter=[0 if direction>0 else -1]
        if not hasattr(unwrp, '__getItem__'):raise "Base Object needs to have a __getItem__ method defined."
        if not type(obj)==unwrp:raise "Base Object should be the instance of Unwrappable class"
            
    def __iter__(self,sub=None):return self
    
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
        
