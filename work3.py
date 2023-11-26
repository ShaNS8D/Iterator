class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_list = self.flatten_list(list_of_lists)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list_of_list):
            item = self.list_of_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten_list(self, input_list):
        flattened = []
        for item in input_list:
            if isinstance(item, list):
                flattened.extend(self.flatten_list(item))
            else:
                flattened.append(item)
        return flattened


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()