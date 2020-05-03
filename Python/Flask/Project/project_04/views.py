from flask import jsonify, request

from app import app, db
from model import District, Street, RequestHelp, Volunteer


@app.route('/')
def main():
    return '<h1>WORK</h1>'


@app.route('/districts', methods=['GET'])
def get_districts():
    districts = db.session.query(District).all()
    if districts:
        districts_out = []
        for district in districts:
            dict_district = dict(id=district.id, title=district.title)
            districts_out.append(dict_district)
        return jsonify(districts_out)
    return jsonify(), 404


@app.route('/streets', methods=['GET'])
def get_streets():
    district = request.args.get('district')
    if district:
        streets = db.session.query(Street).filter(Street.district_id == int(district)).all()
    else:
        streets = db.session.query(Street).all()
    if streets:
        street_out = []
        for street in streets:
            street_dict = dict(id=street.id, title=street.title)
            street_out.append(street_dict)
        return jsonify(street_out)
    return jsonify(), 404


@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    street = request.args.get('streets')
    if street:
        volunteers = db.session.query(Volunteer).filter(Volunteer.street_id == int(street)).all()
        if volunteers:
            volunteers_out = []
            for volunteer in volunteers:
                volunteer_dict = dict(id=volunteer.id, name=volunteer.name, phone=volunteer.phone)
                volunteers_out.append(volunteer_dict)
            return jsonify(volunteers_out)
    return jsonify(), 404


@app.route('/helpme', methods=['POST'])
def set_request_help():
    data = request.get_json()
    if data:
        try:
            street = db.session.query(Street).get(int(data['microdistrict']))
            if street:
                if street.district_id == int(data['district']):
                    new_request_help = RequestHelp(name=data['name'], surname=data['surname'], phone=data['phone'],
                                                   text=data['text'], address=data['address'],
                                                   district_id=int(data['district']),
                                                   microdistrict_id=int(data['microdistrict']), status='new')
                    db.session.add(new_request_help)
                    db.session.commit()
                    response = jsonify(status='success')
                    response.status_code = 201
                    response.headers['location'] = '/helpme'
                else:
                    response = jsonify(status='bad_adress')
                    response.status_code = 400
            else:
                response = jsonify(status='not_adress')
                response.status_code = 400

        except KeyError:
            response = jsonify(status='bad_data')
            response.status_code = 400

    return response
