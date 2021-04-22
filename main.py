#imports
import streamlit as st
import pandas    as pd
import plotly.express as px

# setting the page layout design
st.set_page_config(layout= "wide")

# setting the title font size
st.markdown("""
<style>
.title {font-size:45px !important;}
</style>
""", unsafe_allow_html= True)

# setting the big font size
st.markdown("""
<style>
.big-font {font-size:26px !important;}
</style>
""", unsafe_allow_html= True)

# setting the small font size
st.markdown("""
<style>
.small-font {font-size:22px !important;}
</style>
""", unsafe_allow_html= True)

# setting the side bar personal informations
st.sidebar.markdown('# About Me:')
st.sidebar.markdown('## Name: Pedro Henrique Fratucci')
st.sidebar.markdown("I'm a mechanical engineer graduated from UFRGS in 2020. I've been programming since 2017. \
I started studying data analysis in December 2020. Since then, I've been studying all stages of developing business solution models. \
Staring by understanding the business problem until creating models solutions, interfaces and deploying it through Clouds plataforms.")

# setting side bar contact informations
st.sidebar.markdown("# Contact:")
st.sidebar.markdown('[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/pedro-henrique-fratucci-906a94172/)](https://www.linkedin.com/in/pedro-henrique-fratucci-906a94172/) \
[![GitHub Badge](https://img.shields.io/badge/Git-Hub-brightgreen)](https://github.com/pedrofratucci)')
st.sidebar.markdown('[![Hotmail Badge](https://img.shields.io/badge/-pedrofratucci8@hotmail.com-0078D4?style=flat-square&logo=microsoft-outlook&logoColor=white&link=mailto:pedrofratucci8@hotmail.com)](mailto:pedrofratucci8@hotmail.com)')

# setting side bar project informations
st.sidebar.markdown("# About The Project:")
st.sidebar.markdown("This project is about a business problem solution through insights, for a company called House Rocket. \
Which is a digital platform whose business model is the purchase and sale of properties using technology. \
Its main strategy is to buy good houses in great locations with low prices and then resell them later at higher prices. \
The greater the difference between buying and selling, the greater the company's profit and therefore the greater its revenue.")

# setting the main title and select box
st.title("WELCOME")
st.markdown("## SELECT A SUBJECT:")
selected_box = st.selectbox('' ,("", 'Insights', "CEO's questions and answers", 'Business scenarios simulation results', 'Houses to buy'))

# creating the main function, that commands the others
def main():
    if selected_box == 'Insights':
        insights_selector()
    if selected_box == "CEO's questions and answers":
        load_CEO_questions()
    if selected_box == 'Business scenarios simulation results':
        load_business_scenarios()
    if selected_box == 'Houses to buy':
        houses_selector()

# creating a function that returns other function, related to the insight selected in its selectbox
def insights_selector():

    st.markdown("### SELECT A INSIGHT:")
    insight_box = st.selectbox('',(" ", 'Insight 1', 'Insight 2', 'Insight 3', 'Insight 4', 'Insight 5', 'Insight 6',
                                   'Insight 7', 'Insight 8', 'Insight 9', 'Insight 10', 'Insight 11', 'Insight 12'))

    if insight_box == 'Insight 1':
        load_hypothesis_1()
    if insight_box == 'Insight 2':
        load_hypothesis_2()
    if insight_box == 'Insight 3':
        load_hypothesis_3()
    if insight_box == 'Insight 4':
        load_hypothesis_4()
    if insight_box == 'Insight 5':
        load_hypothesis_5()
    if insight_box == 'Insight 6':
        load_hypothesis_6()
    if insight_box == 'Insight 7':
        load_hypothesis_7()
    if insight_box == 'Insight 8':
        load_hypothesis_8()
    if insight_box == 'Insight 9':
        load_hypothesis_9()
    if insight_box == 'Insight 10':
        load_hypothesis_10()
    if insight_box == 'Insight 11':
        load_hypothesis_11()
    if insight_box == 'Insight 12':
        load_hypothesis_12()

