from collections import namedtuple
item = namedtuple('item', ('b', 'l', 'v'))
text_tags = namedtuple('tags', ('tags', 'iob', 'default'))
iob = namedtuple('iob', ('begin', 'end', ))
#tag_tags =  tags(set_of_tags, iob('B','I'), 'O')


def split_tag(elem, tags):
    if len(elem.split('-')) == 2:
        tag_prefix, tag = elem.split('-')
        assert tag in tags.tags
        assert tag_prefix in tags.iob
    else:
        tag = elem
        tag_prefix = None
        assert tag == tags.default
    return tag_prefix, tag


def add_item(items, coder, tag, start, n):
    if type(start) == int:
        # close opened items
        add_zero_item(items, coder, tag, start)
        items[tag][coder].append(item(b=start, l=n-start, v=1))


def add_zero_item(items, coder, tag, start):
    if items[tag][coder]:
        it = items[tag][coder][-1]
        zero_start = it.b + it.l
    else:
        zero_start = 0
    if start - zero_start:
        items[tag][coder].append(item(b=zero_start, l=start - zero_start, v=0))


def get_items_from_iob(sample, tags):
    # data = {}
    # prepare dictionary to store items by tags
    items = {}
    for tag in tags.tags:
        items[tag] = {}

    # build items for coders
    for i in range(1, len(sample)):
        # coder name
        coder = 'coder_' + str(i)

        for tag in tags.tags:
            items[tag][coder] = []

        # initialize for coder
        start = None
        prev_tag = None
        n = 0

        # iterate by document iob marks by coder to collect items
        for n, elem in enumerate(sample[i]):
            tag_prefix, tag = split_tag(elem, tags)

            if tag_prefix == tags.iob.begin:
                # close opened items
                add_item(items, coder, prev_tag, start, n)
                # open new item
                start = n

            elif not tag_prefix:
                # close opened items
                add_item(items, coder, prev_tag, start, n)
                # no open items
                start = None

            prev_tag = tag

        # close opened items
        add_item(items, coder, prev_tag, start, n)

        # add zero item to the full length of the text for all tags
        start = n + 1
        for tag in tags.tags:
            add_zero_item(items, coder, tag, start)

    return items
