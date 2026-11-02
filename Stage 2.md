# Stage 2/6: Split the data
## Description
In the previous stage, you got to know the data. As there are no problems with it, we can move on. The next step is to  
create a training and test split to further proceed with our ML pipeline.

Ensure that the categorical column with a lot of unique values (in this case, it is the `Zip_loc` column) has all of those  
unique values in the training set. This issue may be addressed with the `stratify` option in the `train_test_split` function  
from `scikit-learn` library.

## Objectives
Continue to work with the data from the previous stage. To complete this stage:

1. Import train_test_split from scikit-learn;  

2. Create two separate datasets:
   - The `X` dataset for the following columns `Area`, `Room`, `Lon`, `Lat`, `Zip_area`, and `Zip_loc`;
   - The `y` dataset for the `Price` target column;  

3. Split the two datasets using the `train_test_split` function. The test data proportion is 30%. Set the `stratify`  
   parameter to `X['Zip_loc'].values`, `random_state` to `1`. Note that this will create a total of four separate datasets;  

4. Print the value count dictionary of the `Zip_loc` column in the final training dataset.

## Example
_Example of training dataset:_

```
     Area  Room       Lon        Lat  Zip_area Zip_loc
499   102     5  4.983162  52.294189        11      LD
535    79     3  5.009082  52.351935        10      LD
88    220     5  4.920481  52.366984        10      AW
388    93     3  4.875949  52.366908        10      HA
689    81     3  4.810853  52.354008        10      ND
```

_Output:_

```
{"LD": 2, "AW": 1, "HA": 1, "ND": 1}
```