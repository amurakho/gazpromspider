import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('base.csv')

    writer = pd.ExcelWriter('data.xlsx')
    df.to_excel(writer)
    writer.save()