import os
import uuid

def get_random_filename(instance, filename):
    """
    Generate a random filename for uploaded files to avoid conflicts.
    The filename will be a UUID followed by the original file extension.
    """
    ext = filename.split('.')[-1]
    # Create a random filename using UUID
    filename = f"{uuid.uuid4().hex}.{ext}"
    
    # Return the path where the file will be stored
    # This assumes you have a 'uploads/' directory in your MEDIA_ROOT
    return os.path.join('uploads', filename[0:2], filename[2:4], filename)
