class Post:
    # Class object attribute
    class_var = "abc"
    def __init__(self, name, description="Default Description", author="Admin", id=1):
        self.__name = name
        self.__description = description
        self.__author = author
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

post_a = Post("Clanak 1", "Probni clanak", "Marko Markovic")
post_b = Post(name="Clanak 2", author="Ivan Ivanovic")
# post_c = Post() # moze li ovo?
print(post_a) # zasto ovako stampa
print(post_a.get_name())
post_a.set_name("Novi opis")
print(post_a.get_name())

print(post_a.class_var)
print(post_b.class_var)
print(type(post_a))
print(Post.class_var)
