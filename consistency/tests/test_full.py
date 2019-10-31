from consistency.items import text_tags, iob
from consistency import alpha_agreement, get_items_from_iob2


def test_full_1():
    tag_tags = text_tags({'MISC', 'LOC', 'PER', 'ORG'}, iob('B', 'I'), 'O')

    sample = (['EU', 'rejects', 'German', 'call', 'to', 'boycott', 'British', 'lamb', '.'],
              ['B-ORG', 'O', 'B-MISC', 'O', 'O', 'O', 'B-MISC', 'O', 'O'],
              ['B-MISC', 'O', 'B-MISC', 'O', 'O', 'O', 'B-MISC', 'O', 'O'],
              ['B-ORG', 'O', 'O', 'O', 'O', 'O', 'B-MISC', 'O', 'O'])

    test_result = {'LOC': (0, 0, 0),
                   'MISC': (0.0165, 0.0399, 0.5873),
                   'ORG': (0.0082, 0.0158, 0.48),
                   'PER': (0, 0, 0)}

    data = get_items_from_iob2(sample, tag_tags)
    for key, items in data.items():
        assert alpha_agreement(items, len(sample[0])) == test_result[key]


def test_full_2():
    tag_tags = text_tags({'MISC', 'LOC', 'PER', 'ORG'}, iob('B', 'I'), 'O')

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

    test_result = {'LOC': (0.0007, 0.0057, 0.879),
                   'MISC': (0.0, 0.0, 0),
                   'ORG': (0.0007, 0.0101, 0.9311),
                   'PER': (0.0, 0.0074, 1.0)}

    data = get_items_from_iob2(sample, tag_tags)
    for key, items in data.items():
        assert alpha_agreement(items, len(sample[0])) == test_result[key]
