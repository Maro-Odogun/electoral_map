from dash import Dash, dcc, Input, Output, callback, html

# External font for customisation
external_stylesheets = ["https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap"]
external_link = 'https://veza.news/article/2025/03/31/broken-promises-of-transparency-a-deep-dive-into-nigerias-2023-election-data/'

# Paragraphs and external links explaining data
presidential_election_p1 = """The 2023 presidential elections was the first of its kind. 
Nigeria finally saw the emergence of a third-force candidate in the person of Peter Obi, 
who unlike his predecessors, was able to garner more than six million votes from the electorate.
It was also the first presidential election to utilise the INEC Results Viewing Portal (iRev). 
However, the platform failed to function as advertised. 
The Centre for Collaborative Investigative Journalism found that 14,252 results were blurred, 
with 7,493 not uploaded, 3,093 uploaded with the wrong election, and 2,679 were cancelled."""

presidential_election_p2 = """Out of Nigeria’s 176,846 polling units, this means over 15% of results remain unverifiable. 
The blurred documents alone account for about 7.7 million votes – judging by the number of registered voters in the units affected. 
 As a result of these discrepancies, the map only shows the ‘announced’ results. A comprehensive report from the CCIJ can be found """

legislature_p = """In the 2007 and 2011 general elections, The All Nigeria Peoples Party and Action Congress had sizable representation in the legislature, 
but neither were able to gain an upper hand on the Peoples’ Democratic Party. 
Coming together with the Centre for Progressive Change in February 2013, the three parties formed a united front called the All Progressives Congress. 
The rest, as they say, is history."""

voter_reg_p = """
Voter participation has consistently been taking hits over the years. A sense of possibility drove citizens to the polls in 2011 to elect Goodluck Ebele Jonathan, 
then widespread frustration led to his removal in 2015. Voter interest kept voter registration high for 2023, 
but the results showed the lowest number of votes cast in a presidential election since the nation's return to democracy in 1999. 
This could be attributed to widespread voter disenfranchisement, the introduction of the Biometric Voter Accreditation System(BVAS) to reduce unaccredited voting which has allegedly inflated numbers in past elections, 
and the number of missing results which leaves millions of votes unaccounted for.
"""



# Helper function for insering breaklines
def make_break(num_breaks):
    br_list = [html.Br()] * num_breaks
    return br_list

