from flask import Flask, render_template, request
import yt_dlp
import os

folder_tujuan = 'downloads'
if not os.path.exists(folder_tujuan):
    os.makedirs(folder_tujuan)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    # Mengambil data 'url' yang dikirim oleh API.js
    video_url = request.form.get('url') 
    
    if not video_url:
        return "Error: URL tidak ditemukan"

    opsi = {
        'format' : 'bestaudio/best',
        'ffmpeg_location': './ffmpeg.exe',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
        # Menggunakan 'r' agar path Windows tidak error
        'outtmpl' : os.path.join(folder_tujuan, '%(title)s.%(ext)s'),
    }
    
    try:
        with yt_dlp.YoutubeDL(opsi) as ydl:
            ydl.download([video_url])
        return "Berhasil !!! Cek folder D:/BELAJAR/downloadanlagu"
    except Exception as e:
        return f"Error: {e}"
    
if __name__ == '__main__':
    app.run(debug=True)