# Stage 1/6: Import & explore
## Description
Before starting to work with your data, you need to explore it first. Luckily, your data is mostly preprocessed!  
The dataset contains information about houses for sale in the following columns:

- `Price` — the price of the house. Class 0 stands for affordable housing with a price of less than 700000 euros,  
  and class `1` stands for expensive housing with the price of more than 700000 euros;
- `Area` — the area of the house;
- `Room` — how many rooms in the house;
- `Lon` — house longitude coordinates;
- `Lat` — house latitude coordinates;
- `Zip_area` — house location in the specific area of the Netherlands based on the zip code;
- `Zip_loc` — house location in a specific Amsterdam area based on the zip code.

Perform the exploratory data analysis. This step will help you to get to know the data and identify possible problems.  
EDA is meant to provide you with the insights about the data and help you better model what are you trying to predict.

## Objectives
To complete this stage:

1. Load the data into the `pandas` DataFrame;
2. Analyze the data and print the answers to the following questions:

   - How many rows does the DataFrame have?
   - How many columns does the DataFrame have?
   - Are there any missing values in the DataFrame (`True` or `False`)?
   - What is the maximum number of rooms across the houses in the dataset?
   - What is the mean area of the houses in the dataset?
   - How many unique values does column `Zip_loc` contain?

🤔 Provide each answer on a new line. Use the format shown in the Example section.

Note: if you are having issues with the provided link, you can [download the data manually](House%20Classification/task/house_class.csv).

## Example

_Example of DataFrame:_

```
     Price  Area  Room       Lon        Lat  Zip_area Zip_loc
0        0    64     3  4.907736  52.356157        10      CR
1        0    60     3  4.850476  52.348586        10      EL
2        1   109     4  4.944774  52.343782        10      SM
3        0   128     6  4.789928  52.343712        10      TH
4        1   138     5  4.902503  52.410538        10      KN
```

_Output:_

```
5
7
False
6
99.8
5
```