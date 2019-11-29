class Bangladesh():
    def capital(self):
        print('Dhaka is the capital of Bangladesh')
    def Language(self):
        print('Bangla the primary language of Bangladesh')
    def type(self):
        print('Bangladesh is a developing country')

class USA():
    def capital(self):
        print('Washington, D.C. is the capital of USA')
    def Language(self):
        print('English the primary language of USA')
    def type(self):
        print('USA is a developed country')

obj_ban = Bangladesh()
obj_usa = USA()

for country in (obj_ban,obj_usa):
    country.capital()
    country.Language()
    country.type()

def func(obj):
    obj.capital()
    obj.Language()
    obj.type()

func(obj_ban)
func(obj_usa)