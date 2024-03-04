# Required packages for running the script
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# A class data_mutate has been made to clean data by removing columns and setting indexes


class data_mutate:

    def __init__(self, file_name):
        # Takes datafile
        self.data = file_name
    def data_clean(self):
        # Read the text file into a DataFrame
        data_file = pd.read_csv(self.data, delimiter = '\t')

        # Set Index as miRNA column
        data_file = data_file.set_index('miRNA')

        # Remove Unnamed :13 columns
        data_file = data_file.loc[:, data_file.columns != 'Unnamed: 13']

        # Remove any data which as NA
        data_file = data_file.dropna()
        data_file = pd.DataFrame(data_file)
        # if self.options == 'only_matrix_corr':
        #     correlation_matrix = data_file.corr(method='pearson')
        #     return correlation_matrix
        # else:
        #     return data_file
        return data_file
# The corr_compute inherits methods from data_mutate class
class corr_compute(data_mutate):
    def generate_corr(self):
        # Calculate correlation_matrix and save as Dataframe
        correlation_matrix = data_mutate.data_clean(self).corr(method='pearson')
        return correlation_matrix



#####################################################################################################################
#                                This Block of code makes the files                                                 #
#####################################################################################################################

try:
######################################################################################################################
#                               Calculating correlation matrix for objects matrix1                                   #
######################################################################################################################

    matrx1 = corr_compute('matrix1.txt')
    # print(matrx1.generate_corr())

    # Save correlation data
    pd.DataFrame(matrx1.generate_corr()).to_csv('matrix1_corr.csv')

    # The matplotlib figure size
    plt.figure(figsize=(16, 14))

    # Create the heatmap using seaborn
    sns.heatmap(matrx1.generate_corr(), annot = True, cmap = 'flare', robust= True, fmt = ".2f", linewidths = .4)
    # sns.set(xlabel = 'Cancer_types', ylabel = 'Cancer_types')

    # Set plot title
    plt.title('Sample 1 Correlation between Cancer type', fontsize = 36, loc = 'center')



    # Save the plot to a file (e.g., in PNG format)
    plt.savefig('matrix_1_correlation_heatmap.png')

    # Show the plot
    # plt.show()
    # print(matrx1.generate_corr())

######################################################################################################################
#                               Calculating correlation matrix for objects matrix2                                   #
######################################################################################################################
    matrx2 = corr_compute('matrix2.txt')
    # Save correlation data
    pd.DataFrame(matrx2.generate_corr()).to_csv('matrix2_corr.csv')
    # Set up the matplotlib figure
    plt.figure(figsize=(16, 14))

    # Create the heatmap using seaborn
    sns.heatmap(matrx2.generate_corr(), annot=True, cmap='flare', robust= True, fmt=".2f", linewidths=.4)

    # Set plot title
    plt.title('Sample 2 Correlation between Cancer type', fontsize = 36, loc = 'center')

    # Save the plot to a file (e.g., in PNG format)
    plt.savefig('matrix_2_correlation_heatmap.png')

    # Show the plot
    # plt.show()


######################################################################################################################
#                               Calculating correlation between both the matrix                                      #
######################################################################################################################
    columns= matrx1.data_clean().shape[1]
    cross_corr = np.zeros((columns, columns))
    rownames = []
    for index_1,i in enumerate(matrx1.data_clean()):
        rownames.append(i)
        for index_2,j in  enumerate(matrx2.data_clean()):
            c = np.corrcoef(matrx1.data_clean()[i], matrx2.data_clean()[j])[0,1]
            cross_corr[index_1,index_2]= c

    # print(cross_corr)
    # The cross correlation data is read as pandas dataframe
    cross_dat = pd.DataFrame(cross_corr, index= rownames, columns= rownames)

    # Save to CSV file
    cross_dat.to_csv('cross_corr.csv')

    # print(new_dat)

    # Set up the matplotlib figure
    plt.figure(figsize=(16, 14))

    # Creates the heatmap using seaborn
    sns.heatmap(cross_dat, annot=True, cmap='flare', robust= True, fmt=".2f", linewidths=.4)

    # Set plot title
    plt.title('Correlation between Sample 1 and Sample 2', fontsize = 36, loc = 'center')

    # Save the plot to a file (e.g., in PNG format)
    plt.savefig('cross_correlation_heatmap.png')

    # Show the plot
    # plt.show()


    # # Correlation between both the matrix
    # with open('cross_corr.txt', 'w') as cross:
    #     cross.write(f'{matrx1.data_clean().corrwith(matrx2.data_clean())}')
except:
    print('ERROR! Files not found')

#     # print(matrx1.data_clean().corrwith(matrx2.data_clean()), axis = 1)
# x = matrx1.data_clean().to_numpy().flatten()
# y = matrx2.data_clean().to_numpy().flatten()
# print(np.corrcoef(x, y, rowvar= False))


