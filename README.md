# Udacity-Professional-Data-AnalysisTrack
## Project Overview:
This project is the first project in egfwd Professional Data Analysis track. It aims to get some practice with python libraries that help in analysis as Numpy and Pandas.
The project aims to explore bike share systems data in 3 differents states in USA: Chicago, New York City, and washington. 

## Dataset Details:

Given 3 .csv files for each state that contain 6 core columns shown below:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following extra two columns:
- Gender
- Birth Year

## Code flow:

1. It starts by getting input from user to filter the data, these inputs are:
   - State name
   - Month
   - Day of the week
 
2. Read Data from corresponding city .csv file and then put it in a DataFrame (data structure type in Pandas library) and then filter the DataFrame considering the *month* and *day of the week*


3. Get some Statistical Data like:
   - **Statistical output related to time of travel:**
     - most common month
     - most common day of week
     - most common hour of day
   - **Statistical output related to traveling stations:**
     - most common start station
     - most common end station
     - most frequent combination of start station and end station
   - **Statistical output related to Trip duration:**
     - total travel time
     - average travel time
   - **Statistical output related to User info:**
     - counts of each user type
     - counts of each gender (only available for NYC and Chicago)
     - earliest, most recent, most common year of birth (only available for NYC and Chicago)
