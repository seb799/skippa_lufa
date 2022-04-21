# Lufa Basket Cancellation
This repository contains a script to automatically cancel a Lufa order for a given week. 

## Why
In response to Lufa disabling the manual basket activation feature and bringing back the automatic weekly deliveries. 

## How
Simply schedule the cancel_order.py script using the Windows task scheduler or Cron on Linux/Unix. 

Credentials must be set in a .env file in the root directory of this repo. 

USER_EMAIL = 'randomemail@gmail.com'

USER_PW = 'randompassword123?'

## Chromedriver
Chromedriver.exe must match Chrome version. Currently 100.x

Chromedrive updates can be found [here](https://chromedriver.chromium.org/downloads)


