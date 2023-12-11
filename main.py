from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos = {
    1: {'name': 'Video 1', 'views': 100, 'likes': 50},
    2: {'name': 'Video 2', 'views': 200, 'likes': 80},
    3: {'name': 'Video 3', 'views': 300, 'likes': 120},
}

class VideoResource(Resource):
    def get(self, video_id):
        video = videos.get(video_id)
        if video:
            return {'video_id': video_id, 'data': video}
        else:
            return {'error': 'Video not found'}, 404

    def post(self, video_id):
        json_data = request.get_json()
        if not json_data or 'name' not in json_data or 'views' not in json_data or 'likes' not in json_data:
            return {'error': 'Invalid request data'}, 400

        videos[video_id] = {'name': json_data['name'], 'views': json_data['views'], 'likes': json_data['likes']}
        return {'video_id': video_id, 'data': videos[video_id]}, 201
        
class VideosListResource(Resource):
    def get(self):
        query_params = request.args
        if query_params:
            filtered_videos = filter_videos(query_params)
            return {'data': filtered_videos}
        else:
            return {'data': videos}

def filter_videos(query_params):
    filtered_videos = []
    for video_id, video in videos.items():
        matches_all_criteria = all(
            str(video.get(key)) == query_params.get(key) for key in query_params.keys()
        )
        if matches_all_criteria:
            filtered_videos.append({'video_id': video_id, 'data': video})
    return filtered_videos

api.add_resource(VideoResource, '/video/<int:video_id>')
api.add_resource(VideosListResource, '/videos')

if __name__ == '__main__':
    app.run(debug=True)
