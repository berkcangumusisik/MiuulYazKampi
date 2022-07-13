import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("car_crashes")

"""
 Görev 1 cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun. Var olan özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.
"""


def check_df(dataframe, head=5, extra_test=False):
    print("################## Shape ##################")
    print(dataframe.shape)
    print("################## Types ##################")
    print(dataframe.dtypes)
    print("################## Head ##################")
    print(dataframe.head(head))
    print("################## Tail ##################")
    print(dataframe.tail(head))
    if extra_test:
        print("################## NA ##################")
        print(dataframe.isnull().sum())
        print("################## Quantiles ##################")
        print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df, 5, True)


"""Görev 2
check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring
yazınız. (task, params, return, example)
"""
def check_df(dataframe, head=5):
    """
    Checks the dataframe.
    Parameters:
    ------
    dataframe : DataFrame
        It can be any dataframe that user prefers.
    head : int > 0
        Number of rows that wanted to be seen on the output starting from the head of the dataframe.
    Returns:
    ------
    None
    """
    print("################## Shape ##################")
    print(dataframe.shape)
    print("################## Types ##################")
    print(dataframe.dtypes)
    print("################## Head ##################")
    print(dataframe.head(head))
    print("################## Tail ##################")
    print(dataframe.tail(head))
    print("################## NA ##################")
    print(dataframe.isnull().sum())
    print("################## Quantiles ##################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


# check_df(df, head=5)

def cat_summary(dataframe, col_name, plot=False):
    """
    Parameters
    ----------
    dataframe : DataFrame
        It can be any dataframe that user prefers.
    col_name : str
        One of the columns of the dataframe.
    plot : bool
        Set True if you want to get a plot of the dataframe.
    Returns
    -------
    None
    """

    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

# cat_summary(df, "total", plot=True)
