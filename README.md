# Housing market speculation
![Main figure](https://image.flaticon.com/icons/png/512/2400/2400362.png)


# Business Problem

In process...

# Objective and Solution Proposal

### Objective

Answer the House Rocket's CEO questions and create insights to discuss with the company business team and simulate business scenarios.

### Solution Proposal

Create a exploratory data analysis through all the dataset available and manipulate the data to answer the CEO questions and simulation business scenarios.


# Dataset Summary

- **`id`** [int]: Unique ID for each home sold
- **`date`** [date]: Date of the home sale
- **`price`** [float]: Price of each home sold
- **`bedrooms`** [categorical]: Number of bedrooms
- **`bathrooms`** [categorical]: Number of bathrooms. Where 1 accounts for a complete bathroom, 0.75 accounts a complete bathroom, but no bathtub and 0.5 accounts for a bathroom with a sink and toilet only
- **`sqft_living`** [float]: Square footage of the apartments interior living space
- **`sqft_lot`** [float]: Square footage of the land space
- **`floors`** [categorical]: Number of floors
- **`waterfront`** [binary]: A dummy variable for whether the apartment was overlooking the waterfront or not
- **`view`** [categorical]: An index from 0 to 4 of how good the view of the property was
- **`condition`** [categorical]: An index from 1 to 5 on the condition of the apartment
- **`grade`** [categorical]: An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design
- **`sqft_above`** [float]: The square footage of the interior housing space that is above ground level
- **`sqft_basement`** [float]: The square footage of the interior housing space that is below ground level
- **`yr_built`** [int]: The year the house was initially built
- **`yr_renovated`** [int]: The year of the house’s last renovation
- **`zipcode`** [int]: What zipcode area the house is in
- **`lat`** [float]: Latitude
- **`long`** [float]: Longitude
- **`sqft_living15`** [float]: The square footage of interior housing living space for the nearest 15 neighbors
- **`sqft_lot15`** [float]: The square footage of the land lots of the nearest 15 neighbors 


#  Mind Map Hypoteses

<img src= "images/mind_map.png"> 

## City's region split

By using the latitude and longitudes available in the dataset we could split the regions like this:

<img src= "images/region_split.png" width= "500" height= "600"> 


# Exploratory Data Analysis

## Univariate Analysis

### Categorical Features Distribution Analysis

<img src= "storytelling/cat_features_distribution.png"> 

- The bedrooms quantity is concentrated between 1 and 6. Which the most common is houses with 3 bedrooms, followed by 4 and 2 
- Talking about bathrooms, the most common is houses with 2.5 bathrooms, probably 2 bathrooms and a toilet (0.5)
- Talking about floors, the most common is houses with only 1 floor, followed by 2 and 3
- When it comes about water view, only a few percent of the houses have it
- When it comes about view level, almost all houses have a poor (0) view level
- When it comes about living condition, we can say that people in Seattle live quite good. With almost all houses having a level 3 or more living condition and only a few percent of the houses being a bad place to live in
- Talking about the construction design, almost all houses are labeled as having a average quality
- Talking about having a basement or not, its impressive that almost 40% of the houses have it
- When it comes about the house's year built, there is not a perceptive pattern, with some ups and downs between this period
- When it comes about if the house had a renovation, only a few did it
- Talking about the house's sales distribution between months, is clearly visible that between April and July is the period that sells more houses during the year
- When it comes about the house's sales distribution between years, even with only 2 years and a 12 months range, its impressive that from January-2015 until April-2015 there is almost the half of the houses sold compared to the hole 2014 year
- Talking about the house's sales distribution between the weather seasons, is clearly visible that the season that sells more houses is Spring, followed by summer
- When it comes about the house distribution between the city's region, more than a half of the houses as located in Southeast and North regions

### Numerical Features Distribution Analysis

<img src= "storytelling/num_features_distribution.png"> 

- All numerical variables have significant high outliers
- **`land_area`** and **`neighbors_land_area`** have the most significant outliers amount

But, we won't go back to check these features outliers, because they won't affect our hypotheses analysis.

## Bivariate Analysis

### Hypothesis 1: For all city regions, their house's average price has a minimum increase of 10% by increasing the house's Living Condition

In process...

### Hypothesis 2: There are more fraudulent transactions in total values through Transfer type

In process...

### Hypothesis 3: All transactions over $ 200,000.00 are fraudulents

In process...

### Hypothesis 4: Transactions with amount values level between $ 50,000.00 and 200,000.00 are more likely to be fraudulent than the others amount levels

In process...

### Hypothesis 5: Fraudulent transations happens more to Customer-Customer than Customer-Merchant relation

In process...

### Hypothesis 6: There is more chance of having a fraudulent transaction when the final origin's balance is zero

In process...

### Hypothesis 7: Fraudulent transactions tends to happen more on the weekends than workweek

In process...

### Hypothesis 8: Fraudulent transactions tends to happen more on the First month's Fortnight than the Second month's Fortnight

In process...

## Multivariate Analysis

<img src= "storytelling/features_relations.png"> 

**For Southeast region:**
- **`price`** feature has a strong positive correlation with the **`living_area`** feature
- **`price`** feature has a moderate positive correlation with the **`bedrooms`**, **`bathrooms`**, **`floors`** and **`construction_design_num`** features
- **`living_condition`** feature has a **weird** negative correlation with all others features
<br>

**For North region:**
- **`price`** feature has a strong positive correlation with the **`living_area`** feature
- **`price`** feature has a moderate positive correlation with the **`bedrooms`**, **`bathrooms`**, **`floors`** and **`construction_design_num`** features
- **`living_condition`** feature has a **weird** negative correlation with the **`bathrooms`**, **`living_area`** and **`floors`** features
- **`living_condition`** feature has a **weird** weak positive correlation with the **`bedrooms`** and **`price`** features
<br>

**For West region:**
- **`price`** feature has a strong positive correlation with the **`living_area`** feature
- **`price`** feature has a moderate positive correlation with the **`bedrooms`**, **`bathrooms`**, **`floors`**, **`living_condition`** and **`construction_design_num`** features
- **`living_condition`** feature has a **weird** negative correlation with the **`bathrooms`** and **`floors`** features
- **`living_condition`** feature has a **weird** weak positive correlation with the **`bedrooms`**, **`living_area`** and **`price`** features
<br>

**For Central region:**
- **`price`** feature has a strong positive correlation with the **`living_area`** feature
- **`price`** feature has a moderate positive correlation with the **`bedrooms`**, **`bathrooms`**, **`floors`**, **`living_condition`** and **`construction_design_num`** features
- **`living_condition`** feature has a **weird** negative correlation with the **`bathrooms`**, **`living_area`** and **`floors`** features
- **`living_condition`** feature has a **weird** weak positive correlation with the **`bedrooms`** and **`price`** features
<br>

**For Downtown region:**
- **`price`** feature has a strong positive correlation with the **`living_area`** feature
- **`price`** feature has a moderate positive correlation with the **`bedrooms`**, **`bathrooms`**, **`floors`**, **`living_condition`** and **`construction_design_num`** features
- **`living_condition`** feature has a **weird** negative correlation with the **`floors`** feature
- **`living_condition`** feature has a **weird** weak positive correlation with the **`bedrooms`** and **`floors`** features


# Answering the CEO's Questions

## Which houses should the company buy and at what price?

**Houses that the company should buy:**

1 - Our priority should be buying houses in Central region with a living condition level 2 and do a renovation so its living condition upgrades to level 3. This renovation will probably increase 75,53% the house's prices, as shown in H1. 

2 - As our second option would be buy houses in West region with a living condition level 2 and do a renovation so its living condition upgrades to level 3. This renovation will probably increase 58,83% the house's prices, as shown in H1. 

3 - As our third option would be buy houses in Southeast region with a living condition level 2 and do a renovation so its living condition upgrades to level 3. This renovation will probably increase 55,80% the house's prices, as shown in H1. 

- These renovations were considered having the same cost, i.e, it don't depends on the city's region
<br>

**Prices that the company should pay:**

If the company could calculate the renovations cost, and assuming that these renovations will cost less than the difference between the before and after renovation scenarios, the company should buy all houses mentioned previously, with prices on averange or lower.

If the company could not calculate the renovations cost, the company should buy all houses mentioned previously, but only with prices below averange. I suggest buy houses in those living conditions with prices 20% below average, so we secure our chances of profit

- These renovations should have a cost lower than the difference between before and after living condition scenarios, so the company profit with it

## Once the house is in the company's possession, what is the best time to sell it and what would be the sale price?

**Best time to sell the bought houses:**

As seen in H3 and H4, all city's regions has its sales peak during the spring, followed by summer. So these are the periods that I suggest to sell the houses.
<br>

**Suggested prices for houses sale:**

After do a renovation on the bought houses, I suggest simply sell them on their new living condition's averange price, for each  region. Because our profit will be originated by the upgrading the living condition, not from trying to sell over their supposed average prices.

## Should the company make a renovation to increase the price of the sale? What would be the suggestions for changes?

**About if the company should make a renovation:**

Yes, it should. All suggestions are based on renovations, as previously mentioned.
<br>

**Changing suggestions:**

- Even though the **`living_condition`** feature has sometimes a negative and sometimes a weak correlation with the features that it supposed to have a strong correlation, such as **`bedrooms`**, **`bathrooms`**, **`floors`** and **`living_area`**, as shown in section 4.3, I will assume that these features have strong correlation

- As shown in H8, by increasing the **`living_area`** the house's price will probably increases too. 
- As shown in H7, by increasing the **`floors`** quantity the house's price will increases too. 
<br>

So, I suggest that for houses with a small **`living_area`** / **`land_area`** proportion (lower than 1), the renovation focus should be into build more **`bedrooms`** and **`bathrooms`**, respecting the range accepted of **`bedrooms`** and **`bathrooms`** that increases the house's price, as shown in H11 and H12, respectively.

And for houses with a significant **`living_area`** / **`land_area`** proportion (higher than 1), the renovation focus should be into build a new floor, then build more **`bedrooms`** and **`bathrooms`**, respecting the range accepted of **`bedrooms`** and **`bathrooms`** that increases the house's price, as shown in H11 and H12, respectively.


# Business Simulation

In process...
    
## Expected Scenario

In process...

## Worst Scenario

In process...

## Best Scenario

In process...

# Further Improvements

In proces...

# References

## Business Problem Source
- https://youtu.be/DSVQ3HcxEPw?t=871

## Data Source
- https://www.kaggle.com/harlfoxem/housesalesprediction

## Supplementary Materials

- https://homes.cs.washington.edu/~domta/seattle-inequity.html
