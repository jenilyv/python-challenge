# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "C:\\9_23_24HW\\PyPoll\\Resources\\election_data.csv"  # Input file path
file_to_output =  "C:\\9_23_24HW\\PyPoll\\analysis"

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
dict = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        if dict.get(row[2]) == None:
            dict[row[2]] = 1
        else:
            dict[row[2]] += 1

        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


    output = "Election Results \n ------------------------- \nTotal Votes: " + str(total_votes) + "\n-------------------------\n"

    winValue = 0
    for candidate in dict:
        votes = dict[candidate]
        if winValue < votes:
            winValue = votes
            winner = candidate
        output += str(candidate) + ": " + "{:.3%}".format(votes / total_votes) + "(" + str(votes) + ")" + "\n"

    output += "-------------------------\n" + winner + "\n-------------------------"

election_data.close()

    # Write the total vote count to the text file
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

txt_file.close()
    # Print the total vote count (to terminal)


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
