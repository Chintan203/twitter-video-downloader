from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        tweet_url = request.form['url']
        if tweet_url:
            command = ['yt-dlp', '-f', 'best', '-g', tweet_url]
            try:
                video_url = subprocess.check_output(command).decode('utf-8').strip()
            except subprocess.CalledProcessError:
                video_url = "ERROR: Unable to download video."
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
