def checking_numbers_func(nums_list):
    positive_list = []
    negative_list = []

    for num in nums_list:
        if num < 0:
            negative_list.append(num)
        else:
            positive_list.append(num)

    sum_of_positives = sum(positive_list)
    sum_of_negatives = sum(negative_list)

    print(sum_of_negatives)
    print(sum_of_positives)

    return [sum_of_positives, sum_of_negatives]


def check_the_stronger(positives, negatives):
    if positives > abs(negatives):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


all_numbers = [int(x) for x in input().split()]
sum_positives, sum_negatives = checking_numbers_func(all_numbers)

check_the_stronger(sum_positives, sum_negatives)

# 1 2 -3 -4 65 -98 12 57 -84

# 1 2 3
