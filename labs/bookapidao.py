import requests
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

# create a book
def createBook(book):
    book = {
        "Author":"test",
        "Title":"test title",
        "Price": 123
    }
    response = requests.post(url,json=book)
    return response.json()

def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__== "__main__":
    bookdiff = {
        "Price": 1000000
    } 
    print(getAllBooks())
    #print(getBookById(1))
    #print(deleteBook(498))
    #print(createBook({}))
    #print(updateBook(501, bookdiff))