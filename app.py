from pytube import YouTube
from flask import Flask, render_template, request, send_file
import os
import tempfile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Download', methods=['POST'])
def YouTubeDownloader():
    video_url = request.form['url']
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()

    # Download video to a temporary directory
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, stream.default_filename)
    stream.download(output_path=temp_dir)

    # Send the file to the user
    return send_file(temp_file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
