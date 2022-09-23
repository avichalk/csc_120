# Word of the day: abstraction

# Activity 1
class TODO_List:
    def __init__(self):
        self._todo = []
    def add_urgent(self, string):
        self._todo.append(string)
    def get_first_ten(self):
        ar = []
        i = 0
        while i < len(self._todo[:10]):
            x = (i, self._todo[i])
            ar.append(x)
            i += 1
        return ar
    def complete(self, id_1):
        self._todo.pop(id_1)

# Activity 2
class TODO_List:
    def __init__(self):
        self._todo = []
        self._ID = 1
    def add_urgent(self, string):
        self._ID += 1
        self._todo.append((self._ID, string))
    def get_first_ten(self):
        ar = []
        i = 0
        while i < len(self._todo[:10]):
            ar.append(self._todo[i])
            i += 1
        return ar
    def complete(self, id_1):
        for i in self._todo:
            if i[0] == id_1:
                self._todo.remove(i)

# Activity 3
class TODO_List:
    def __init__(self):
        self._todo = []
        self._ID = 1
        self._time = 0
        self._not_urgent = []
    def add_urgent(self, string):
        self._ID += 1
        self._todo.append((self._ID, string))
    def add_appointment(self, string, time):
        self._ID += 1
        self._not_urgent.append((time, self._ID, string))
    def update_time(self, time):
        self._time = time
        for i in self._not_urgent:
            if int(i[0]) < int(self._time):
                self._not_urgent.remove(i)
    def get_first_ten(self):
        ar = []
        ar = self._todo[:10]
        j = 10 - len(self._todo[:10])
        for j in sorted(self._not_urgent[:j]):
            ar.append(j)
        return ar
    def complete(self, id_1):
        for i in self._todo:
            if i[0] == id_1:
                self._todo.remove(i)
        for i in self._not_urgent:
            if i[0] == id_1:
                self._not_urgent.remove(i)

# Activity 4
class TODO_List:
    def __init__(self):
        self._todo = []
        self._ID = 1
        self._time = 0
        self._not_urgent = []
        self._repeating = []
    def add_urgent(self, string):
        self._ID += 1
        self._todo.append((self._ID, string))
    def add_appointment(self, string, time):
        self._ID += 1
        self._not_urgent.append((time, self._ID, string))
    def update_time(self, time):
        self._time = time
        for i in self._not_urgent:
            if int(i[0]) < int(self._time):
                self._not_urgent.remove(i)
    def get_first_ten(self):
        ar = []
        ar = self._todo[:10]
        j = 10 - len(self._todo[:10])
        for j in sorted(self._not_urgent[:j]):
            ar.append(j)
        return ar
    def complete(self, id_1):
        for i in self._todo:
            if i[0] == id_1:
                self._todo.remove(i)
        for i in self._not_urgent:
            if i[0] == id_1:
                self._not_urgent.remove(i)
    def add_repeating_event(self, string, first_time, how_often):
        self._ID += 1
        self._repeating.append([first_time, self._ID, string])