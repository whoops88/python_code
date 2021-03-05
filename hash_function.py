class Mytable:
    size = 30

    def __init__(self):
        self.data = [None] * self.size

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.data[h] is None:
            self.data[h]= {"key":key, "value":value}
            return
        h_next = h + 1
        try:    
            while self.data[h_next] is not None:
                if self.data[h_next]["key"]==key:
                    self.data[h_next]["value"]=value
                    break
                h_next+=1
        except IndexError():
            raise        
        self.data[h_next] = {"key":key, "value":value}

    def __getitem__(self, key):
        h = self.get_hash(key)
        try:
            while self.data[h]:
                if self.data[h] and self.data[h]["key"]==key:
                    return self.data[h]["value"]
                h+=1
        except IndexError:
            return 'There is no such key'

    
    def get_hash(self, name):
        return len(name) % self.size

    def delete(self, key):
        h = self.get_hash(key)
        if self.data[h]["key"]==key:
            self.data[h]=None
            return
        next_h = h + 1
        try:
            while self.data[next_h] is not None:
                if self.data[next_h]["key"]==key:
                    self.data[next_h]=None
                    break
                next_h+=1
        except IndexError:
            raise

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

table = Mytable()
for key, value in m.items():
    table[key] =  value

print(table['Hulk'])
print(table['Hellboy'])
for i in table.data:
    if i is not None:
        print(i)

