import pandas as pd
import numpy as np
import random
import os
import json, xmltodict

def makeData(num_cols, nums_headers, is_ascii, sort, empty_entry):
    headers = []
    data = None
    rows = 50

    if(is_ascii == "ascii"):
        # ascii
        for j in range(0, nums_headers):
            sub_header = []
            for i in range(0, num_cols):
                sub_header.append(i)
            headers.append(sub_header)
    
        data = np.random.randint(0, 100, size=(rows, num_cols))
    else:
        # unicode
        for j in range(0, nums_headers):
            sub_header = []
            for i in range(0, num_cols):
                sub_header.append(i)
            headers.append(sub_header)
    
        for i in range(0, rows):
            temp_arr = []
            for j in range(0, num_cols):
                temp_arr.append(randomUnicode())
        #    data.append(temp_arr.decord("utf-8"))
        data = np.random.randint(0, 100, size=(rows, num_cols))

    df = pd.DataFrame(data, columns=headers)

    if(sort == 'sorted'):
        df = df.sort_values(by=df.columns[0], ascending=True).drop_duplicates(df.columns[0])
    elif(sort == 'unsorted'):
        df = df.drop_duplicates(df.columns[0])
        df = df = df.sample(frac=1)
    else:
        # duplicates
        df = df.append(df.iloc[0])
    
    if(empty_entry):
        df.iloc[-1, df.columns.get_loc(0)] = np.NaN

    return df


def randomUnicode():
    rand = random.randint(0, 65536)
    return chr(rand)

def generateTestFiles():
    path_csv = "../TestData/TestFiles/"
    path_json = "../TestData/ExpectedOutput/"
    file_name = "test"
    csv_postfix = ".csv"
    json_postfix = ".json"
    delimeter = None
    
    test_file = open('TestCases.json', 'r')
    data = json.loads(test_file.read())
    test_set = data['System'] 
    test_set = test_set['Testset']
    for test in test_set['Testcase']:
        #print(test['Value'][1])
        if(test['Value'][1] == 'valid_delimeters'):
            delimeter = ';'
        elif(test['Value'][1] == 'invalid_delimeters'):
            
        result = makeData(5, 3, 'not', 'duplicate', True)
        result.to_csv(path_csv+file_name+i+csv_postfix, sep=delimeter_valid, index=False)
        result.to_json(path_json+file_name+i+json_postfix, orient='records')
    

if __name__ == "__main__":
    generateTestFiles()
    
