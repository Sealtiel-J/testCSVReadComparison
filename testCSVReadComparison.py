import os.path
import logging
import pandas as pd

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
        with open(firstFile, "r") as f:
            textData = pd.read_json(f, lines=True, orient='records')
        df = pd.DataFrame(textData)
        firstJsonData = df[['id', 'sku']]
        print(firstJsonData.nunique(0))
        # textData.to_csv('compFile.csv',index=False)
        # print(df.nunique(0))


    except Exception as e:
        logging.error('Exeption occured', exc_info=True)


def main():
    logging.warning('Beggining testCSVReadComparison')
    try:
        # Define file path
        mainPath = "mainFile.csv"
        secondaryPath = "compFile.csv"
        textFilePath = "EjemploCanonico.txt"
        # compareFromCsvFile(mainPath,secondaryPath)
        compareFromTxtFile(textFilePath, secondaryPath)

    except Exception as e:
        logging.error('Exeption occured', exc_info=True)


if __name__ == '__main__':
    main()
