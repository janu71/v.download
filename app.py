from flask import Flask, request, jsonify
from flask_cors import CORS
from rahad_all_downloader import alldl

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/download', methods=['POST'])
def download():
    data = request.get_json()
    if not data or not data.get('url'):
        return jsonify({'success': False, 'error': 'URL প্রয়োজন'}), 400

    url = data['url'].strip()

    try:
        result = alldl(url)
        if result.get('success') and result.get('videoUrl'):
            return jsonify({
                'success': True,
                'videoUrl': result['videoUrl'],
                'title': result.get('data', {}).get('title', 'ভিডিও')
            })
        else:
            return jsonify({
                'success': False,
                'error': 'এই লিংক থেকে ভিডিও বের করা যায়নি। অন্য লিংক চেষ্টা করুন।'
            })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

app = app