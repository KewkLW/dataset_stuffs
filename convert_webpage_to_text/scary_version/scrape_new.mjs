// Dynamic import for node-fetch due to ESM
import fetch from 'node-fetch';
import cheerio from 'cheerio';
import Mercury from '@postlight/mercury-parser';
import fs from 'fs/promises';

// Configurable Options
const targetUrl = 'https://huggingface.co/BAAI/bge-large-en';  // Replace with your target URL
const outputFileName = 'output.txt';  // Desired output file name
const stripHtmlTags = true;  // true to strip HTML tags, false otherwise
const fixEncoding = false;  // true to fix encoding issues, false otherwise
const mercuryOptions = { contentType: 'text' };  // Mercury Parser options

// Fetch and process webpage content
fetch(targetUrl)
  .then(res => res.text())
  .then(html => {
    const $ = cheerio.load(html);
    return Mercury.parse(targetUrl, mercuryOptions);
  })
  .then(result => {
    let content = result.content;

    if (stripHtmlTags) {
      content = content.replace(/<\/?[^>]+(>|$)/g, '');
    }

    if (fixEncoding) {
      try {
        content = decodeURIComponent(escape(content));
      } catch (err) {
        console.error('Failed to fix encoding:', err);
      }
    }

    return fs.writeFile(outputFileName, content);
  })
  .then(() => {
    console.log(`Content has been written to ${outputFileName}`);
  })
  .catch(err => {
    console.error(err);
  });
