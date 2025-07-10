# Web Scraping Toolkit

A collection of Python scripts focused on advanced **web scraping techniques**, including handling **AJAX**, **CSRF tokens**, **iframes**, **dynamic tables**, and **authentication-based content**.

This toolkit is specifically designed to scrape data from [scrapethissite.com](https://scrapethissite.com), a website built for practicing web scraping.

## Overview

This project demonstrates how to extract data from complex or protected websites using various techniques:

- **AJAX requests handling** – Simulate background requests for dynamic content
- **CSRF token extraction** – Automatically detect and include CSRF tokens in POST requests
- **Iframe content parsing** – Access and extract content loaded in `<iframe>` tags
- **HTML table data extraction** – Parse structured data from `<table>` elements
- **Link spoofing via `href`** – Follow or modify links dynamically to reach hidden data
- **Scraping while logged into a session** – Maintain login state using cookies or sessions
