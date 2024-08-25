@app.route('/grievance', methods=['POST'])
@jwt_required()
def submit_grievance():
    data = request.json
    content = data.get('content', '')
    if not content:
        return jsonify({'msg': 'Content is required'}), 400
    # Further validation and processing

