# returns a list with index for all items in the input list
# that match the input value
def index_all(ls, value):
    indices = []
    for i in range(len(ls)):
        if isinstance(ls[i], list):
            # get index from nested list
            index = index_all(ls[i], value)
            # iterate through each index in index
            for j in range(len(index)):
                # insert to the front of each index the index i
                index[j].insert(0, i)
            # extends the modified index to indices
            indices.extend(index)
        elif ls[i] == value:
            indices.append([i])
    return indices


def solution(search_list, item):
    indices = []
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            # only section of code that differs from my solution (index_all)
            # iterates through each index that is returned
            # and appends to indices:
            # the index i (as a list) followed by current index element
            for index in index_all(search_list[i], item):
                indices.append([i] + index)
    return indices