def load_hypothesis_1():
    st.title('Insight 1')
    st.subheader("For all city regions, their house's average price has a minimum increase of 10% by increasing the \
    house's Living Condition.")
    st.subheader("FALSE")
    st.image('storytelling/H1.png')
    st.write("- Southeast region don't have the average house's price minimum increase of 10% for each living condition levels upgrade. It can be seen when upgrading the living condition from level 3 to level 4, the house prices decreases. But, it has a significant 55,80% average houses price increase by upgrade the living condition level 2 to level 3.")
    st.write("- North region don't have the average house's price minimum increase of 10% for each living condition levels upgrade. Neither a significant average houses price increase when upgrading the living condition level.")
    st.write("- Even though west region has the average average house prices increase by upgrading the levels condition, when upgrading the living condition level 1 to level 2, its increases is only 1,95%. But, it has a significant 58,83%  average houses price increase by upgrade the living condition level 2 to level 3.")
    st.write("- Central region don't have the average house's price minimum increase of 10% for each living condition levels upgrade. It can be seen when upgrading the living condition from level 1 to level 2, the house prices decreases. But, it has a significant 75,53% average houses price increase by upgrade the living condition level 2 to level 3.")
    st.write("- Downtown region have the average house's price minimum increase of 10% for each living condition levels upgrade. But, the houses prices increases when upgrading the living condition level are not significant, something like 11% for both levels. Also, it can be seen that the downtown region doesn't have living condition levels 1 and 2.")

def load_hypothesis_2():
    st.title('Insight 2')
    st.subheader("For all city regions, their house's average price has a minimum increase of 10% by increasing the \
    house's Construction Design level.")
    st.subheader("TRUE")
    st.image('storytelling/H2.png')
    st.write("- Southeast region do have the average house's price minimum increase of 10% for each construction design level upgrade. Also, it is the only region with low quality, when it comes about houses construction design. This because, proprably, its the poorest city's region.")
    st.write("- North region do have the average house's price minimum increase of 10% for each construction design level upgrade. It only has average and high quality levels. The average house's price difference when upgrading from level 2 to 3 is 115,92% raise.")
    st.write("- West region do have the average house's price minimum increase of 10% for each construction design level upgrade. It only has average and high quality levels. The average house's price difference when upgrading from level 2 to 3 is 201,46% raise.")
    st.write("- Central region do have average house's price the minimum increase of 10% for each construction design level upgrade. It only has average and high quality levels. The average house's price difference when upgrading from level 2 to 3 is 82,69% raise.")
    st.write("- Downtown region do have average house's price the minimum increase of 10% for each construction design level upgrade. It only has average and high quality levels. The average house's price difference when upgrading from level 2 to 3 is 73,52% raise.")

def load_hypothesis_3():
    st.title('Insight 3')
    st.subheader("For North, downtown and west regions, their houses are more likely to be sold during the spring than any other season.")
    st.subheader("TRUE")
    st.image('storytelling/H3.png')
    st.write("All 3 regions have the approximately the same pattern when we talk about houses sale. Selling more houses during the spring, followed by summer, fall and winter.")

def load_hypothesis_4():
    st.title('Insight 4')
    st.subheader("For Central and Southeast regions, their houses are more likely to be sold during the winter than any other season.")
    st.subheader("FALSE")
    st.image('storytelling/H4.png')
    st.write("Both regions have the approximately the same pattern when we talk about houses sale, which is almost the same of the other 3 regions. Selling more houses during the spring, followed by summer, fall and winter.")

def load_hypothesis_5():
    st.title('Insight 5')
    st.subheader("For all city regions, houses prices growth month over month is at a 3% minimum.")
    st.subheader("FALSE")
    st.image('storytelling/H5.png')
    st.write("- Southeast region don't have the average house's price minimum increase of 3% between each month. The house's price variates between the months, with ups and downs.")
    st.write("- North region don't have the average house's price minimum increase of 3% between each month. The house's price variates between the months, with ups and downs.")
    st.write("- West region don't have the average house's price minimum increase of 3% between each month. The house's price variates between the months, with ups and downs.")
    st.write("- Central region don't have the average house's price minimum increase of 3% between each month. The house's price variates between the months, with ups and downs.")
    st.write("- Downtown region don't have the average house's price minimum increase of 3% between each month. The house's price variates between the months, with ups and downs.")

    st.write("But, when analysing all city regions, its clearly visible that, when talking about average house's prices sold and not the amount of houses sold, April is the month that sells the expensive houses.")

