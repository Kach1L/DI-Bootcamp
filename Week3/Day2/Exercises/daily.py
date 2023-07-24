class Pagination:
    def __init__(self,items=list(None),pageSize=int(10)):
        self.items = items
        self.pageSize = pageSize
    
    def getVisibleItems(self):
        print(self.items)
            
    def prevPage(self):
        for i in self.items:
            if self.items[i] == self.items:
                print(self.items[i-1])
            else:
                print('Not Available')
            
    def nextPage(self):
        for i in self.items:
            if self.items[i] == self.items:
                print(self.items[i+1])
            else:
                print('Not Available')
        
    def firstPage(self):
        for i in self.items:
            if self.items[i] == self.items:
                print(self.items[0])
            else:
                print('Not Available')

    def lastPage(self):
        for i in self.items:
            if self.items[i] == self.items:
                print(self.items[-1])
            else:
                print('Not Available')

    def goToPage(self, pageNum):
        for i in self.items:
            if self.items[i] == self.items:
                print(self.items[pageNum])
            else:
                print('Not Available')
    
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]