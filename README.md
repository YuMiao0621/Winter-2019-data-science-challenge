# Winter-2019-data-science-challenge
Question #1

#Problem Statement:

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis.

a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

b. What metric would you report for this dataset?

c. What is its value?

#Solutions:

From the dataset, I noticed that there are two kinds of outliers. The first type is the number of total items to be thousands (i.e., the user (user_id 607) always made an order of $704000 with 2000 items each time at the same store (store_id 42) and also the same time of the day (4am)). This could be something wrong with the data collection (may be this is a businesses customer that should not appear in this data collection) OR there are some problems with the user itself (e.g., the credit card has been cloned). Another type of outliers in this data is the unit price to be more than 20k (i.e., the price of one item in the same store (store_id 78) is $25725). We can tell that the sneaker in this store costs $25725 OR again there is something suspicious with the data. 

   Solution A: Use median other than AOV

The problem with the AOV of $3145.13 is that it is just the mean value which is sensitive to the outliers over all the order amounts. However, removing the outliers is not a perfect way since some of the outliers are rational values or even important to the entire data. Median is one of the robust statistics (https://en.wikipedia.org/wiki/Robust_statistics) which is not affected by outliers, especially when the distribution is not normal. In this way, we can get an AOV of $284 (See 'median.py').

   Solution B: Using a better metric describing this data

The AOV can only give a limited sight into this data. Maybe we can search for a better metric, for example, the repeat purchase rate and the customer purchase latency. The repeat purchase rate shows how loyal your customer base is (https://www.littlestreamsoftware.com/articles/repeat-purchase-rate-calculate/) and is calculated in the equation below. To improve this value can definitely help with improving the sales volume.  

    Repeat Purchase Rate = # of Repeat Customers / # of Total Customers
    
 And the customer purchase latency shows the average amount of time between purchases (https://www.littlestreamsoftware.com/articles/repeat-customers-using-purchase-latency/). Knowing this value can help us make decisions to nudge customers to reorder (e.g., sending out coupons or other strategies) before and after the calculated time window.

Thank you for your time.

