# Automated Tests for [Barnivore](https://www.barnivore.com/)

## What is Barnivore?
Barnivore is a comprehensive directory of vegan-friendly alcoholic beverages. It aims to assist individuals who follow a vegan lifestyle in making informed choices about the alcoholic beverages they consume. 
The website offers a platform where users can access a vast collection of information on various alcoholic products, including beers, ciders, wines, and spirits, to determine whether they are suitable for consumption. 
Barnivore gets its data from users and provides helpful templates for emailing companies to ask whether body parts or secretions of animals are used in their production process. 
The website is a valuable resource for vegans seeking to find cruelty-free options within the realm of alcoholic beverages.
Support Barnivore on [Patreon](https://www.patreon.com/barnivore/overview)!

## What this repo is:
A repository of automated tests to validate some of the core functionality of the Barnivore site.
This repository is not comprehensive and serves to ensure that the most visible features of the site are performing as intended as well as validation of some of the available alcohol data.

## Repository Structure

### Functional Tests
Functional tests are stored in Barnivore_Test_Suite_Desktop.py, Barnivore_Test_Suite_Mobile.py, and Barnivore_Test_Suite_Tablet.py.
These files possess duplicates of the same tests, but are run in different size viewports.

### Data Validation
Barnivore_Test_Suite_Data_Validation.py houses tests that evaluate filtering functions and verification that hundreds of different results are presented as expected.

## Test Structure
Details about coverage and structure of test suites and test cases may be found in the [Test_Plan](Test_Plan.md) file

## Requirements
These tests were created and run using [Python](https://www.python.org/) and the [Moonrise](https://pypi.org/project/moonrise/) test automation framework.