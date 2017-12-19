from sdutils.G import describe_G
from sdutils.M import describe_M

def describe(my_var):
    print('type:', type(my_var))
    fn_str_list = ", ".join(sorted([fn_str for fn_str in my_var.__dir__() if fn_str[0] != '_']))
    print('__dir__():', fn_str_list)
    print('shape:', _getshapeof(my_var))
    print('print():', my_var)

    if type(my_var).__name__ == 'Graph':
        describe_G(my_var)
    elif 'matrix' in type(my_var).__name__ or (type(my_var).__name__ == 'ndarray' and len(my_var.shape) == 2):
        describe_M(my_var)

def _getshapeof(x):
    if type(x).__name__ in ['list', 'tuple', 'dict', 'array']: # native python
        return len(x)
    elif type(x).__name__ in ['Series', 'DataFrame', 'Panel']: # pandas
        return x.shape
    elif 'matrix' in type(x).__name__ or type(x).__name__ == 'ndarray': # scipy and numpy
        return x.shape
    else:
        return None
