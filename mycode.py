import pandas as pd
import os

data = {'name':['Alice','Bob','Charlie'],
        'Age':[25,30,30],
        'City':['New York','Los Angles','Chicago']
        }
df = pd.DataFrame(data)


# Adding new row to df for V2
new_row_loc = {'name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for V3df = pd.DataFrame(data)
# new_row_loc2 = {'Name': 'V3',
#                 'Age': 30,
#                 'City': 'City1'}
# df.loc[len(df.index)] = new_row_loc2



# Ensures that 'data' directory exits at the root level
data_dir = 'data'  # this is the folder name !!
os.makedirs(data_dir,exist_ok = True) # this ensures that no same name dir.. exits

# Define the file path
file_path = os.path.join(data_dir,'sample_data.csv')#this will create 'sample_data.csv' file inside the 'data' folder!!

# save the dataframe to csv file
df.to_csv(file_path,index = False)

print(f'csv file saved to {file_path}')