from models.metadata import Metadata
import logging
import re

#TODO : To replace by Possible Key / Value 
def get_all_metadatas():
    metadata_list = Metadata.get_all()
    return metadata_list, 200 