'''
    Get a overview of the structure of a variable that is nested dict of list of dict ...

    Usage:
        recur_get_keys_print(dictlist)

    Input:
    dictlist = {
         'k1': 3,
         'k2': {'kk1': 4},
         'k3': [1,2,3],
         'k4': [[1,2],3],
         'k5': {'kk5':[{'kkk1': 666},{'kkk2': 666}] },
         'k6': [[1,[{'kkk': 666},3]],3],
         'g': {'c': [[3,2],[1,1]], 'o1': 666},
         'g2': {'o1': 666, 'c': [1,1]},
    }

    Output:
        {k1

        {k2
            {kk1

        {k3
            [3

        {k4
            [2
                [2

        {k5
            {kk5
                [2
                    {kkk1

        {k6
            [2
                [2

        {g
            {c
                [2
                    [2
            {o1

        {g2
            {o1
            {c
                [2
'''

# private
def _recur_get_keys(dict_or_list, count=1):
    if type(dict_or_list) is dict:
        for key, value in dict_or_list.items():
            yield {
                'depth': count,
                'type': 'dict',
                'key': key,
                'item_count': 0,
            }

            if type(value) is dict or type(value) is list:
                for dic in _recur_get_keys(value, count+1):
                    yield dic

    elif type(dict_or_list) is list:
        yield {
            'depth': count,
            'type': 'list',
            'key': 0,
            'item_count': len(dict_or_list),
        }
        value = dict_or_list[0] # assuming all list elem are identical type
        if type(value) is dict or type(value) is list:
            for dic in _recur_get_keys(value, count+1):
                yield dic

def recur_get_keys_print(dictlist):
    for item in _recur_get_keys(dictlist): # "visualizing"
        if item['depth'] == 1:       # for clarity
            print ('')
        print ('    '*item['depth'], end='')
        if item['type'] == 'dict':
            print ('{', end='')
            print (item['key'], end='' )
        elif item['type'] == 'list':
            print ('[', end='')
            print (item['item_count'], end='' )
        print ('')
