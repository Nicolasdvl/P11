# Project 11 : 

This repo was created as part of coding learning with Open Classroom.  

The aim is to improve an application by implement a new feature, fix an bug, and fix a test.  
It based on application developed in this repo : https://github.com/Nicolasdvl/P8.  

## Fix

Fix was made on branch 'fix'. Code versionning visible [here](https://github.com/Nicolasdvl/P11/pull/1).

### Error 404 on '/product'.
- Context : The app contain a search bar on home page and on nav on every pages.  
The bug appear when user use it to search a inexistant product.  
- Error : 404 page not found.  
- Fix : Implement an intermediate page when user input doesn't match with name product in the database.  
This page display products similar to input or a feedback message to inform no product was found.  

### Fix Parser tests
- Context : Fixtures used to test Paser was not relevant. Fixtures changes highlight tests deficiences.  
- Error : Tests failed.  
- Fix : Change and refactor code to pass tests.  

### Fix selenium tests  
Note : This correction was not implement on 'fix' branch but on 'feature_user_claim' branch.
- Context : Selenium 4.3.0 remove find_elements_by_*  
- Error :  
    - AttributeError: 'WebDriver' object has no attribute 'find_element_by_name'  
    - AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'  
    - AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'   
- Fix : Change all recurrences of find_elements_by_*  


## New Feature

The implementation was made on branch 'feature_user_claim'. Code versionning visible [here](https://github.com/Nicolasdvl/P11/pull/2).

The feature allow user to claim for products missing in database.
- When user is auth, a link at bottom of 'similar' page suggest to claim for a missing product.
- When user is not auth, the link suggest to create an account or to connect before claimming for a missing product.  

The data submit by claim form is display on an admin page. Admin can deal with by accecpt or decline suggestions.