def load_hypothesis_6():
    st.title('Insight 6')
    st.subheader("For all city regions, houses prices growth year over year is at a 10% minimum.")
    st.subheader("FALSE")
    st.image('storytelling/H6.png')
    st.write("- Southeast region don't have the average house's price minimium increase of 10% between the years. Also, the average houses price sold decreases between 2014 and 2015.")
    st.write("- North region do presents an average house's price minium increase between the years. The increase was 2,99%, nothing close to 10%.")
    st.write("- West region do presents an average house's price minium increase between the years. The increase was 4,24%, nothing close to 10%.")
    st.write("- Central region do presents an average house's price minium increase between the years. The increase was 2,77%, nothing close to 10%.")
    st.write("- Downtown region do presents an average house's price minium increase between the years. The increase was 2,00%, nothing close to 10%.")

def load_hypothesis_7():
    st.title('Insight 7')
    st.subheader("For all city regions, their houses floor's number growth increases the house's price at a 20% minimum.")
    st.subheader("FALSE")
    st.image('storytelling/H7.png')
    st.write("- Southeast region do have the average house's price minimum increase of 20% when renovating its amount of floors. With a significant average house's price increase of 44,34% when upgrading from 1 to 2 floors.")
    st.write("- North region don't have the average house's price minimum increase of 20% when renovating its amount of floors. Also, the average house's prices decreases when upgrading from 2 to 3 floors, probably because of other features influences.")
    st.write("- West region do have the average house's price minimum increase of 20% when renovating its amount of floors. With a significant average house's price increase of 24,65% when upgrading from 1 to 2 floors.")
    st.write("- Central region don't have the average house's price minimum increase of 20% when renovating its amount of floors. Also, the average house's prices decreases when upgrading from 2 to 3 floors, probably because of other features influences.")
    st.write("- Downtown region don't have the average house's price minimum increase of 20% when renovating its amount of floors. Also, the average house's prices decreases when upgrading from 2 to 3 floors, probably because of other features influences. But, it has a significant average house's price increase of 25,32% when upgrading from 1 to 2 floors.")

def load_hypothesis_8():
    st.title('Insight 8')
    st.subheader("For all city regions, the Living Area size growth is more likely to increase the house's prices.")
    st.subheader("TRUE")
    st.image('storytelling/H8.png')
    st.write("For all city's regions, its clearly that not always a living area size increase will increase the average house's prices, because of other variables influences. But, analyzing with a macro view, its visible that the living area size increase will likely increase the house's price.")

def load_hypothesis_9():
    st.title('Insight 9')
    st.subheader("For all city regions, the (Living Area / Land Space) proportion growth is more likely to increase the house's prices.")
    st.subheader("TRUE")
    st.image('storytelling/H9.png')
    st.write("For all city's regions, there is no visible pattern of house's prices increase or decrease when increasing the living area / land area proportion.")

def load_hypothesis_10():
    st.title('Insight 10')
    st.subheader("Houses with water view has a average price growth of 10% by increasing the house's Living Condition.")
    st.subheader("FALSE")
    st.image('storytelling/H10.png')
    st.write("- There is no houses with water view in Downtown region.")
    st.write("- Southeast region don't have the average water view house's price minimum increase of 10% when upgrading the living condition levels. Also, there is no houses with living condition level less than 3 in Southeast region.")
    st.write("- North region don't have the average water view house's price minimum increase of 10% when upgrading the living condition levels. The house's price tends to remain the same. Also, there is no houses with living condition level less than 3 in Southeast region.")
    st.write("- West region don't have the average water view house's price minimum increase of 10% when upgrading the living condition levels. Also, there is a house's price decrease pattern after a living condition level 3.")
    st.write("- Central region don't have the average water view house's price minimum increase of 10% when upgrading the living condition levels. But its important to notice that there is a significant average house's price increase of 47,82% when upgrading it from living condition level 3 to 4.")

