from consistency import agreement
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

    assert agreement.agreement(fulldata['class_0'], text_lenght) == (0.0144, 0.0532, 0.7286)
    assert agreement.agreement(fulldata['class_1'], text_lenght) == (0.0, 0.049, 1.0)
