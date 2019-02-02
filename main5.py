import numpy as np
import pandas as pd

# load data from csv
data = pd.read_csv('./enjoysportdata/data.csv', ',')

no_of_columns = data.shape[1]
no_of_examples = data.shape[0]

# Create inital specialisation
# S -> most specific hypothesis
# G -> most generalised hypothesis
S = np.array(['phi']*(no_of_columns-1),dtype='|U10')
G = pd.DataFrame(data=[['?']*(no_of_columns-1)],columns=list(data.columns.values)[:no_of_columns-1])

print(S)
print(G)

for index, i in data.iterrows():
    if i[no_of_columns-1] == 'Y':
        for j in range(0, no_of_columns-1):

            # Generalize S
            if S[j] == 'phi':
                S[j] = i[j]
            elif S[j] == '?':
                pass
            elif S[j] != i[j]:
                S[j] = '?'

            # Specialize G
            for hypind, hyp in G.iterrows():
                if hyp[j] != '?' and hyp[j] != i[j]:
                    G.drop(hypind, inplace=True)
    else:
        # This is for 'N'
        tempdf = pd.DataFrame()
        # Specialize G
        for hypind, hyp in G.iterrows():
            accepts = True
            for j in range(0, no_of_columns-1):
                if hyp[j] == '?' or hyp[j] == i[j]:
                    pass
                elif hyp[j] != i[j]:
                    accepts = False
                    break
            if accepts:
                for j in range(0, no_of_columns - 1):
                    if hyp[j] == '?':
                        if S[j] == 'phi':
                            # add all the other values possible
                            temp_k_data = data[data.columns[j]].unique()
                            temp_values = np.delete(temp_k_data, i[j])
                            t_hyp = hyp.copy()
                            for temp_itr in temp_values:
                                t_hyp[j] = temp_itr
                                tempdf = tempdf.append(t_hyp,sort=False,ignore_index=True)
                        elif S[j] == '?':
                            pass
                        elif S[j] != i[j]:
                            t_hyp = hyp.copy()
                            t_hyp[j] = S[j]
                            tempdf = tempdf.append(t_hyp,sort=False,ignore_index=True)
                G.drop(hypind, inplace = True)
        G = G.append(tempdf,sort=False,ignore_index=True)
        G.drop_duplicates(inplace = True)
    print("For "+str(index+1)+":")
    print("S:")
    print(S)
    print("G:")
    print(G)
