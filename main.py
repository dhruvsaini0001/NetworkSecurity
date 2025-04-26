from networksecurity.compoents.data_ingestion import DataIngestion
from networksecurity.compoents.data_validation import DataValidation
from networksecurity.compoents.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
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
        logging.info("Data initiation completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiating data validation")
        datavalidationartifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(datavalidationartifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(datavalidationartifact,data_transformation_config)
        logging.info("Initiating data Transformation")
        datatransforamtionartifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed")
        print(datatransforamtionartifact)





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
