class MyDict:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]
my_dict = MyDict({"name": "Alice", "age": 25})
print(my_dict["name"])
print(my_dict["age"]) 