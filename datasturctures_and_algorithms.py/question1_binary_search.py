# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

def locate_card(cards, query):
    # brute force
    # position = 0
    # while position < len(cards):
    #    if cards[position] == query:
    #        return position
    #    position += 1
    #   if position == len(cards):
    #       # card not found
    #       return -1

    # binary method
    start, end = 0, len(cards) - 1
    while start <= end:
        # access the middle element
        mid_point = (start + end) // 2
        middle_card = cards[mid_point]
        print(f'Start: {start}, End: {end}, Mid: {middle_card}')
        # check if the middle element is the query
        result = test_location(cards, query, mid_point)
        if result == 'found':
            return mid_point
        # depending on the sort direction
        elif result == 'left':
            # the query is in the left half
            end = mid_point - 1
        elif result == "right":
            # the query is in the right half
            start = mid_point + 1
    # not found
    return -1


# check if the number is the first occurance in the array
def test_location(cards, query, mid_point):
    middle_card = cards[mid_point]
    if middle_card == query:
        if mid_point >= 0 and cards[mid_point - 1] == query:
            return 'left'
        else:
            return 'found'
    elif middle_card < query:
        return 'left'
    else:
        return 'right'


# test case 1
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests = []

tests.append(test)

# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)

result = locate_card(tests[1]['input']['cards'], tests[1]['input']['query'])
print(result)
