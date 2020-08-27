# Real-time Election Results: Portugal 2019 Data Set

## Data Set Information

A data set describing the evolution of results in the Portuguese Parliamentary Elections of October 6th 2019.
The data spans a time interval of 4 hours and 25 minutes, in intervals of 5 minutes, concerning the results of the 27 parties involved in the electoral event.

## Attribute Information

TimeElapsed (Numeric): Time (minutes) passed since the first data acquisition
time (timestamp): Date and time of the data acquisition
territoryName (string): Short name of the location (district or nation-wide)
totalMandates (numeric): MP's elected at the moment
availableMandates (numeric): MP's left to elect at the moment
numParishes (numeric): Total number of parishes in this location
numParishesApproved (numeric): Number of parishes approved in this location
blankVotes (numeric): Number of blank votes
blankVotesPercentage (numeric): Percentage of blank votes
nullVotes (numeric): Number of null votes
nullVotesPercentage (numeric): Percentage of null votes
votersPercentage (numeric): Percentage of voters
subscribedVoters (numeric): Number of subscribed voters in the location
totalVoters (numeric): Percentage of blank votes
pre.blankVotes (numeric): Number of blank votes (previous election)
pre.blankVotesPercentage (numeric): Percentage of blank votes (previous election)
pre.nullVotes (numeric): Number of null votes (previous election)
pre.nullVotesPercentage (numeric): Percentage of null votes (previous election)
pre.votersPercentage (numeric): Percentage of voters (previous election)
pre.subscribedVoters (numeric): Number of subscribed voters in the location (previous election)
pre.totalVoters (numeric): Percentage of blank votes (previous election)
Party (string): Political Party
Mandates (numeric): MP's elected at the moment for the party in a given district
Percentage (numeric): Percentage of votes in a party
validVotesPercentage (numeric): Percentage of valid votes in a party
Votes (numeric): Percentage of party votes
Hondt (numeric): Number of MP's according to the distribution of votes now
FinalMandates (numeric): Target: final number of elected MP's in a district/national-level

