import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    Data1 = pd.read_csv('adult.data.csv')
    Data1.head(8)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =Data1["race"].value_counts()
    

    # What is the average age of men?
    average_age_men = round(Data1[Data1['sex'] == 'Male']['age'].mean(), 1)
    

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(Data1["education"].value_counts(normalize=True).loc["Bachelors"] * 100, 1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    educated_groups=[Data1[Data1["education"]=="Bachelors"],Data1[Data1["education"]=="Masters"],Data1[Data1["education"]=="Docatrate"]]

    educated_groups=pd.concat(educated_groups)

    percentage_higher_education=(len(educated_groups[educated_groups["salary"]==">50K"])/len(educated_groups))*100

    round(percentage_higher_education,1)
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    filt = Data1["education"].isin(["Bachelors", "Masters", "Doctorate"])

    higher_education = Data1.loc[filt]
    lower_education = Data1.loc[~filt]

    # percentage with salary >50K
    higher_education_rich = round((higher_education["salary"]==">50K").sum() / higher_education["salary"].count() * 100, 1)
    lower_education_rich = round((lower_education["salary"]==">50K").sum() / lower_education["salary"].count() * 100, 1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = Data1["hours-per-week"].min()
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_hours = Data1[Data1["hours-per-week"]==min_work_hours]
    rich_percentage = (num_min_hours["salary"]==">50K").sum() / len(num_min_hours) * 100

    # What country has the highest percentage of people that earn >50K?
    country_earn_50K = Data1.loc[Data1["salary"]==">50K"]["native-country"].value_counts() / Data1["native-country"].value_counts() * 100
    highest_earning_country = country_earn_50K.idxmax()
    highest_earning_country_percentage = round(country_earn_50K.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = Data1[Data1["native-country"] == "India"]
    rich_indians = rich_indians[rich_indians["salary"] == ">50K"]
    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()   
    
  # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
