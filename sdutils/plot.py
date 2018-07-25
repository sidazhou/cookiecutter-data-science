from sdutils.df import plot_df

def plot(my_var):
    if type(my_var).__name__ == 'DataFrame':
        plot_df(my_var)
    else:
        print('type not supported')
#     elif 'matrix' in type(my_var).__name__ or (type(my_var).__name__ == 'ndarray' and len(my_var.shape) == 2):
#         describe_M(my_var)