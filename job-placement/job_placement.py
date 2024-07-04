import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('job_placement_data.csv')


# importance of work experience
# 1) divide by status (placed or not)
# 2) how many people of the two categories had previous working experiences

df_placed = df.loc[df.status == 'Placed']
df_notplaced = df.loc[df.status == 'Not Placed']

placed_experience = df_placed.groupby('workex').workex.count()
notplaced_experience = df_notplaced.groupby('workex').workex.count()

# graph of placed people
slice_placed = [placed_experience.iloc[i] for i in range(len(placed_experience))]
labels_placed = [placed_experience.index[i] for i in range(len(placed_experience))]
plt.pie(slice_placed, labels=labels_placed)
plt.title('Prior experiences of placed people')
plt.show()

# graph of non placed people
slice_nonplaced = [notplaced_experience.iloc[i] for i in range(len(notplaced_experience))]
labels_nonplaced = [notplaced_experience.index[i] for i in range(len(notplaced_experience))]
plt.pie(slice_nonplaced, labels=labels_nonplaced)
plt.title('Prior experiences of non placed people')
plt.show()


# mean degree percentage for placed and not placed
print('Mean degree percentage for placed people:', df_placed.degree_p.mean())
print('Mean degree percentage for non placed people:', df_notplaced.degree_p.mean())


# salary for degree
df_degree = df_placed.groupby('degree_t').salary.mean()
x = [df_degree.index[i] for i in range(len(df_degree))]
y = [df_degree.iloc[i] for i in range(len(df_degree))]
plt.bar(x, y, width=0.35, color='y', edgecolor='k')
plt.xlabel('Obtained degree', labelpad=15)
plt.ylabel('Average salary', labelpad=15)
plt.show()

# salary men vs women
gender_salary = df_placed.groupby('gender').salary.mean()
print(gender_salary)
x = [gender_salary.index[i] for i in range(len(gender_salary))]
y = [gender_salary.iloc[i] for i in range(len(gender_salary))]
plt.bar(x, y, width=0.3, color='g', edgecolor='r')
plt.ylabel('Average salary')
for i in range(len(gender_salary)):
    plt.text(x[i], y[i]+10000, y[i], color='r')
plt.show()

# plt.text(maxRowInf,yInfection_ita[maxRowInf], maxInfections, color='#FF00FF')