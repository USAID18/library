class library:
  
 def __init__(self,list_of_book,name):
  self.booklist=list_of_book
  self.name=name
  self.leadDict={}


 def displaybooks(self):
    
    print(f"we have this books in our librarywe:{self.name}")
    for book in self.booklist:
        print(book)

def lendbook(self,user,book):
  if book not in self.booklist:
    print("sorry we donot have this book")

  elif book in self.leadDict:
         print("bieng used{self.leadDict[book]}")
        
  else:

    self.leadDict[book]=user
    print("enter youe name")


def addbook(self,book):
  self.booklist.append(book)
  print(f"{book} new book added to the collection")

def returnbook(self,book):
     if  book in self.leadDict:
       del self.leadDict[book]
       print("book has returned")

     else:
         print("was'nt borrowed from us")
 
if __name__='__main__':
  books=library(['python','rich dad por dad','algorithms by ix'],"lets update")

  user_name=input("welcom please enter your name")