class Star_Cinema:
    __hall_list = []
    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)

class Hall(Star_Cinema):
    __id = 0
    __id_list = []
    __sh_list=[]
    def __init__(self,rows,cols):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__entry_hall(self)
        Hall.__id+=1
        self.__hall_no = Hall.__id
        Hall.__id_list.append(id)
    
    def entry_show(self,id,movie_name,time):
        dummy = (id,movie_name,time)
        self.__show_list.append(dummy)
        Hall.__sh_list.append(dummy)
        seat = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        self.__seats[id] = seat

    def book_seats(self,id,r,c):
        if id in Hall.__id_list:
            self.__seats[id][r-1][c-1] = 1
        else:
            return "there is no such hall"
        

    def view_show_list(self):
        for a in Hall.__sh_list:
            print("MOVIE NAME : ",a)

    def view_available_seats(self):
        print(self.__seats[self.__hall_no])

while True:
    print("1. VIEW ALL SHOW TODAY") 
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT") 
    a = int(input("ENTER OPTION : "))
    if(a==4):
        break
    if(a==2):
        b=int(input("ENTER SHOW ID : "))
        Hall.view_available_seats()
    if(a==1):
        Hall.__sh_list
    if(a==3):
        c = int(input("SHOW ID: "))
        n = int(input("NUMBER OF TICKETS: "))
        r = int(input("ENTER SEAT ROW: "))
        c = int(input("ENTER SEAT COLUMN: "))
        Hall.book_seats(c,r,c)
        
