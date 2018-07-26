#import dependencies
import csv
import os

# Files to load in and output
Load_File = os.path.join("Resources", "election_data.csv")
Output_File = os.path.join("election_analysis.txt")

#define variables
total_votes = 0
candidates_list = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#Read the csv
with open(Load_File) as election_data:
    reader = csv.reader(election_data)
    #skip header
    header = next(reader)

    #loop
    for row in reader:
        
        #add up total votes
        total_votes = total_votes + 1

        #get candidate_name
        candidate_name = row [2]
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
        
        #track their votes
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        #add the candidate votes

#open text file as writeable
with open(Output_File, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #write the total vote count to txt file
    txt_file.write(election_results)
    
    #determine winner
    for candidate in candidate_votes:

        #get vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        #write to text file
        txt_file.write(voter_output)

    #winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #write to text file
    txt_file.write(winning_candidate_summary)

