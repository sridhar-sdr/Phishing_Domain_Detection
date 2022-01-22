import datetime
import re
import configparser
import boto3
from pandas import read_csv
import os

class Data_Handler:
    
    def file_name_generator(self,file_name, file_extension): 
        """
        Generates a file name with the current date and time.
        """
        return file_name + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + file_extension


    def csv_seperator_rows(self,csv_file_path,number_of_files=10,sep=',',size=10000):
        """
        Seperates the rows of a csv file.
        """
        df= read_csv(csv_file_path, sep=sep)
        
        
        for i in range(number_of_files):
                df_1 = df[size*i:size*(i+1)]
                df_1.to_csv(f'G:\Phishing_Domain_Detection\src\Raw_Data\{self.file_name_generator("Phishing", ".csv")}', index=False)
    
        
        
                   
if __name__ == '__main__':
    
    cv = Data_Handler()
    config = configparser.ConfigParser()
    config.read('src\config.ini')
    access_key = config['s3_bucket']['access_key']
    secret_key = config['s3_bucket']['secret_key']

    #cv.csv_seperator_rows("G:\Phishing_Domain_Detection\src\Raw_Data\dataset_full.csv",number_of_files=10,sep=',',size=10000)
    client = cv.s3_client_initialize(access_key, secret_key)
    cv.s3_bucket_upload("G:\\Phishing_Domain_Detection\\src\\Raw_Data\\",bucket_name='phishingdomain')