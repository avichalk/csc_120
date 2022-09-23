# Activity 1 and 3
class Counter:
    def __init__(self):
        self.count = 0
    def click(self):
        self.count += 1
    def reset(self):
        self.count = 0
    def get_count(self):
        return self.count

# Activity 2
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
for i in range(2):
    counter1.click()
print(counter1.get_count())
for i in range(4):
    counter2.click()
print(counter2.get_count())
for i in range(6):
    counter3.click()
print(counter3.get_count())

# Word of the day - pain