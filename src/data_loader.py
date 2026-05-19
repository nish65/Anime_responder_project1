import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):   #Initializing the values
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):           #Fetching the csv files by encoding, skippin the bad line and dropping the null values 
        df = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()

        required_cols = {'Name' , 'Genres','sypnopsis'}  #From the csv files we are fetching the these 3 columns as required columns

        missing = required_cols - set(df.columns)   #Checking with csv files whether these 3 required columns exist or not in csv files, if not it will raise an error
        if missing:
            raise ValueError("Missing column  in CSV File")
        
        df['combined_info'] = (   #Creating a one more column by using csv file
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv , index=False,encoding='utf-8')  #The combained column will be added to processed_csv file

        return self.processed_csv #returing the self.processed_csv file