import os

# Grabs all files
for filename in os.listdir():
    
    
    if filename.endswith('.py'):
        
        
        print(filename[:-3])