def delta(item1, item2):
    if ((item1.v == 1 and item2.v == 1) and
            (item1.b - item2.b) > (-item1.l) and (item1.b - item2.b) < (item2.l)):
        return (item1.b - item2.b) ** 2 + (item1.b + item1.l - item2.b - item2.l) ** 2

    elif ((item1.v == 1 and item2.v == 0) and
          (item1.b - item2.b) >= 0 and (item2.l - item1.l) >= (item1.b - item2.b)):
        return item1.l ** 2

    elif ((item1.v == 0 and item2.v == 1) and
          (item1.b - item2.b) <= 0 and (item2.l - item1.l) <= (item1.b - item2.b)):
        return item2.l ** 2

    else:
        return 0


def observed_disagreement(class_data, text_length):
    # get names of coders and number of coders
    coders = list(class_data.keys())
    n_c = len(coders)
    disagreement = 0

    # iterate by coders and items, that they have marked.
    for coder_1 in range(0, n_c):
        for item_1 in class_data[coders[coder_1]]:
            for coder_2 in range(coder_1 + 1, n_c):
                for item_2 in class_data[coders[coder_2]]:
                    # add to total disagreement
                    disagreement += delta(item_1, item_2)

    # normalize by number of coders and text length
    disagreement = 2 * disagreement / (n_c * (n_c - 1) * text_length ** 2)

    return disagreement


def expected_disagreement(class_data, class_num, text_length):
    # get names of coders and number of coders
    coders = list(class_data.keys())
    n_c = len(coders)

    # initialize variables
    disagreement = 0
    constant = (class_num - 1) / 3
    denominator = 0

    # iterate by coders and items, that they have marked.
    for coder_1 in range(0, n_c):
        for item_1 in class_data[coders[coder_1]]:
            if item_1.v == 1:
                denominator += item_1.l * (item_1.l - 1)
                numerator = constant * (2 * item_1.l ** 3 - 3 * item_1.l ** 2 + item_1.l)

                for coder_2 in range(0, n_c):
                    for item_2 in class_data[coders[coder_2]]:
                        if item_2.l >= item_1.l:
                            numerator += item_1.l ** 2 * (1 - item_2.v) * (item_2.l - item_1.l + 1)

                disagreement += numerator

    # normalize by number of coders and text length
    disagreement = (2 * disagreement / text_length) / ((n_c * text_length) * (n_c * text_length - 1) - denominator)

    return disagreement


def agreement(data, text_lenght):
    # get observed_disagreement
    d_o = observed_disagreement(data, text_lenght)

    class_sum = 0
    for _, items in data.items():
        class_sum += sum([1 for i in items if i.v == 1])
    d_e = expected_disagreement(data, class_sum, text_lenght)

    return round(d_o, 4), round(d_e, 4), round(1 - d_o / d_e if d_e else 0, 4)


