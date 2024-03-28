## YouTube Video Fetcher API

### Overview
This API fetches the latest YouTube videos based on a specified date (`publishedAfter`) and stores them into a database if the video is not present earlier. It also displays the number of new videos retrieved after every call. Additionally, it provides optional parameters such as `query`, `per_page`, and `no_of_pages` to customize the results.

### Installation Steps
1. **Clone the Repository:**

2. **Create and Activate a Virtual Environment:**

3. **Install Dependencies:**
    pip install python-dotenv
    pip install flask...
    and other modules
  
5. **Set Database URL and YouTube API Key in `.env` File:**
    YouTube API Key will expire after 30 days
   
6. **Run the Application:**
    flask run

### Optional Parameters
You can use the following optional parameters to customize your search:
- `query`: Specify the search query. Default is 'cricket'.
- `per_page`: Number of videos per page. Default is 9.
- `no_of_pages`: Number of pages to fetch. Default is 5.

Example API containing all optional parameters:
http://127.0.0.1:5000/?query=animal&per_page=10&no_of_pages=6


### Usage
- Access the application at [http://localhost:5000](http://localhost:5000) in your web browser.
- Use the search bar to search for YouTube videos.
- The application will fetch and display the latest videos based on the search query.
- Videos will be stored in the database to avoid duplicate entries.
