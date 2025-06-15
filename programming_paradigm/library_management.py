class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.___is_checked_out = False
    
    def set_is_checked_out(self):
        if self.___is_checked_out == False:
            set_is_checked_out = True
        else:
            set_is_checked_out = False
    

class Library:
    def __init__(self,Books):
        self.___books = [Books]
    
    def add_book(self):
        Title = input("Enter the Book Title: ")
        Author = input("Enter the Author Name: ")

        self.___books.append(Book(Title,Author))
        print("Available books after setup:")
        self.list_available_books()
    
    def check_out_book(self,title):
        for b in self.___books:
            if b.title == title:
                b.set_is_checked_out()
        print(f"Available books after checking out '{title}':")
        self.list_available_books()
    
    def checking_in(self,title):
        for b in self.___books:
            if b.title == title:
                b.set_is_checked_out()
        print(f"Available books after returning '{title}':")
        self.list_available_books()
    
    def list_available_books(self):
        for b in self.___books:
            print(f"{b.title} By {b.author}")
        



