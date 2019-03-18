class item(object):
    def __init__(self, n, v, w, v_w):
        self.name = n
        self.value = v
        self.weight = w
        self.v_w = v_w

def get_items():
    items=[]
    items.append(item('Clock', 175, 10, 17.5))
    items.append(item('Painting', 90, 9, 10))
    items.append(item('Radio', 20, 4, 5))
    items.append(item('Vase', 50, 2, 25))
    items.append(item('Book', 10, 1, 10))
    items.append(item('Computer', 200, 20, 10))
    return items

def print_items(items):
    for item in items:
        print(item.name,item.value)

def sort_my_items(items):
        return sorted(items,key=lambda item:item.name,reverse=True)

def test():
    items=get_items()
    print_items(items)
    print("--- sorted items ---")
    items=sort_my_items(items)
    print_items(items)

def get_list_for_burglar(items,maxWeight):
    result=[]
    totalValue,totalWeight=0,0
    for i in range(len(items)):
        if(totalWeight+items[i].weight <=maxWeight):
            result.append(items[i])
            totalWeight=totalWeight+items[i].weight
            totalValue=totalValue+items[i].value

    return(result,totalValue)

def print_result(items_2):
    for item_1 in items_2[0]:
        print(item_1.name)
    print(items_2[1])


items_1=get_items()
items_2=get_list_for_burglar(items_1,20)
print_result(items_2)