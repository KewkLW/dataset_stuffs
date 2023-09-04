# Web Scraping using Puppeteer

This repository contains a script for web scraping using Puppeteer, a Node library that provides a high-level API to control Chrome or Chromium over the DevTools Protocol.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Installation

1. Make sure you have Node.js and npm installed on your machine. If not, download and install it from [Node.js official site](https://nodejs.org/).

2. Clone this repository or download the script.

    ```bash
    svn checkout https://github.com/KewkLW/dataset_stuffs/trunk/convert_webpage_to_text
    ```

3. Navigate to the project directory.

    ```bash
    cd web-scraping-using-puppeteer
    ```

4. Install the required packages.

    ```bash
    npm install puppeteer
    ```

## Usage

1. Open the script in your preferred text editor.

2. Locate the following line to specify the URL you want to scrape:

    ```javascript
    const url = 'https://example.com';  // Replace with the URL you want to scrape
    ```

3. Save the changes.

4. Run the script using Node.js:

    ```bash
    node scrape.js
    ```

The script will launch a headless browser, navigate to the specified URL, and scrape the text content within the <p> tags. The scraped content will be saved in a text file named `output.txt`.

## Disclaimer

Web scraping can be against the Terms of Service of some websites. Ensure that you have the right to scrape the website and that you are respectful of the website's resources. This script doesn't respect `robots.txt` files; it's your responsibility to do so if required.
