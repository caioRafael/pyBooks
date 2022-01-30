class Book: 
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def create():

        title = input("informe o titulo do livro: ")
        price = input("quanto custa: ")
        author = input("quem escreveu esse livro: ")

        book = Book(title, price, author)
        return book

    def list(books):
        for book in books:
            print("-----------------------------")
            print("Titulo: " + book.title)
            print("Preço: " + book.price)
            print("Autor: " + book.author)
            print("-----------------------------")

def menu():
    print("------Opções------")
    print("1-Listar livros")
    print("2-Cadastrar livro")
    print("0-Sair")


print("-----------Bem vindo á livraria RG!-----------")

books = []

while True:
    menu()
    option = input()

    if option == '1':
        print("lsitar")
        Book.list(books)
    elif option == '2':
        print("cadastrar")
        newBook = Book.create()
        books.insert(len(books),newBook)
    elif option == '0':
        print("encerrando aplicação")
        break
    else:
        print("comando não encontrado")
        