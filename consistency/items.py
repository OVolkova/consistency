from collections import namedtuple
item = namedtuple('item', ('b', 'l', 'v'))
text_tags = namedtuple('tags', ('tags', 'iob', 'default'))
iob = namedtuple('iob', ('begin', 'end', ))
TAG_SEP = '-'


def split_tag(elem, tags):
    """
    split IOB2-format tag on iob-prefix and tag
    assert if default tag('O') is not allowed default tag
    assert if iob-prefix not in allowed prefixes
    assert if tag not in allowed tags
    :param elem: tag to process
    :param tags: config for tags: set of tags, iob-begin and -intermediate tags, default tag when no class is marked
                ({set_of_tags}, iob('B','I'), 'O'
    :return: iob-prefix and tag. if tag is default, iob-prefix is None
    """
    splited_tag = elem.split(TAG_SEP)
    if len(splited_tag) > 1:
        tag_prefix, tag = splited_tag
        assert tag in tags.tags
        assert tag_prefix in tags.iob
    else:
        tag = elem
        tag_prefix = None
        assert tag == tags.default
    return tag_prefix, tag


def add_item(items, coder, tag, start, n):
    """
    # if there are a start position, then add default-tag item till that start position
    and add found-tag item form start with length n
    :param items: items of all classes of all coders
    :param coder: coder id
    :param tag: class that should be modified now
    :param start: position at which default class has started
    :param n: length of the item to be added
    """
    if start is not None:
        # close opened items
        add_zero_item(items, coder, tag, start)  # default tag
        items[tag][coder].append(item(b=start, l=n-start, v=1))  # found tag


def add_zero_item(items, coder, tag, start):
    """
    add default class to the coder items.
    Changes the list - items
    :param items: items of all classes of all coders
    :param coder: coder id
    :param tag: class that should be modified now
    :param start: position at which default class has started
    """
    if items[tag][coder]:
        it = items[tag][coder][-1]
        zero_start = it.b + it.l
    else:
        zero_start = 0
    if start - zero_start:
        items[tag][coder].append(item(b=zero_start, l=start - zero_start, v=0))


def get_items_from_iob2(annotations, tags):
    """
    Convert IOB2 markup format to items.
    That allows to operate in tokens, not in symblos, for agreement metric later.
    :param annotations: list of text and marks of several coders. (first dim - text, next - coders annotations)
    :param tags: config for tags: set of tags, iob-begin and -intermediate tags, default tag when no class is marked
                ({set_of_tags}, iob('B','I'), 'O')
    :return: {'class_name': { 'coder_id': [list of items]}}
    """
    # prepare dictionary to store items by tags
    items = {}
    for tag in tags.tags:
        items[tag] = {}

    # build items for coders ()
    for i in range(1, len(annotations)):
        # coder name
        coder = 'coder_' + str(i)

        for tag in tags.tags:
            items[tag][coder] = []

        # initialize for coder
        start = None
        prev_tag = None
        n = 0

        # iterate by document iob marks by coder to collect items
        for n, elem in enumerate(annotations[i]):
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
