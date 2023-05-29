# Barnivore Test Plan

- [Barnivore Test Plan](#barnivore-test-plan)
  - [Introduction](#introduction)
  - [Basic Page Tests Suite](#basic-page-tests-suite)
    - [Basic Page Preconditions](#basic-page-preconditions)
    - [Basic Page Test Cases](#basic-page-test-cases)
  - [Company Search Tests Suite](#company-search-test-suite)
    - [Company Search Preconditions](#company-search-preconditions)
    - [Company Search Test Cases](#company-search-test-cases)

## Introduction
Detailed explanations of test steps for the [barnivore.com](https://www.barnivore.com/) website

## Basic Page Tests Suite
Verify that basic functionality is covered on the main barnivore pages. Basic functionality is defined as expected data from each main page being returned correctly.

### Basic Page Preconditions
1. Open a web browser to [barnivore.com](https://www.barnivore.com/)
2. Verify that tabs for "Beer", "Cider", "Wine", "Liquor", "Ask a Company", "Mobile Apps", "Contact", and "FAQ" are present
3. Verify that the search bar and search buttons are present

### Basic Page Test Cases
1. Home Page:
- The ["Home"](https://www.barnivore.com/) page is loaded
- The Home search bar and search buttons are displayed
- Expected text for the Home page is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

2. Beer Page:
- Select the "Beer" header
- The ["Beer"](https://www.barnivore.com/beer) page is loaded
- The "Filters" widget is present with the "By Letter", "By veganosity", and "Country" options
- "Listing beers..." header is present
- "(Diplaying products 1 - 50 of (some number) in total)" is displayed
- A list of 50 beers is displayed
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

3. Cider Page:
- Select the "Cider" header
- The ["Cider"](https://www.barnivore.com/cider) page is loaded
- The "Filters" widget is present with the "By Letter", "By veganosity", and "Country" options
- "Listing ciders..." header is present
- "(Diplaying products 1 - 50 of (some number) in total)" is displayed
- A list of 50 ciders is displayed
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

4. Wine Page:
- Select the "Wine" header
- The ["Wine"](https://www.barnivore.com/wine) page is loaded
- The "Filters" widget is present with the "By Letter", "By veganosity", and "Country" options
- "Listing wines..." header is present
- "(Diplaying products 1 - 50 of (some number) in total)" is displayed
- A list of 50 wines is displayed
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

5. Liquor Page:
- Select the "Liquor" header
- The ["Liquor"](https://www.barnivore.com/liquor) page is loaded
- The "Filters" widget is present with the "By Letter", "By veganosity", and "Country" options
- "Listing liquors..." header is present
- "(Diplaying products 1 - 50 of (some number) in total)" is displayed
- A list of 50 liquors is displayed
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

6. Ask a Company Page:
- Select the "Ask a Company" header
- The ["Ask a Company"](https://www.barnivore.com/askacompany) page is loaded
- Expected text appears in "The Question" and "The Response" areas of the page
- Language selectors for the question, non-vegan response, and vegan response areas are present
- Brand Name and Your Name inputs are present
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

7. Mobile Apps Page:
- Select the "Mobile Apps" header
- The ["Mobile Apps"](https://www.barnivore.com/mobile) page is loaded
- "Barnivore on the go" text is present
- Links for Patreon page and Twitter are present
- Links for full-text views of beer, cider, wine, and liquor pages are present
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

8. Contact Page:
- Select the "Contact" header
- The ["Contact"](https://www.barnivore.com/contact) page is loaded
- The "Contact Us" text is present
- The contact@barnvore.com email link is present
- A link to the "Ask a Company" page with text "available here" is present
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

9. FAQ Page:
- Select the "FAQ" header
- The ["FAQ"](https://www.barnivore.com/faq) page is loaded
- All "FAQ" text is present
- Links to Ask a Company page are present
- Links to Contact page are present
- Link to Terms of Use page is present
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

## Company Search Test Suite
Verify that the Search tool can be used to find multiple results that target a single company

### Company Search Preconditions
1. Open a web browser to [barnivore.com](https://www.barnivore.com/)
2. Verify that tabs for "Beer", "Cider", "Wine", "Liquor", "Ask a Company", "Mobile Apps", "Contact", and "FAQ" are present
3. Verify that the search bar and search buttons are present
4. Possess a list of companies known to produce alcoholic beverages

### Company Search Test Cases
1. (All Company Search Tests follow this format, regardless of data)
- Enter the company name into the search box
- Select the "Search" button
- "Search results for (company name)" is in the Header
- The Search bar is preloaded with the company name
- A list of products is diplayed
- All products are producted by the company searched for
- All products possess a link to their product page
- All products have a label of either "Vegan Friendly", "Not Vegan Friendly", or "Unknown"
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow