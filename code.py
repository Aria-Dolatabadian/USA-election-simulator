import geopandas as gpd
import matplotlib.pyplot as plt

# Define the number of electoral votes per state
electoral_votes = {
    'Alabama': 9, 'Alaska': 3, 'Arizona': 11, 'Arkansas': 6, 'California': 54, 'Colorado': 10,
    'Connecticut': 7, 'Delaware': 3, 'Florida': 30, 'Georgia': 16, 'Hawaii': 4, 'Idaho': 4,
    'Illinois': 19, 'Indiana': 11, 'Iowa': 6, 'Kansas': 6, 'Kentucky': 8, 'Louisiana': 8,
    'Maine': 4, 'Maryland': 10, 'Massachusetts': 11, 'Michigan': 15, 'Minnesota': 10,
    'Mississippi': 6, 'Missouri': 10, 'Montana': 4, 'Nebraska': 5, 'Nevada': 6, 'New Hampshire': 4,
    'New Jersey': 14, 'New Mexico': 5, 'New York': 28, 'North Carolina': 16, 'North Dakota': 3,
    'Ohio': 17, 'Oklahoma': 7, 'Oregon': 8, 'Pennsylvania': 19, 'Rhode Island': 4,
    'South Carolina': 9, 'South Dakota': 3, 'Tennessee': 11, 'Texas': 40, 'Utah': 6,
    'Vermont': 3, 'Virginia': 13, 'Washington': 12, 'West Virginia': 4, 'Wisconsin': 10,
    'Wyoming': 3, 'District of Columbia': 3
}

# Initialize total votes for each party
democrat_total = 0
republican_total = 0
state_results = {}

# Loop through each state and ask for the winner
for state, votes in electoral_votes.items():
    winner = input(f"Who won {state} (Democrat/Republican)? ").strip().lower()

    # Check who won and add electoral votes accordingly
    if winner == "democrat":
        democrat_total += votes
        state_results[state] = "Democrat"
    elif winner == "republican":
        republican_total += votes
        state_results[state] = "Republican"
    else:
        print("Invalid input. Please enter either 'Democrat' or 'Republican'.")
        continue

# Determine and display the winner based on the electoral vote count
print("\nElection Results:")
print(f"Democratic Party: {democrat_total} electoral votes")
print(f"Republican Party: {republican_total} electoral votes")

if democrat_total > republican_total:
    print("The Democratic Party wins the election!")
elif republican_total > democrat_total:
    print("The Republican Party wins the election!")
else:
    print("It's a tie!")

# Load U.S. states shapefile
# unzip map in WD
shapefile_path = 'map/ne_110m_admin_1_states_provinces.shp'
usa = gpd.read_file(shapefile_path)

# Filter for the United States only
states = usa[usa['iso_a2'] == 'US']

# Assign colours to states based on election results
colours = {'Democrat': 'blue', 'Republican': 'red'}
states['color'] = states['name'].map(lambda x: colours.get(state_results.get(x, ''), 'grey'))

# Plot the U.S. map with state colours
fig, ax = plt.subplots(figsize=(15, 10))
states.boundary.plot(ax=ax, linewidth=1)
states.plot(ax=ax, color=states['color'])

# Create legend
blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Democrat')
red_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Republican')
ax.legend(handles=[blue_patch, red_patch], loc='upper left')

# Customize plot
ax.set_title("2024 U.S. Electoral College Map", fontsize=16)
ax.axis('off')

# Show plot
plt.show()
