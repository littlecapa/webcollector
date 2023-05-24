import os
import shutil

import logging
logger = logging.getLogger()

def create_path(path):
    if not os.path.exists(path):
        new = True
        try: 
            os.makedirs(path)
            logger.debug(f"Created directory: {path}")
        except OSError as e:
            logger.error(f"Error creating directory: {e}")
            raise OSError(f"Error creating directory: {e}")
    else:
        new = False
        logger.debug(f"Existing path: {path}")
    return new
def path_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False
    
def file_path(path, filename):
    return (os.path.join(path, filename))

def del_all(path, secret, del_secret):
        if secret == del_secret:
            try:
                shutil.rmtree(path)
                logger.debug("Directory deleted successfully.")
            except OSError as e:
                logger.error(f"Error deleting directory: {e}")
        else:
            logger.error("Invalid Secret")