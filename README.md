# IndexArbitrage

## Overview
This dashboard displays stocks that are likely to get removed from the S&P 500 due to a lowering of market capitalization. It is a common strategy among hedge funds to predict what stocks are likely to be removed from an index in order to place a short trade on that ticker. In recent years this strategy has not been as fruitful as it once was. 

![IndexArbImport drawio (1)](https://github.com/jhoward39/IndexArbitrage/assets/70383367/1231f579-d066-4ded-9e11-770a5c7dcfe9)


## Methodology 
The methodology behind this strategy is that if a stock is removed from S&P 500 the selling of shares by the many funds that track the index moves the price down. The decision to add or remove a stock from the index is made by a committee. This committee makes the decision based on market cap, broader sector trends, and is employed by the S&P Dow Jones Indices LLC. 

This is the committee's most recent update to the criteria for entry into the S&P 500:<be>
>In consideration of overall market conditions, the Index Committee believes a minimum threshold of $14.6 billion for the S&P 500 is appropriate. These ranges are reviewed >quarterly and updated as needed to assure consistency with market conditions. A company meeting the unadjusted company market capitalization criteria must also have a >security level float-adjusted market capitalization that is at least 50% of the respective index's unadjusted company level minimum market capitalization threshold.

>As a reminder, the market capitalization eligibility criteria are for addition to an index, not for continued membership. As a result, an index constituent that appears to >violate criteria for addition to that index is not removed unless ongoing conditions warrant an index change.


https://www.spglobal.com/spdji/en/documents/methodologies/methodology-index-math.pdf

## What This Is Not
There are other reasons that stocks can get removed from the S&P, usually mergers. This does not even attempt to predict that. Also, just because a stock falls below the S&P's minimum capitalization mark, does not automatically mean the committee will remove it from the index. It's an art, not a science. One thing is for certain, the committee watches it closely to look for signs of weakness. 

In the future, I would like to do an in-depth study of the history of companies that have been removed from the S&P for market capitalization reasons to possibly predict closer to when the index is likely to drop a stock. 

##
# LINK: https://indexarbitrage.azurewebsites.net/

## Notes
An index is just a basket of stocks, it does not become investable until a financial product is created that tracks the index.
There is no wikipedia page for the S&P Total Market Index while there is one for every other index




