import streamlit as st
import pickle
import pandas as pd

st.title("IPL Win Predictor")

teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the Bowling Team', sorted(teams))

selected_city = st.selectbox('Select Host City', sorted(cities))
target = st.number_input('Target', min_value=1, step=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score', min_value=0, step=1)
with col4:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1)

if st.button('Predict Probability'):
    if batting_team == bowling_team:
        st.error("Batting and Bowling teams cannot be the same. Please select different teams.")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        if wickets == 10 or overs == 20:
            st.header(f"{batting_team} - 0%")
            st.header(f"{bowling_team} - 100%")
        else:
            input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                                     'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
                                     'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

            result = pipe.predict_proba(input_df)
            loss_prob = result[0][0]
            win_prob = result[0][1]

            st.header(f"{batting_team} - {round(win_prob * 100)}%")
            st.header(f"{bowling_team} - {round(loss_prob * 100)}%")
