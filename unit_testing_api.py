import unittest
import requests

class TestFlaskAPI(unittest.TestCase):
    base_url = "http://127.0.0.1:5000"
    def test_get_video(self):
        response = requests.get(f"{self.base_url}/video/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("video_id", data)
        self.assertIn("data", data)
        self.assertEqual(data["video_id"], 1)
        print("test get video", data)

    def test_get_video_not_found(self):
        response = requests.get(f"{self.base_url}/video/999")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("error", data)
        print("test get video not found", data)

    def test_get_videos_list(self):
        response = requests.get(f"{self.base_url}/videos")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("data", data)
        self.assertIsInstance(data["data"], dict)
        print("test get video list",data)

    def test_post_video(self):
        data = {"name": "New Video", "views": 50, "likes": 20}
        response = requests.post(f"{self.base_url}/video/4", json=data)
        self.assertEqual(response.status_code, 201)
        created_data = response.json()
        self.assertIn("video_id", created_data)
        self.assertIn("data", created_data)
        self.assertEqual(created_data["video_id"], 4)
        print("test post video",created_data)

    def test_post_video_invalid_data(self):
        data = {"name": "New Video", "views": 50}
        response = requests.post(f"{self.base_url}/video/5", json=data)
        self.assertEqual(response.status_code, 400)
        error_data = response.json()
        self.assertIn("error", error_data)
        print("test post video invalid data", error_data)

if __name__ == "__main__":
    unittest.main()
