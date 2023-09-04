#iAmKewk 
const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  console.log("Launching browser...");
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const url = 'https://example.com';  // Replace with the URL you want to scrape
  const output_file = 'output.txt';  // Name of the text file to save the content

  console.log(`Navigating to ${url}...`);
  await page.goto(url);

  console.log("Extracting content...");
  const content = await page.evaluate(() => {
    let textContent = '';
    const paragraphs = document.querySelectorAll('p');
    paragraphs.forEach((p) => {
      textContent += p.innerText + '\n';
    });
    return textContent;
  });

  console.log(`Saving content to ${output_file}...`);
  fs.writeFileSync(output_file, content);

  console.log("Done.");
  await browser.close();
})();
