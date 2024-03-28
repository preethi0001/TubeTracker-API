from flask import Blueprint, current_app, request, jsonify
from .database import db
from .models import Video
import requests
from datetime import datetime, timedelta

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_latest_videos():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    query = request.args.get('query', default='cricket', type=str)
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=9, type=int)
    no_of_pages = request.args.get('no_of_pages', default=5, type=int)

    # Calculate the datetime for fetching videos published after a certain time
    published_after_datetime = datetime.utcnow() - timedelta(days=7)  # Fetch videos published in the last 7 days
    published_after_str = published_after_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

    search_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        'q': query,
        'part': 'snippet',
        'maxResults': per_page * no_of_pages,
        'type': 'video',
        'order': 'date',
        'publishedAfter': published_after_str
    }

    r = requests.get(search_url, params=search_params)
    search_results = r.json().get('items', [])

    if not search_results:
        return jsonify({'error': 'No videos found'}), 404

    video_ids = [item['id']['videoId'] for item in search_results]
    video_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        'id': ','.join(video_ids),
        'part': 'snippet',
        'maxResults': per_page
    }

    r = requests.get(video_url, params=video_params)
    video_results = r.json().get('items', [])
    
    videos_saved = 0  # Counter for the number of videos saved

    for item in video_results:
        video_id = item['id']
        
        # Check if video already exists in the database
        existing_video = Video.query.filter_by(id=video_id).first()
        if existing_video:
            continue  # Skip inserting the video if it already exists
        
        # Insert the video into the database
        video = Video(
            id=video_id,
            title=item['snippet']['title'],
            description=item['snippet']['description'],
            publishedAt=datetime.strptime(item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
            thumbnails=item['snippet']['thumbnails']['high']['url'],
            videoId=video_id
        )
        db.session.add(video)
        videos_saved += 1
    
    db.session.commit()

    return jsonify({'success': f'{videos_saved} new videos stored successfully', 'videos': video_results}), 200