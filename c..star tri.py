class star:
    def __triangle(self):
        for i in range(1,8):
            print("\n")
            for j in range(1,i-1):
                print(j,end=" ")
    def display(self):
        self.__triangle()
        

tria=star()
#tria.triangle()
tria.display()
