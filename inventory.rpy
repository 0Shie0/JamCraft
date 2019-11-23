init python:
    class item:
        def __init__(s,name,grade,price,gift,craftable):
            s.name = name
            s.price = price
            s.grade = grade # 0, 1 or 2
            s.gift = gift # 1 if it is a gift or 0 if not
            s.craftable = craftable # can you craft something with it?



    class inventory:
        def __init__(s):
            s.item = [] # items you have

        def add(s,q): # to add items
            s.item.append(q)

        def remove(s,q):
            if type(q) is list:
                for i in q:
                    if type(q[i]) is item:
                        if q[i] in s.item:
                            s.item.remove(q[i])
            elif type(q) is item:
                if q in s.item:
                    s.item.remove(q)

define all_items = [item("item1",0,10,1,1),
                    item("item1",1,20,1,1),
                    item("item1",2,30,1,1),
                    item("item2",1,20,1,0),
                    item("item3",1,5,0,1)]