def load_hypothesis_11():
    st.title('Insight 11')
    st.subheader("For all city regions, by increasing the bedrooms quantity its most likely to increases the house prices.")
    st.subheader("TRUE")
    st.image('storytelling/H11.png')
    st.write("For all city's regions, there is a pattern that by increasing the bedrooms quantity its most likely that the house's price will increase too.")
    st.write("- Southeast region respects this pattern in a range between 1 and 5 bedrooms.")
    st.write("- North region respects this pattern in a range between 1 and 5 bedrooms.")
    st.write("- West region respects this pattern in a range between 1 and 7 bedrooms.")
    st.write("- Central region respects this pattern in a range between 1 and 5 bedrooms.")
    st.write("- Downtown region respects this pattern in a range between 1 and 5 bedrooms.")

def load_hypothesis_12():
    st.title('Insight 12')
    st.subheader("For all city regions, by increasing the bathrooms quantity its most likely to increases the house prices.")
    st.subheader("TRUE")
    st.image('storytelling/H12.png')
    st.write("For all city's regions, there is a pattern that by increasing the bathrooms quantity its most likely that the house's price will increase too.")

# creating a fuction that returns all CEO's questions and their answers
def load_CEO_questions():

    st.title('Which houses should the company buy and at what price?')

    st.subheader("Houses that the company should buy:")
    st.write("1 - Our priority should be buying houses in Central region with a living condition level 2 and do a renovation so its living condition upgrades to level 3. This renovation will probably increase 75,53% the house's prices, as shown in H1. ")
    st.write("2 - As our second option would be buy houses in West region with a living condition level 2 and do a renovation so its living condition upgrades to level 3. This renovation will probably increase 58,83% the house's prices, as shown in H1. ")
    st.write("3 - As our third option would be buy houses in Southeast region with a living condition level 2 and do a renovation so its living condition upgrades to level 3. This renovation will probably increase 55,80% the house's prices, as shown in H1. ")
    st.write("- These renovations were considered having the same cost, i.e, it don't depends on the city's region")

    st.subheader("Prices that the company should pay:")
    st.write("If the company could calculate the renovations cost, and assuming that these renovations will cost less than the difference between the before and after renovation scenarios, the company should buy all houses mentioned previously, with prices on averange or lower.")
    st.write("If the company could not calculate the renovations cost, the company should buy all houses mentioned previously, but only with prices below averange. I suggest buy houses in those living conditions with prices 20% below average, so we secure our chances of profit.")
    st.write("- These renovations should have a cost lower than the difference between before and after living condition scenarios, so the company profit with it")
    st.write("")

    st.title("Once the house is in the company's possession, what is the best time to sell it and what would be the sale price?")
    st.write("")
    st.write("")

    st.subheader("Best time to sell the bought houses:")
    st.write("As seen in H3 and H4, all city's regions has its sales peak during the spring, followed by summer. So these are the periods that I suggest to sell the houses.")

    st.subheader("Suggested prices for houses sale:")
    st.write("After do a renovation on the bought houses, I suggest simply sell them on their new living condition's averange price, for each  region. Because our profit will be originated by the upgrading the living condition, not from trying to sell over their supposed average prices.")
    st.write("")

    st.title("Should the company make a renovation to increase the price of the sale? What would be the suggestions for changes?")
    st.write("")
    st.write("")

    st.subheader("About if the company should make a renovation:")
    st.write("Yes, it should. All suggestions are based on renovations, as previously mentioned.")

    st.subheader("Changing suggestions:")
    st.write("- Even though the **`living_condition`** feature has sometimes a negative and sometimes a weak correlation with the features that it supposed to have a strong correlation, such as **`bedrooms`**, **`bathrooms`**, **`floors`** and **`living_area`**, as shown in section 4.3, I will assume that these features have strong correlation.")
    st.write("- As shown in H8, by increasing the **`living_area`** the house's price will probably increases too.")
    st.write("- As shown in H7, by increasing the **`floors`** quantity the house's price will increases too. ")
    st.write("")
    st.write("So, I suggest that for houses with a small **`living_area`** / **`land_area`** proportion (lower than 1), the renovation focus should be into build more **`bedrooms`** and **`bathrooms`**, respecting the range accepted of **`bedrooms`** and **`bathrooms`** that increases the house's price, as shown in H11 and H12, respectively.")
    st.write("And for houses with a significant **`living_area`** / **`land_area`** proportion (higher than 1), the renovation focus should be into build a new floor, then build more **`bedrooms`** and **`bathrooms`**, respecting the range accepted of **`bedrooms`** and **`bathrooms`** that increases the house's price, as shown in H11 and H12, respectively.")

