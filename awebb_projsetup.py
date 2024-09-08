''' This module provides functions for creating a series of project folders. '''

# Start with imports from the Python Standard Library
import pathlib
import time

# Import local modules
import utils_awebb

# Declare global variables

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
##################################### 

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # Iterate over the range of years and create a folder for each year
    for year in range(start_year, end_year + 1):
        folder_path = data_path.joinpath(str(year))  # Create the folder path for each year
        folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
        print(f"Created folder: {folder_path}")  # Provide feedback to the user


#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of folder names with options to force lowercase and remove spaces.
    
    Arguments:
    folder_list -- A list of folder names to be created.
    to_lowercase -- Convert folder names to lowercase if True.
    remove_spaces -- Remove spaces from folder names if True.
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

    # Iterate over the list and create a folder for each name
    for folder_name in folder_list:
        # Apply transformations based on parameters
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")
        if to_lowercase:
            folder_name = folder_name.lower()
        
        folder_path = data_path.joinpath(folder_name)  # Create the folder path
        folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
        print(f"Created folder: {folder_path}")  # Provide feedback to the user

#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################


def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders with a given prefix added to each folder name.
    
    Arguments:
    folder_list -- A list of folder names to be prefixed and created.
    prefix -- A string to be added as a prefix to each folder name.
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

    # Use a list comprehension to create prefixed folder names
    prefixed_folders = [prefix + folder for folder in folder_list]

    # Iterate over the new list and create folders
    for folder_name in prefixed_folders:
        folder_path = data_path.joinpath(folder_name)  # Create the folder path
        folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
        print(f"Created folder: {folder_path}")  # Provide feedback to the user


#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create a folder periodically at a set interval.
    
    Arguments:
    duration_seconds -- The number of seconds to wait between creating each folder.
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    count = 0  # Counter for folder names
    
    # Create folders every few seconds
    while count < 3:  # Create 3 folders for demonstration purposes
        folder_name = f"periodic-folder-{count + 1}"  # Name folders sequentially
        folder_path = data_path.joinpath(folder_name)  # Create the folder path
        folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
        print(f"Created folder: {folder_path}")  # Provide feedback to the user
        
        count += 1  # Increment the counter
        time.sleep(duration_seconds)  # Wait for the specified duration


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # use your module function and uncomment
    # print(f"Byline: {case_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options

    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
