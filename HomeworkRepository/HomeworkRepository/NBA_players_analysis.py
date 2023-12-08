import pandas as pd

file_paths = [
    "./data/1_lebron_james_shot_chart_1_2023.csv",
    "./data/2_james_harden_shot_chart_2023.csv",
    "./data/3_stephen_curry_shot_chart_2023.csv"
]

# Reading the data
lebron_data = pd.read_csv(file_paths[0])
harden_data = pd.read_csv(file_paths[1])
curry_data = pd.read_csv(file_paths[2])

# Displaying the first few rows of each dataset to understand their structure
lebron_data.head(), harden_data.head(), curry_data.head()

# Function to calculate average shooting percentage
def calculate_shooting_percentage(data):
    total_shots = len(data)
    made_shots = len(data[data['result'] == True])
    shooting_percentage = (made_shots / total_shots) * 100 if total_shots > 0 else 0
    return shooting_percentage

# Calculating the average shooting percentages for each player
lebron_shooting_percentage = calculate_shooting_percentage(lebron_data)
harden_shooting_percentage = calculate_shooting_percentage(harden_data)
curry_shooting_percentage = calculate_shooting_percentage(curry_data)

print(f"Average shooting percentages:\nLeBron James: {lebron_shooting_percentage}%\nJames Harden: {harden_shooting_percentage}%\nStephen Curry: {curry_shooting_percentage}%\n")

# Function to calculate 3-point shooting percentage
def calculate_three_point_percentage(data):
    three_point_shots = data[data['shot_type'] == 3]
    total_three_point_shots = len(three_point_shots)
    made_three_point_shots = len(three_point_shots[three_point_shots['result'] == True])
    three_point_percentage = (made_three_point_shots / total_three_point_shots) * 100 if total_three_point_shots > 0 else 0
    return three_point_percentage

# Calculating the 3-point shooting percentages for each player
lebron_three_point_percentage = calculate_three_point_percentage(lebron_data)
harden_three_point_percentage = calculate_three_point_percentage(harden_data)
curry_three_point_percentage = calculate_three_point_percentage(curry_data)

print(f"Three-point shooting performance:\nLeBron James: {lebron_three_point_percentage}%\nJames Harden: {harden_three_point_percentage}%\nStephen Curry: {curry_three_point_percentage}%\n")

# Function to filter data for the fourth quarter and calculate shooting percentage
def calculate_fourth_quarter_performance(data):
    fourth_quarter_data = data[data['qtr'] == '4th Qtr']
    return calculate_shooting_percentage(fourth_quarter_data)

# Calculating the shooting performance in the fourth quarter for each player
lebron_fourth_quarter_percentage = calculate_fourth_quarter_performance(lebron_data)
harden_fourth_quarter_percentage = calculate_fourth_quarter_performance(harden_data)
curry_fourth_quarter_percentage = calculate_fourth_quarter_performance(curry_data)

print(f"Key moment performance (4th quarter):\nLeBron James: {lebron_fourth_quarter_percentage}%\nJames Harden: {harden_fourth_quarter_percentage}%\nStephen Curry: {curry_fourth_quarter_percentage}%\n")

# Function to analyze shooting performance based on score lead
def analyze_performance_based_on_score_lead(data):
    # Dividing data based on lead
    leading_data = data[data['lead'] == True]
    trailing_data = data[data['lead'] == False]
    close_game_data = data[abs(data['lebron_team_score'] - data['opponent_team_score']) <= 5]

    # Calculating shooting percentages
    leading_percentage = calculate_shooting_percentage(leading_data)
    trailing_percentage = calculate_shooting_percentage(trailing_data)
    close_game_percentage = calculate_shooting_percentage(close_game_data)

    return leading_percentage, trailing_percentage, close_game_percentage

# Analyzing LeBron James's performance based on score lead
lebron_leading_percentage, lebron_trailing_percentage, lebron_close_game_percentage = analyze_performance_based_on_score_lead(lebron_data)

# Analyzing James Harden's performance based on score lead
harden_leading_percentage, harden_trailing_percentage, harden_close_game_percentage = analyze_performance_based_on_score_lead(harden_data)

# Analyzing Stephen Curry's performance based on score lead
curry_leading_percentage, curry_trailing_percentage, curry_close_game_percentage = analyze_performance_based_on_score_lead(curry_data)

print(f"Performance against different defensive strategies:\nLeBron James: \nWhen ahead:{lebron_leading_percentage}%\nWhen trailing:{lebron_trailing_percentage}%\nSmaller point differentials (5 points or less): {lebron_close_game_percentage}%\n")
print(f"Performance against different defensive strategies:\nJames Harden: \nWhen ahead:{harden_leading_percentage}%\nWhen trailing:{harden_trailing_percentage}%\nSmaller point differentials (5 points or less): {harden_close_game_percentage}%\n")
print(f"Performance against different defensive strategies:\nStephen Curry: \nWhen ahead:{curry_leading_percentage}%\nWhen trailing:{curry_trailing_percentage}%\nSmaller point differentials (5 points or less): {curry_close_game_percentage}%\n")

# Function to analyze shooting performance in specific quarters
def analyze_performance_in_quarters(data, quarters):
    performance = {}
    for quarter in quarters:
        quarter_data = data[data['qtr'] == quarter]
        quarter_performance = calculate_shooting_percentage(quarter_data)
        performance[quarter] = quarter_performance
    return performance

# Analyzing performance in the first and last quarters
quarters_to_analyze = ['1st Qtr', '4th Qtr']
lebron_quarter_performance = analyze_performance_in_quarters(lebron_data, quarters_to_analyze)
harden_quarter_performance = analyze_performance_in_quarters(harden_data, quarters_to_analyze)
curry_quarter_performance = analyze_performance_in_quarters(curry_data, quarters_to_analyze)

print(f"Performance in different phases of the game (first and last quarters):\nLeBron James: {lebron_quarter_performance}\nJames Harden: {harden_quarter_performance}\nStephen Curry: {curry_quarter_performance}\n")
