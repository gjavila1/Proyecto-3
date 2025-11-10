from flask import Flask, render_template, request, jsonify
from turing_machine import TuringMachine
from regex_patterns import REGEX_PATTERNS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', patterns=REGEX_PATTERNS)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    input_string = data.get('input', '')
    pattern_key = data.get('pattern', '')
    
    if pattern_key not in REGEX_PATTERNS:
        return jsonify({'error': 'Patrón no válido'}), 400
    
    tm = TuringMachine(REGEX_PATTERNS[pattern_key])
    steps = tm.simulate(input_string)
    
    return jsonify({
        'steps': steps,
        'accepted': tm.is_accepted(),
        'pattern_name': pattern_key,
        'pattern_description': REGEX_PATTERNS[pattern_key]['description']
    })

if __name__ == '__main__':
    app.run(debug=True)