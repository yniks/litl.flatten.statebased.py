class SymtricalList(list):
    def __getitem__(self, index):
        if index>0:return super().__getitem__(index-1)
        elif index<0:return super().__getitem__(index)
        else:raise IndexError("Illegal Index")
