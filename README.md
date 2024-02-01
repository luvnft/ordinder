# coordinates-tinder
Think ordinals, swipe left, swipe right.

## About
The interfaces for buying NFTs such as Opensea do not allow for users to explore NFTs.  Netflix, a pioneer in the streaming industry, has revolutionized the way viewers discover content through its innovative use of machine learning. This technology underpins their recommendation engine, a system that analyzes vast amounts of data to suggest films, series, and documentaries tailored to individual tastes. By examining user interactions, such as what they watch, how long they watch it, and their ratings, Netflix's algorithms create a highly personalized viewing experience. The system even considers factors like the time of day and the device being used for streaming. This sophisticated approach not only enhances user satisfaction by making content discovery effortless and intuitive but also benefits Netflix by increasing viewer engagement and retention. The success of this machine learning-driven recommendation system has set a benchmark in the industry, influencing how other streaming services approach content curation.

An academic paper titled "Deep Learning for Recommender Systems: A Netflix Case Study" by Steck et al., published in AI Magazine, discusses the impact of deep learning on Netflix's recommender systems. The paper outlines the challenges and lessons learned in implementing deep learning for these systems at Netflix. It highlights that different model architectures are effective for various recommendation tasks and that significant performance improvements were only observed when numerous heterogeneous features were added to the input data. This study provides insights into how deep learning has led to substantial improvements in Netflix's recommendations, both offline and online. For more details, you can refer to the full paper [here](https://ojs.aaai.org/index.php/aimagazine/article/view/18140).

Similarly, Tinder's innovative swipe interface, which popularized the simple 'swipe right to like, swipe left to pass' concept, revolutionized the online dating experience. This intuitive design made user decisions quick and easy, significantly streamlining the process of finding potential matches. By reducing the complexity of interacting with a dating app, Tinder attracted a broad user base, becoming a cultural phenomenon. Its swipe mechanism, mimicking the natural process of selection or rejection, also added a gamified element to dating, making it more engaging and less daunting for users. This innovation not only transformed the online dating landscape but also influenced user interface design in various other applications.

## This project
This project aims to combine both "match making" techinques to allow users to browse new creators that they perhaps would not discover.

## User profiles
By using the blockchain, we can obtain some demographics about the customer.

* First seen on chain
* Trade / In Out volume
* Trade frequence
* Balances
* Holding time

## Installation
```
yarn install coordinates-tinder
```

## Running the Python API
```bash
uvicorn main:app --reload
```
