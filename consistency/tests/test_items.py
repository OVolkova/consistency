from consistency import agreement
from consistency import items
from consistency.items import item


def test_on_conll_sample_1():
    tag_tags = items.text_tags({'MISC', 'LOC', 'PER', 'ORG'}, items.iob('B', 'I'), 'O')

    sample = (['EU', 'rejects', 'German', 'call', 'to', 'boycott', 'British', 'lamb', '.'],
              ['B-ORG', 'O', 'B-MISC', 'O', 'O', 'O', 'B-MISC', 'O', 'O'],
              ['B-MISC', 'O', 'B-MISC', 'O', 'O', 'O', 'B-MISC', 'O', 'O'],
              ['B-ORG', 'O', 'O', 'O', 'O', 'O', 'B-MISC', 'O', 'O'])

    data = items.get_items_from_iob(sample, tag_tags)

    test = {'LOC': {'coder_1': [item(b=0, l=9, v=0)],
                    'coder_2': [item(b=0, l=9, v=0)],
                    'coder_3': [item(b=0, l=9, v=0)]},
            'MISC': {'coder_1': [item(b=0, l=2, v=0),
                                 item(b=2, l=1, v=1),
                                 item(b=3, l=3, v=0),
                                 item(b=6, l=1, v=1),
                                 item(b=7, l=2, v=0)],
                     'coder_2': [item(b=0, l=1, v=1),
                                 item(b=1, l=1, v=0),
                                 item(b=2, l=1, v=1),
                                 item(b=3, l=3, v=0),
                                 item(b=6, l=1, v=1),
                                 item(b=7, l=2, v=0)],
                     'coder_3': [item(b=0, l=6, v=0),
                                 item(b=6, l=1, v=1),
                                 item(b=7, l=2, v=0)]},
            'ORG': {'coder_1': [item(b=0, l=1, v=1),
                                item(b=1, l=8, v=0)],
                    'coder_2': [item(b=0, l=9, v=0)],
                    'coder_3': [item(b=0, l=1, v=1),
                                item(b=1, l=8, v=0)]},
            'PER': {'coder_1': [item(b=0, l=9, v=0)],
                    'coder_2': [item(b=0, l=9, v=0)],
                    'coder_3': [item(b=0, l=9, v=0)]}}

    assert data == test


def test_on_conll_sample_2():
    tag_tags = items.text_tags({'MISC', 'LOC', 'PER', 'ORG'}, items.iob('B', 'I'), 'O')

    sample = (['Germany', "'s", 'representative', 'to', 'the', 'European', 'Union', "'s", 'veterinary', 'committee',
               'Werner', 'Zwingmann', 'said', 'on', 'Wednesday', 'consumers', 'should', 'buy', 'sheepmeat', 'from',
               'countries', 'other', 'than', 'Britain', 'until', 'the', 'scientific', 'advice', 'was', 'clearer', '.'],
              ['B-LOC', 'I-LOC', 'O', 'O', 'O', 'B-ORG', 'I-ORG', 'I-ORG', 'O', 'O',
               'B-PER', 'I-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
               'O', 'O', 'O', 'B-LOC', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['B-LOC', 'O', 'O', 'O', 'O', 'B-ORG', 'I-ORG', 'O', 'O', 'O',
               'B-PER', 'I-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
               'O', 'O', 'O', 'B-LOC', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['B-LOC', 'O', 'O', 'O', 'O', 'B-ORG', 'I-ORG', 'O', 'O', 'O',
               'B-PER', 'I-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
               'O', 'O', 'O', 'B-LOC', 'O', 'O', 'O', 'O', 'O', 'O', 'O'])

    data = items.get_items_from_iob(sample, tag_tags)

    test = {'LOC': {'coder_1': [item(b=0, l=2, v=1),
                                item(b=2, l=21, v=0),
                                item(b=23, l=1, v=1),
                                item(b=24, l=7, v=0)],
                    'coder_2': [item(b=0, l=1, v=1),
                                item(b=1, l=22, v=0),
                                item(b=23, l=1, v=1),
                                item(b=24, l=7, v=0)],
                    'coder_3': [item(b=0, l=1, v=1),
                                item(b=1, l=22, v=0),
                                item(b=23, l=1, v=1),
                                item(b=24, l=7, v=0)]},
            'MISC': {'coder_1': [item(b=0, l=31, v=0)],
                     'coder_2': [item(b=0, l=31, v=0)],
                     'coder_3': [item(b=0, l=31, v=0)]},
            'ORG': {'coder_1': [item(b=0, l=5, v=0),
                                item(b=5, l=3, v=1),
                                item(b=8, l=23, v=0)],
                    'coder_2': [item(b=0, l=5, v=0), item(b=5, l=2, v=1), item(b=7, l=24, v=0)],
                    'coder_3': [item(b=0, l=5, v=0), item(b=5, l=2, v=1), item(b=7, l=24, v=0)]},
            'PER': {'coder_1': [item(b=0, l=10, v=0),
                                item(b=10, l=2, v=1),
                                item(b=12, l=19, v=0)],
                    'coder_2': [item(b=0, l=10, v=0),
                                item(b=10, l=2, v=1),
                                item(b=12, l=19, v=0)],
                    'coder_3': [item(b=0, l=10, v=0),
                                item(b=10, l=2, v=1),
                                item(b=12, l=19, v=0)]}}

    assert data == test
