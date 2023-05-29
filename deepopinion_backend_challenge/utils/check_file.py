def is_csv_file(file_path):
    """
    Checks if a file has a CSV file format based on its file extension.
    
    Parameters:
        file_path (str): The path to the file.
        
    Returns:
        bool: True if the file has a CSV file format, False otherwise.
    """
    csv_extensions = ['.csv']

    if file_path.endswith(tuple(csv_extensions)):
        return True
    else:
        return False

# if __name__ == "__main__":
#     is_csv_file('file')


def is_excel_file(file):
    """
    Checks if a file has a Excel file format based on its file extension.
    
    Parameters:
        file_path (str): The path to the file.
        
    Returns:
        bool: True if the file has a Excel file format, False otherwise.
    """
    excel_extensions = ['.xlxs']

    if file.endswith(tuple(excel_extensions)):
        return True
    else:
        return False


# if __name__ == "__main__":
#     is_excel_file('file')