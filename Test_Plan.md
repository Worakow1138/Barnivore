# Barnivore Test Plan

- [Barnivore Test Plan](#barnivore-test-plan)
  - [Introduction](#introduction)
  - [Header Suite](#header-suite)
    - [Preconditions](#preconditions)
    - [Test Cases](#test-cases)

## Introduction
Detailed explanations of test steps for the [barnivore.com](https://www.barnivore.com/) website

## Header Suite
Verify that anticipated data is returned from each header page on the barnivore website.

### Preconditions
1. Open a web browser to [barnivore.com](https://www.barnivore.com/)
2. Verify that tabs for "Beer", "Cider", "Wine", "Liquor", "Ask a Company", "Mobile Apps", "Contact", and "FAQ" are present

### Test Cases
1. Beer Page:
- Select the "Beer" header
- The ["Beer"](https://www.barnivore.com/beer) page is loaded
- The "Filters" widget is present with the "By Letter", "By veganosity", and "Country" options
- "Listing beers..." header is present
- "(Diplaying products 1 - 50 of (some number) in total)" is displayed
- A list of 50 beers is displayed in alphabetical order
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved.
Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page"