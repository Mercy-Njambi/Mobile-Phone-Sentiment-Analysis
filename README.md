
# MOBILE PHONES SENTIMENT ANALYSIS
**Team Members:** 

* [Mercy Mukundi](https://github.com/Mercy-Njambi/)
* [Daniel Oselu](https://github.com/danieloselu3)
* [Roseline Maina](https://github.com/mainaroseline)
* [Vivian King'asia](https://github.com/VivianKingasia)
* [Elsie Juma](https://github.com/E-Juliet)
* [Mercy Ngila](https://github.com/MercyNgila)

## OVERVIEW
Building  a Sentiment predictor for consumers’ satisfaction on mobile phone products based on the reviews.

## BUSINESS PROBLEM
Purchasing a product is an interaction between two entities, consumers and business owners. Consumers often use reviews to make decisions about what products to buy, while businesses, on the other hand, not only want to sell their products but also want to receive feedback in terms of consumer reviews. 

Consumer reviews about purchased products shared on the internet have a great impact. Human nature is generally structured to make decisions based on analyzing and getting the benefit of other consumer experience and opinions because others often have a great influence on our beliefs, behaviors, perception of reality, and the choices we make. Hence, we ask others for their feedback whenever we are deciding on doing something.

In this research, we attempt to build a predictor for consumers’ satisfaction on mobile phone products based on the reviews. We will also attempt to understand the factors that contribute to classifying reviews as positive, negative or neutral (based on important or most frequent words). This is believed to help companies improve their products and also help potential buyers make better decisions when buying products.

## DATA
The data used for this project is scraped from `Amazon.com` and contains more than 1,7000 reviews of unlocked mobile phones. 

The data contains 6 columns:

* **`Product_name`** : Contains the name of the product
* **`Brand`** : Contains the brand of the product
* **`Price`** : Contains the price of the brans
* **`Rating`** : Contains the rating awarded to that product
* **`Reviews`** : Contains the review of that product
* **`Review_votes`** : Number of people who found the review helpful

```
├── code
│   ├── __init__.py
|
├── data
├── images
├── __init__.py
├── README.md
├── Non-Technical-Presentation.pdf
└── Mobile-Phone-Sentiment-Analysis.ipynb
```