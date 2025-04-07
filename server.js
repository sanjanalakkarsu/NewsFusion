const express = require('express');
const RSSParser = require('rss-parser');
const cors = require('cors');

const app = express();
const port = 5001;

// Enable CORS for all requests
app.use(cors());

// Define an endpoint to fetch RSS feed data
app.get('/fetch-rss', async (req, res) => {
    const rssUrl = req.query.url;  // Get the RSS URL from the query parameters
    const parser = new RSSParser();

    try {
        console.log('Fetching RSS URL:', rssUrl);  // Log the URL being fetched
        const feed = await parser.parseURL(rssUrl);  // Parse the RSS feed
        console.log('Fetched Feed:', feed);  // Log the parsed feed
        res.json({ status: 'success', articles: feed.items });  // Send articles as JSON
    } catch (error) {
        console.error('Error fetching RSS:', error);  // Log detailed error message
        res.json({ status: 'error', message: 'Failed to fetch or parse RSS feed', error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
