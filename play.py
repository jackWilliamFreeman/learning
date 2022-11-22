def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

pretty = ordinary()


def generator_ex(items):
    for item in items:
        yield item

i = 0
items = []
while(i <= 1000):
    items.append(i)
    i+=1

for item in generator_ex(items):
    print(item)