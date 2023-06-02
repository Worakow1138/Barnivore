# Barnivore Test Plan

- [Barnivore Test Plan](#barnivore-test-plan)
  - [Introduction](#introduction)
  - [Basic Page Test Suite](#basic-page-tests-suite)
    - [Basic Page Preconditions](#basic-page-preconditions)
    - [Basic Page Test Cases](#basic-page-test-cases)
  - [Company Search Test Suite](#company-search-test-suite)
    - [Company Search Preconditions](#company-search-preconditions)
    - [Company Search Test Cases](#company-search-test-cases)
  - [Product Evaluation Test Suite](#product-evaluation-test-suite)
    - [Product Evaluation Preconditions](#product-evaluation-preconditions)
    - [Product Evaluation Test Cases](#product-evaluation-test-cases)
  - [Ask A Company Page Test Suite](#ask-a-company-page-test-suite)
    - [Ask A Company Page Preconditions](#ask-a-company-page-preconditions)
    - [Ask A Company Page Test Cases](#ask-a-company-page-test-cases)
  - [Data Validation Test Suite](#data-validation-test-suite)
    - [Data Validation Preconditions](#data-validation-preconditions)
    - [Data Validation Test Cases](#data-validation-test-cases)

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
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

## Product Evaluation Test Suite
Verify that when products are selected from a search list, they display expected information

### Product Evaluation Preconditions
1. A company to search for that has options labeled "Vegan Friendly", "Not Vegan Friendly", and "Unknown"
2. Open a web browser to [barnivore.com](https://www.barnivore.com/)
3. Verify that the search bar and search buttons are present
4. Enter the company name into the search box
5. Select the "Search" button
6. "Search results for (company name)" is in the Header
7. The Search bar is preloaded with the company name
8. A list of products is diplayed

### Product Evaluation Test Cases
1. Vegan Friendly
- Find a product on the list marked as "Vegan Friendly"
- Verify the product is marked with a Green square
- Select the product link and verify that the product's page is loaded
- Verify that the page title has the text "(product) is Vegan Friendly"
- Verify that the text "by (company name)" is present
- Verify that text entries for the following exist:
  - Address:
  - Phone:
  - Email:
  - URL:
  - Checked by:
  - Double checked by:
  - Added:
  - Double Checked:
- Verify that at least one "Company email" paragraph exists
- Verify that a list of products all from the company are present
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

2. Not Vegan Friendly
- Find a product on the list marked as "Not Vegan Friendly"
- Verify the product is marked with a Red square
- Select the product link and verify that the product's page is loaded
- Verify that the page title has the text "(product) is Not Vegan Friendly"
- Verify that the text "by (company name)" is present
- Verify that text entries for the following exist:
  - Address:
  - Phone:
  - Email:
  - URL:
  - Checked by:
  - Double checked by:
  - Added:
  - Double Checked:
- Verify that at least one "Company email" paragraph exists
- Verify that a list of products all from the company are present
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

3. Unknown
- Find a product on the list marked as "Unknown"
- Verify the product is marked with a Yello square
- Select the product link and verify that the product's page is loaded
- Verify that the page title has the text "(product) is Unknown"
- Verify that the text "by (company name)" is present
- Verify that text entries for the following exist:
  - Address:
  - Phone:
  - Email:
  - URL:
  - Checked by:
  - Double checked by:
  - Added:
  - Double Checked:
- Verify that at least one "Company email" paragraph exists
- Verify that a list of products all from the company are present
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

## Ask A Company Page Test Suite
Verify that expected text is displayed when selecting different languages and entering brand and personal information on the Ask a Company page 

### Ask A Company Page Preconditions
1. Open a web browser to [barnivore.com/askacompany](https://www.barnivore.com/askacompany)
2. Expected text appears in "The Question" and "The Response" areas of the page
3. Language selectors for the question, non-vegan response, and vegan response areas are present
4. Brand Name and Your Name inputs are present
5. "Find Booze:" with a search bar and search button is displayed
6. "Please Drink Responsibly" is at the bottom of the page
7. Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
8. "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

### Ask A Company Page Test Cases
1. English
- Set the "Question" language to English
- Verify that the question text is in English
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to English
- Verify that the non vegan response text is in English
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to English
- Verify that the vegan response text is in English
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

2. French
- Set the "Question" language to French
- Verify that the question text is in French
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to French
- Verify that the non vegan response text is in French
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to French
- Verify that the vegan response text is in French
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

3. Hebrew
- Set the "Question" language to Hebrew
- Verify that the question text is in Hebrew
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

4. Danish
- Set the "Question" language to Danish
- Verify that the question text is in Danish
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Danish
- Verify that the non vegan response text is in Danish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Danish
- Verify that the vegan response text is in Danish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

5. Ukrainian
- Set the "Question" language to Ukrainian
- Verify that the question text is in Ukrainian
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Ukrainian
- Verify that the non vegan response text is in Ukrainian
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Ukrainian
- Verify that the vegan response text is in Ukrainian
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

6. Arabic
- Set the "Question" language to Arabic
- Verify that the question text is in Arabic
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

7. Brazilian Portuguese
- Set the "Question" language to Brazilian Portuguese
- Verify that the question text is in Brazilian Portuguese
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Brazilian Portuguese
- Verify that the non vegan response text is in Brazilian Portuguese
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively

8. Croat
- Set the "Question" language to Croat
- Verify that the question text is in Croat
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

9. Dutch
- Set the "Question" language to Dutch
- Verify that the question text is in Dutch
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Dutch
- Verify that the non vegan response text is in Dutch
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Dutch
- Verify that the vegan response text is in Dutch
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

10. Finnish
- Set the "Question" language to Finnish
- Verify that the question text is in Finnish
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Finnish
- Verify that the non vegan response text is in Finnish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively

11. German
- Set the "Question" language to German
- Verify that the question text is in German
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to German
- Verify that the non vegan response text is in German
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to German
- Verify that the vegan response text is in German
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

12. Greek
- Set the "Question" language to Greek
- Verify that the question text is in Greek
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

13. Hindi
- Set the "Question" language to Hindi
- Verify that the question text is in Hindi
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

14. Icelandic
- Set the "Question" language to Icelandic
- Verify that the question text is in Icelandic
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

15. Italian
- Set the "Question" language to Italian
- Verify that the question text is in Italian
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Italian
- Verify that the non vegan response text is in Italian
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively

16. Japanese
- Set the "Question" language to Japanese
- Verify that the question text is in Japanese
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

17. Korean
- Set the "Question" language to Korean
- Verify that the question text is in Korean
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

18. Norwegian
- Set the "Question" language to Norwegian
- Verify that the question text is in Norwegian
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

19. Polish
- Set the "Question" language to Polish
- Verify that the question text is in Polish
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

20. Portuguese
- Set the "Question" language to Portuguese
- Verify that the question text is in Portuguese
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Portuguese
- Verify that the non vegan response text is in Portuguese
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Portuguese
- Verify that the vegan response text is in Portuguese
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

21. Russian
- Set the "Question" language to Russian
- Verify that the question text is in Russian
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Russian
- Verify that the non vegan response text is in Russian
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Russian
- Verify that the vegan response text is in Russian
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

22. Slovak
- Set the "Question" language to Slovak
- Verify that the question text is in Slovak
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

23. Slovenian
- Set the "Question" language to Slovenian
- Verify that the question text is in Slovenian
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively

24. Spanish
- Set the "Question" language to Spanish
- Verify that the question text is in Spanish
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Spanish
- Verify that the non vegan response text is in Spanish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Spanish
- Verify that the vegan response text is in Spanish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

25. Swedish
- Set the "Question" language to Swedish
- Verify that the question text is in Swedish
- Verify that "[BRAND NAME]" and/or "[YOUR NAME]" populate the question text in appropriate places
- Set the "Non Vegan Response" language to Swedish
- Verify that the non vegan response text is in Swedish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the non vegan response text in appropriate places
- Set the "Vegan Response" language to Swedish
- Verify that the vegan response text is in Swedish
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" populate the vegan response text in appropriate places 
- Change the "Brand Name:" field to a desired value
- Change the "Your Name:" field to a desired value
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the question text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the non vegan response text are replaced by the entered brand name and your name, respectively
- Verify that the "[BRAND NAME]" and/or "[YOUR NAME]" sections of the vegan response text are replaced by the entered brand name and your name, respectively

## Data Validation Test Suite
Validatate that filters on the "Beer", "Cider", "Wine", and "Liquor" pages correctly filter available product data and that this data is presented alphabetically

### Data Validation Preconditions
1. Open a web browser to [barnivore.com](https://www.barnivore.com/)
2. Load the "Beer", "Cider", "Wine", or "Liquor" page
3. The "Filters" widget is present with the "By Letter", "By veganosity", and "Country" options
4. If applicable, a country is selected from the region dropdown

### Data Validation Test Cases
1. All Filter
- Select the "All" filter
- Select the "Everything" filter
- The header displays "Listing all beers from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

2. All Filter Only Vegan
- Select the "All" filter
- Select the "Only Vegan" filter
- The header displays "Listing all beers from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

3. 0-9 Filter
- Select the "0-9" filter
- Select the "Everything" filter
- The header displays "Listing beers 0-9 from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

4. 0-9 Filter Only Vegan
- Select the "0-9" filter
- Select the "Only Vegan" filter
- The header displays "Listing vegan beers 0-9 from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

5. A-F Filter
- Select the "A-F" filter
- Select the "Everything" filter
- The header displays "Listing beers A-F from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

6. A-F Filter Only Vegan
- Select the "A-F" filter
- Select the "Only Vegan" filter
- The header displays "Listing vegan beers A-F from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

7. G-L Filter
- Select the "G-L" filter
- Select the "Everything" filter
- The header displays "Listing beers G-L from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

8. G-L Filter Only Vegan
- Select the "G-L" filter
- Select the "Only Vegan" filter
- The header displays "Listing vegan beers G-L from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

9. M-R Filter
- Select the "M-R" filter
- Select the "Everything" filter
- The header displays "Listing beers M-R from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

10. M-R Filter Only Vegan
- Select the "M-R" filter
- Select the "Only Vegan" filter
- The header displays "Listing vegan beers M-R from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

11. S-T Filter
- Select the "S-T" filter
- Select the "Everything" filter
- The header displays "Listing beers S-T from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

12. S-T Filter Only Vegan
- Select the "S-T" filter
- Select the "Only Vegan" filter
- The header displays "Listing vegan beers S-T from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

13. U-Z Filter
- Select the "U-Z" filter
- Select the "Everything" filter
- The header displays "Listing beers U-Z from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page

14. U-Z Filter Only Vegan
- Select the "U-Z" filter
- Select the "Only Vegan" filter
- The header displays "Listing vegan beers U-Z from specified country"
- The subheader displays "(Displaying products 1-50 of (total number) in total)"
- A list of products is displayed, no greater than 50
- No entry in the list starts with a character outside the filtered scope
- The list of products is in alphebetical order
- The list of products all indicated that they are from the specified country in their company field
- All product labels are correct: "VF" is green, "NVF" is red, "U" is yellow
- "Find Booze:" with a search bar and search button is displayed
- "Please Drink Responsibly" is at the bottom of the page
- Links for "Vegan Beer", "Vegan Wine", and "Vegan Liquor" are at the bottom of the page
- "Contents copyright © 2023 Thrust Labs. All rights reserved. Contact Us | Terms of Use/Privacy Policy" is at the bottom of the page