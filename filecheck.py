import os

# Grabs all files in the Current Working Directory.
for filename in os.listdir():
    
    # Checks which files end with '.py'.
    if filename.endswith('.py'):
        
        # Prints the filenames that end with '.py', and strips the last 3 characters.
        print(filename[:-3])