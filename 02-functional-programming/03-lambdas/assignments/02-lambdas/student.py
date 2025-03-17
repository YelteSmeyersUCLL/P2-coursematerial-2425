
def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)

def group_by_value(cards):
    return group_by(cards, lambda card: card.value)

def partition_by_color(cards):
    return partition(cards, lambda card: card.suit in {"spades", "clubs"})

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value}, {self.suit}"


def group_by(xs, key_function):
    result = {}
    for x in xs:
        key = key_function(x)
        if key not in result:
            result[key] = []
        result[key].append(x)
    return result


def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)

cards = [
    Card(2, "hearts"),
    Card(3, "spades"),
    Card(4, "diamonds"),
    Card(5, "clubs"),
    Card(6, "hearts"),
    Card(7, "spades"),
    Card(7, "diamonds"),
    Card(7, "clubs"),
    Card(7, "hearts"),
    Card("J", "spades"),
    Card("Q", "diamonds"),
    Card("K", "clubs"),
    Card("A", "hearts")
]

print(group_by_suit(cards))
print(group_by_value(cards))
print(partition_by_color(cards))