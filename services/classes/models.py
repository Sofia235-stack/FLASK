@class_routes.route('/', methods=['POST'])
def add_class():
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'Le nom de la classe est requis'}), 400

    new_class = Classe(name=data['name'])
    db.session.add(new_class)
    db.session.commit()

    return jsonify(new_class.to_dict()), 201