# creating a fuction that returns all business scenarios simulated
def load_business_scenarios():

    st.write("")
    st.write("")
    st.write("")
    st.write("Because of the lack of information, I will assume some premisses for each scenario simulation.")

    st.subheader("Expected Scenario:")
    st.write("- For this scenario, I will assume that the renovation costs will be 30% of the bought house's price.")
    st.write("- For this scenario, I will assume that we are going to buy the houses at their average price or lower, then sell them at their average prices, accordingly to their living condition level.")
    st.write("**Expected profit: $ 16,831,921.21**")
    st.write("**Expected ROI: 0.60%**")

    st.subheader("Worst Scenario:")
    st.write("- For this scenario, I will assume that the renovation costs will be 30% of the bought house's price.")
    st.write("- For this scenario, I will assume that we are going to buy the houses at their average price or lower, then sell them at 20% below their average prices, accordingly to their living condition level.")
    st.write("**Expected profit: $ 7,846,357.17**")
    st.write("**Expected ROI: 0.28%**")

    st.subheader("Best Scenario:")
    st.write("- For this scenario, I will assume that the renovation costs will be 30% of the bought house's price.")
    st.write("- For this scenario, I will assume that we are going to buy the houses at their average price  or lower, then sell them at 20% above their average prices, accordingly to their living condition level.")
    st.write("**Expected profit: $ 25,817,485.25**")
    st.write("**Expected ROI: 0.92%**")


def houses_selector():

    st.write("")
    st.write("")
    st.subheader("These are all houses that I suggest to buy. Feel free to filter them as it fits you")


    # read the final dataset, with the houses that we should buy. Saved as a pickle file
    df = pd.read_csv("data/df_houses_to_buy.csv")


    # creating a select box to select the city's region
    st.write("")
    st.write("")
    region_box = st.selectbox("Select which city's region you're interesed", (
    'All regions', 'Central', 'Downtown', 'North', 'Southeast', 'West'))


    # creating a slider to filter the houses prices range
    st.write("")
    st.write("")
    price_limit = st.slider(label= 'Select the maximum price Limit',
        value= 429000,
        min_value= 115000,
        max_value= 429000,
        step= 1000)


    # creating a slider to filter the bedrooms range
    st.write("")
    st.write("")
    min_bedrooms = st.slider(label= 'Select the minimum Bedrooms accepted',
        value= 1,
        min_value= 1,
        max_value= 6,
        step= 1)


    # creating a slider to filter the bathrooms range
    st.write("")
    st.write("")
    min_bathrooms = st.slider(label= 'Select the minimum Bathrooms accepted',
        value= 0.25,
        min_value= 0.75,
        max_value= 2.75,
        step= 0.25)

    if region_box == 'All regions':
        # filtering the dataset with the inputed filters by the user
        df_filtered = df[(df['price'] <= price_limit) &
                       (df['region'] != region_box) &
                       (df['bedrooms'] >= min_bedrooms) &
                       (df['bathrooms'] >= min_bathrooms)]
    else:
        # filtering the dataset with the inputed filters by the user
        df_filtered = df[(df['price'] <= price_limit) &
                       (df['region'] == region_box) &
                       (df['bedrooms'] >= min_bedrooms) &
                       (df['bathrooms'] >= min_bathrooms)]


    # filtering the features that we want to show in the graph
    df_filtered = df_filtered[['id', 'latitude', 'longitude', 'price', 'living_condition']]



    # creating a scatter mapbox graph with plotly
    fig = px.scatter_mapbox(df_filtered, lat='latitude', lon='longitude', hover_name='id',
                            hover_data=['price'],
                            color_discrete_sequence=['blue'],
                            zoom=10,
                            color='price',
                            height=700, width=1200, size='price', size_max=10)

    # adjusting the graph layout
    fig.update_layout(mapbox_style = 'open-street-map')

    # adjusting the graph margins
    fig.update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})

    st.plotly_chart(fig, use_container_width= True)


if __name__ == "__main__":
    main()






