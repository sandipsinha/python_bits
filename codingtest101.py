import itertools
import operator

def trim(data, delta):
    """Trims elements within `delta` of other elements in the list."""

    output = []
    last = 0

    for element in data:
        if element['value'] > last * (1 + delta):
            output.append(element)
            last = element['value']

    return output


def merge_lists(m, n):
    """
    Merges two lists into one.

    We do *not* remove duplicates, since we'd like to see all possible
    item combinations for the given approximate subset sum instead of simply
    confirming that there exists a subset that satisfies the given conditions.

    """
    merged = itertools.chain(m, n)
    return sorted(merged, key=operator.itemgetter('value'))


def approximate_subset_sum(data, target, epsilon):
    """
    Calculates the approximate subset sum total in addition
    to the items that were used to construct the subset sum.

    Modified to track the elements that make up the partial
    sums to then identify which subset items were chosen
    for the solution.

    """

    # Intialize our accumulator with the trivial solution
    acc = [{'value': 0, 'partials': [0]}]

    count = len(data)

    # Prep data by turning it into a list of hashes
    data = [{'value': d, 'partials': [d]} for d in data]
 

    for key, element in enumerate(data, start=1):
        augmented_list = [{
            'value': element['value'] + a['value'],
            'partials': a['partials'] + [element['value']]
        } for a in acc]
        print 'Augmented list', augmented_list
        acc = merge_lists(acc, augmented_list)
        print 'Merged list', acc
        acc = trim(acc, delta=float(epsilon) / (2 * count))
        print 'Triimmed list', acc
        acc = [val for val in acc if val['value'] <= target]
        print 'Final list', acc

    # The resulting list is in ascending order of partial sums; the
    # best subset will be the last one in the list.
    return acc[-1]

data = [650, 1200, 1350, 450, 2875, 1625, 1500, 1875]
target = 3450
epsilon = 0.2

print approximate_subset_sum(data, target, epsilon=epsilon)


        
