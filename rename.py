import os

# Replace 'path_to_directory' with the actual path of your directory
path_to_directory = 'C:/Users/User/AppData/Roaming/Notepad++/backup'

def rename_files(directory):
    for filename in os.listdir(directory):
        # Check if the entry is a file
        if os.path.isfile(os.path.join(directory, filename)):
            # Split the filename by "@" and keep the part before "@"
            new_filename = filename.split('@')[0]
            
            # Construct the new path
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(os.path.join(directory, filename), new_path)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == '__main__':
    rename_files(path_to_directory)
