
# Mobile-Phone-Sentiment-Analysis

![App Screenshot](https://miro.medium.com/max/535/1*Yzvu3Fgk-2eZDHmQ1tqgrA.png)


Purchasing a product is an interaction between two entities, consumers and business owners. Consumers often use reviews to make decisions about what products to buy, while businesses, on the other hand, not only want to sell their products but also want to receive feedback in terms of consumer reviews. Consumer reviews about purchased products shared on the internet have a great impact. Human nature is generally structured to make decisions based on analyzing and getting the benefit of other consumer experience and opinions because others often have a great influence on our beliefs, behaviors, perception of reality, and the choices we make. Hence, we ask others for their feedback whenever we are deciding on doing something. Additionally, this fact applies not only to consumers but also to organizations and institutions.
E-commerce websites have increased in popularity to the point where consumers rely on them for buying and selling. These websites give consumers the ability to write comments about different products and services, which has resulted in a huge amount of reviews becoming available. Consequently, the need to analyze these reviews to understand consumers’ feedback has increased for both vendors and consumers. However, it is difficult to read all the feedback for a particular item, especially for popular items with many comments.

In this research, a predictor for consumers’ satisfaction is built on mobile phone products based on the reviews with ratings as the constructed label. We will also attempt to understand the factors that contribute to classifying reviews as positive, negative or neutral (based on important or most frequent words). This is believed to help companies improve their products and also help potential buyers make better decisions when buying products.

## Authors

- [Vivian Kingasia](https://www.github.com/VivianKingasia)
- Elsie Juma
- Mercy Mukundi
- Mercy Ngila
- Roseline Maina
- Daniel Oselu


## Main Objective

To perform a sentiment analysis of mobile phone reviews from Amazon website to determine how these reviews can help buyers make informed purchasing decisions and sellers to make better choices in terms of phones to sell.

## Specific Objectives

1. To help companies understand their consumers’ feedback to maintain their products/services or enhance them.

2. To provide insights to companies in curating offers on speciﬁc products to increase their proﬁts and customer satisfaction.

3. To advise the advertisement department in companies on these key features to use as selling points and to specific customer segments in upcoming advertisements.

4. To understand the factors that contribute to classifying reviews as positive, negative or neutral (based on important or most frequent words).



## Data Understanding

The data used for this project was scraped from amazon.com, an ecommerce platform that sells different products. It contains more than 17 thousand reviews of unlocked mobile phones sold on between the period 2014 to August 2022. The data has 7 features:

- Rating - Contains the rating awarded to a product.

- Review Title - The title of review of a product.

- Review - Contains the review of a product.

- Location and Date of Review - The date and location from where a review was done.

- Affiliated Company - Company affiliated with the mobile phone.

- Brand and Features - The brand of the product and its relevant features.

- Price - The price of the product.

## Models Implemented

Modeling

FIve algorithms were used in this analysis; three unsupervised and one supervised model.

 - Multinomial Naive Bayes Model implemented produced an f1 score-0.74 and ROC score-0.88

- Support Vector Machine (SVM) implemented produced an f1 score -0.77 and ROC score-0.89. Even after tuning gridsearch, the SVM model did not produce better results.

- XGBoost implemented produced an f1 score-0.67 and ROC score-0.84

- Vader model was implemented to challenge solution. It produced an f1 score-0.63

- LTSM model was also implemented to challenge solution. It produced an f1 score-0.75

Evaluation 

Several metrics were used to meet the objectives.
The ROC score and f1 score were the main metrics used to evaluate final model which was the SVM model.

## Conclusion

- Sentiment analysis is necessary to understand consumer reviews.

- Consumers are more likely to leave a review when highly pleased or highly frustrated.

- Used products are more likely to get reviews as consumers hail or slam them.

- Online shopping is here to stay purchases increase each passing year.

## Recommendations

- Monitoring and improvement of the sentiment analysis model to improve its performance.

- Harnessing of more and more consumer reviews as they will provide great insights that will drive profits and help understand the consumer better.

- Follow up to find out if the increase in online purchases are due to new customers or repeat customers and if so, explore ways to onboard new customers possibly through convenience, efficiency and reviews to improve their trust.

- Improvement of factors that lead to positive reviews and correction of factors leading of negative reviews.

- Negative Reviews aren't always bad. They at times show a consumer the worst case scenario. Monitoring to confirm if some products still get high sales despite negative reviews.

- Follow up on third party resellers that have received scam claims and action taken if found guilty.
## Deployment

To deploy this project run

```bash
  npm run deploy
```
