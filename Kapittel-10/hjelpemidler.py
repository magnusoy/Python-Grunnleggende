def list_content(*args):
    for arg in args:
        print(arg)

list_content(1, 2, 3, 4, 5, 6)

def list_content(**kwargs):
    for arg in kwargs:
        print(arg)
        print(kwargs[arg])

list_content(Name="Magnus", Alder=25)