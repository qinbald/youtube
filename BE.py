from flask import Flask, render_template, request, jsonify
import yt_dlp
import os
import syncedlyrics

app = Flask(__name__)

folder_tujuan = 'downloads'
if not os.path.exists(folder_tujuan):
    os.makedirs(folder_tujuan)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form.get('url') 
    
    if not video_url:
        return jsonify({"error": "URL tidak ditemukan"}), 400

    opsi = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
        'outtmpl' : os.path.join(folder_tujuan, '%(title)s.%(ext)s'),
        'nocheckcertificate': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(opsi) as ydl:
            info = ydl.extract_info(video_url, download=True)
            judul = info.get('title', 'Lagu')
            
            try:
                lirik_text = syncedlyrics.search(judul)
            except:
                lirik_text = "Lirik tidak ditemukan."

            return jsonify({
                "status": "Selesai",
                "judul": judul,
                "lirik": lirik_text or "Lirik tidak tersedia untuk lagu ini."
            })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)