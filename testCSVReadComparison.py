import json
import os.path
import logging
import pandas as pd
import json as js

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


# def writeToFile(words):
#  with open('myFile.txt','w') as file:
#   file.write(words)

def compareFromCsvFile(firstFile, secondFile):
    logging.warning('Beginning compareFromCsvFile')
    try:
        if os.path.isfile(firstFile) and os.path.isfile(secondFile):
            # We read the columns with index then fill in empty values
            dataSet = pd.read_csv(firstFile, usecols=['product_id', 'description'], skip_blank_lines=True)
            dataSet.fillna("Empty Value", inplace=True)
            # dataSet = dataSet.convert_dtypes()
            print(dataSet.nunique())
            # print(dataSet)

            compSet = pd.read_csv(secondFile, usecols=['product_id', 'description'], skip_blank_lines=True)
            compSet.fillna("Empty Value", inplace=True)
            # compSet = compSet.convert_dtypes()
            # compSet['id'] = pd.to_numeric(compSet['id'].apply(str),errors='coerse')
            print(compSet.nunique())
            # print(compSet)

            # Make the comparison,count and deposit in file as table
            # compResult = dataSet[dataSet.apply(tuple, 1).isin(compSet.apply(tuple, 1))]
            compResult = pd.merge(dataSet, compSet, on=['product_id'], how='left')
            # compResult = trainSet.merge(dataSet, on="org_id", how="left")
            print(compResult)
        else:
            logging.warning('A File Doesnt Exist')
    except Exception as e:
        logging.error('Exeption occured', exc_info=True)


def compareFromTxtFile(firstFile, secondFile):
    logging.warning('Beginning compareFromTxtFile')
    try:

        with open(firstFile, mode="r", encoding='utf8', newline='\r\n') as f:
            textData1 = pd.read_json(f, lines=True, orient='records')

        with open(secondFile, mode="r", encoding='utf8', newline='\r\n') as f:
            textData2 = pd.read_json(f, lines=True, orient='records')

        df1 = pd.DataFrame(textData1[['sku', 'name']]).convert_dtypes()
        df1['product_id'] = pd.to_numeric(df1['sku'])
        print(type(df1['product_id']))
        df2 = pd.DataFrame(textData2[['product_id', 'status']]).convert_dtypes()
        #df2['product_id'] = pd.to_numeric(df2['product_id'],errors='coerse')
        # firstJsonData = df1['sku', 'name']
        # print(firstJsonData.nunique(0))
        # secondJsonData = df2[['product_id', 'status']]
        # print(secondJsonData.nunique(0))

        #compResult = pd.merge(right=df1, left=df2,right_on='sku', left_on='product_id', how='inner')
        compResult = pd.merge(df1, df2, on=['product_id'], how='left')
        print(compResult)
        compResult.to_csv('compFile.csv',index=False)
        # print(df.nunique(0))

    except Exception as e:
        logging.error('Exeption occured', exc_info=True)


def main():
    logging.warning('Beggining testCSVReadComparison')
    try:
        # Define file path
        mainPath = "mainFile.csv"
        secondaryPath = "compFile.csv"
        textMainPath = "ProductsCoppel.txt"
        textSecondaryPath = "ProductBY.txt"
        # compareFromCsvFile(mainPath,secondaryPath)
        compareFromTxtFile(textMainPath, textSecondaryPath)

    except Exception as e:
        logging.error('Exeption occured ' + str(e), exc_info=True)


if __name__ == '__main__':
    main()
