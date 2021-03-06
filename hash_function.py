class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.capacity = self.size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        try:
            h = self.find_key_hash(key)
            return self.data[h]
        except KeyError(key):
            raise

    def __delitem__(self, key):
        try:
            h = self.find_key_hash(key)
            self.slots[h] = None
            self.data[h] = None
            self.capacity += 1
        except KeyError("there is no such key") :
            return "there is no such key"

    def __repr__(self):
        return str(self.slots) +'\n'+str(self.data)

    def hashfunction(self, key):
        return len(key) % self.size

    def put(self, key, value):
        h = self.hashfunction(key)
        # проверяем наличие места в таблице
        if self.capacity < 3:
            self.slots += [None]
            self.data += [None]
            self.capacity += 1
        # если ячейка пустая, записываем значения
        if self.slots[h] is None:
            self.slots[h] = key
            self.data[h] = value
            self.capacity -= 1
        # иначе ищем ячейку с существующим ключем и меняем значение
        else:
            if self.slots[h] == key:
                self.data[h] = value
            else:
                next_h = h + 1
                while self.slots[next_h] is not None:
                    if self.slots[next_h] == key:
                        self.data[next_h] = value
                        break
                    next_h += 1
                self.slots[next_h] = key
                self.data[next_h] = value
                self.capacity -= 1

    def find_key_hash(self, key):
        h = self.hashfunction(key)
        while self.slots[h] is not None:
            if self.slots[h] == key:
                return h
            h += 1
        raise KeyError(key)

m = {'Batman': 280,
     'Spider man': 260,
     'Thor': 159,
     'Robin': 291,
     'Jocker': 266,
     'Hulk': 225,
     'Eagle': 283,
     'Iron Man': 152,
     'Catwoman': 215,
     'Aquaman': 142,
     'Wolverine': 248,
     'Ninja Turtles': 118,
     'Guardians of the Galaxy': 395,
     'Wonder Woman': 101,
     'Hellboy': 104}

table = MyHashTable(20)
for key, value in m.items():
    table[key] =  value

print(table['Hulk'])
print(table)

