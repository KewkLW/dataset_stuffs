# Web Scraping Script

## Overview

This repository contains a web scraping script implemented in Node.js. The script fetches a webpage's content, processes it using Mercury Parser, and then writes the processed text to a file.

## Dependencies

- `node-fetch`: For fetching web page content.
- `cheerio`: For parsing HTML and manipulating it.
- `@postlight/mercury-parser`: For extracting the main content from the webpage.

## How to Run

1. Make sure you've installed the required Node.js packages.
2. Update the `targetUrl` and `outputFileName` variables in `scrape_new.mjs`.
3. Run the script with `node scrape_new.mjs`.

## Files

- `scrape_new.mjs`: The main web scraping script.

## Assessment of Output Files

Two output files were generated from the same website but using different scripts. After careful evaluation, the following conclusions were made:

- `output.txt`: Focuses on the essential content. Recommended if you're interested in just the core information.
- `output2.txt`: Includes additional elements such as navigation menus and UI components. May contain redundant information.

## Recommendation

For most cases, `output.txt` is recommended as it focuses on essential, content-focused information.

