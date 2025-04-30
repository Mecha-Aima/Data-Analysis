import pandas as pd


def calculate_demographic_data(print_data=True):
    """
    Calculate demographic data from a source (e.g., a CSV file).

    Parameters:
        :param print_data (bool): Whether to print the results to the console.

    Returns:
        A dictionary with the following keys:
            race_count (pd.Series): Number of each race.
            average_age_men (float): Average age of men.
            percentage_bachelors (float): Percentage with Bachelor's degrees.
            higher_education_rich (float): Percentage with higher education that earn >50K.
            lower_education_rich (float): Percentage without higher education that earn >50K.
            min_work_hours (int): Minimum number of hours a person works per week.
            rich_percentage (float): Percentage of the people who work the minimum number of hours per week have a salary of >50K.
            highest_earning_country (str): Country with highest percentage of people that earn >50K.
            highest_earning_country_percentage (float): Highest percentage of rich people in country.
            top_IN_occupation (str): Top occupations in India.
    """
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts('race')

    # What is the average age of men?
    males = df['sex'] == 'Male'
    average_age_men = round(df[males].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    education_count = df['education'].value_counts()
    percentage_bachelors = round((education_count['Bachelors'] / education_count.sum()) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))]
    lower_education = df[~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))]

    # percentage with salary >50K
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K']['salary'].count() / higher_education['salary'].count()) * 100
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K']['salary'].count() / lower_education['salary'].count()) * 100
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]['salary'].count()

    rich_percentage = (num_min_workers / df[df['hours-per-week'] == min_work_hours]['salary'].count()) * 100

    # What country has the highest percentage of people that earn >50K?
    rich_people = df[df['salary'] == '>50K']
    total_people_per_country = df['native-country'].value_counts()
    rich_people_per_country = rich_people['native-country'].value_counts()
    rich_people_percentage = (rich_people_per_country / total_people_per_country) * 100

    highest_earning_country = rich_people_percentage.idxmax()
    highest_earning_country_percentage = round(rich_people_percentage.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    occupation_counts = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts()
    top_IN_occupation = occupation_counts.idxmax()


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

calculate_demographic_data()