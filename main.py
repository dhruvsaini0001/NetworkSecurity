from networksecurity.compoents.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
import traceback

import traceback

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        
        # Pass the config to DataIngestion constructor
        data_ingestion = DataIngestion(dataingestionconfig)
        
        logging.info("Initiating data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        # Get the error message (string representation of the exception)
        error_message = str(e)
        
        # Capture the full traceback of the error
        error_details = traceback.format_exc()
        
        # Log the error message and details before raising the exception
        logging.error(f"Error Message: {error_message}")
        logging.error(f"Error Details: {error_details}")
        
        # Raise the custom exception with both the message and details
        raise NetworkSecurityException(error_message, error_details)
