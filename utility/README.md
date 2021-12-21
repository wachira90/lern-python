# merge multiple excel files into a single files

## Example: 1

Method 1: Using dataframe.append()

Pandas dataframe.append() function is used to append rows of other dataframe to the end of the given dataframe, returning a new dataframe object. Columns not in the original dataframes are added as new columns and the new cells are populated with NaN value.

Syntax : DataFrame.append(other, ignore_index=False, verify_integrity=False, sort=None)

Parameters :

other : DataFrame or Series/dict-like object, or list of these

ignore_index : If True, do not use the index labels. default False.

verify_integrity : If True, raise ValueError on creating index with duplicates. default False.

sort : Sort columns if the columns of self and other are not aligned. default False.

Returns: appended DataFrame


## Example: 2

Excel Used: FoodSales1-1.xlsx, FoodSales2-1.xlsx

Method 2: Using pandas.concat()

The pandas.concat() function does all the heavy lifting of performing concatenation operations along with an axis of Pandas objects while performing optional set logic (union or intersection) of the indexes (if any) on the other axes.

Syntax: concat(objs, axis, join, ignore_index, keys, levels, names, verify_integrity, sort, copy)

Parameters:

objs: Series or DataFrame objects

axis: axis to concatenate along; default = 0 //along rows

join: way to handle indexes on other axis; default = ‘outer’

ignore_index: if True, do not use the index values along the concatenation axis; default = False

keys: sequence to add an identifier to the result indexes; default = None

levels: specific levels (unique values) to use for constructing a MultiIndex; default = None

names: names for the levels in the resulting hierarchical index; default = None

verify_integrity: check whether the new concatenated axis contains duplicates; default = False

sort: sort non-concatenation axis if it is not already aligned when join is ‘outer’; default = False

copy: if False, do not copy data unnecessarily; default = True

Returns: a pandas dataframe with concatenated data.


Example: 2

In the last example, we worked on only two Excel files with a few rows. Let’s try merging more files each containing approximately 5000 rows and 7 columns. We have 5 files BankE, BankD, BankC, BankB, BankA having historical stock data for respective bank. Let’s merge them into a single ‘Bank_Stocks.xlsx’ file. Here we are using the pandas.concat() method.
