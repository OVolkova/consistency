from consistency import agreement
from consistency import alpha_agreement
from consistency.items import item


def test_delta():
    assert agreement.delta(item(b=9, l=5, v=1), item(b=7, l=8, v=1)) == 5
    assert agreement.delta(item(b=9, l=5, v=1), item(b=7, l=8, v=0)) == 25
    assert agreement.delta(item(b=9, l=5, v=1), item(b=8, l=7, v=1)) == 2
    assert agreement.delta(item(b=9, l=5, v=0), item(b=8, l=7, v=1)) == 0


def test_agreement_1():
    fulldata = {'class_0': {}, 'class_1': {}}
    fulldata['class_0']['coder_0'] = [item(150, 75, 0), item(225, 70, 1), item(295, 75, 0), item(370, 30, 1),
                                      item(400, 50, 0)]
    fulldata['class_0']['coder_1'] = [item(150, 70, 0), item(220, 80, 1), item(300, 55, 0), item(355, 20, 1),
                                      item(375, 25, 0), item(400, 20, 1), item(420, 30, 0)]
    fulldata['class_1']['coder_0'] = [item(150, 30, 0), item(180, 60, 1), item(240, 60, 0), item(300, 50, 1),
                                      item(350, 100, 0)]
    fulldata['class_1']['coder_1'] = [item(150, 30, 0), item(180, 60, 1), item(240, 60, 0), item(300, 50, 1),
                                      item(350, 100, 0)]
    text_lenght = 300

    assert alpha_agreement(fulldata['class_0'], text_lenght) == (0.0144, 0.0532, 0.7286)
    assert alpha_agreement(fulldata['class_1'], text_lenght) == (0.0, 0.049, 1.0)


def test_agreement_2():
    fulldata = {'LOC': {'coder_1': [item(b=0, l=9, v=0)],
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
    text_lenght = 9

    test_result = {'LOC': (0, 0, 0),
                   'MISC': (0.0165, 0.0399, 0.5873),
                   'ORG': (0.0082, 0.0158, 0.48),
                   'PER': (0, 0, 0)}

    for key, items in fulldata.items():
        assert alpha_agreement(items, text_lenght) == test_result[key]


def test_agreement_3():
    fulldata ={'LOC': {'coder_1': [item(b=0, l=2, v=1),
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
    text_lenght = 31



    for key, items in fulldata.items():
        print(key, alpha_agreement(items, text_lenght))

