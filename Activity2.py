class library:
    def __init__(self , list , name):
        self.name=name
        self.booklist=list
        self.lendict={}
    def display_books(self):
        print(f"We have following books in our library. {self.name}")
        for book in self.booklist:
            print(book)
        
    def lenbook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("Lender book database has been updated , you can take the book now")
        else:
            print(f"Book is already been used by {self.lenbook[book]}")
    def add_book(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")
    def return_book(self,book):
        self.lendict.pop(book)
    

if __name__ == '__main__':


    books=library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")

    while True:
        print(f"Welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        userchoice=input()
        if userchoice not in ["1" , "2" , "3" , "4"]:
            print("Please enter a valid option")
            continue
        else:
            userchoice=int(userchoice)
        if userchoice==1:
            books.display_books()
        elif userchoice==2:
            book=input("Enter the namer of the book youwant to lend")
            user=input("Enter your name")
            books.lenbook(user,book)
        