REGEX_PATTERNS = {
    'pattern1': {
        'name': '(a|b)*abb',
        'description': 'Cadenas que terminan en "abb"',
        'states': ['q0', 'q1', 'q2', 'q3', 'accept', 'reject'],
        'alphabet': ['a', 'b', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q0', 'b'): ('q0', 'b', 'R'),
            ('q0', '_'): ('reject', '_', 'R'),
            ('q1', 'a'): ('q1', 'a', 'R'),
            ('q1', 'b'): ('q2', 'b', 'R'),
            ('q1', '_'): ('reject', '_', 'R'),
            ('q2', 'a'): ('q1', 'a', 'R'),
            ('q2', 'b'): ('q3', 'b', 'R'),
            ('q2', '_'): ('reject', '_', 'R'),
            ('q3', 'a'): ('q1', 'a', 'R'),
            ('q3', 'b'): ('q0', 'b', 'R'),
            ('q3', '_'): ('accept', '_', 'R')
        }
    },
    'pattern2': {
        'name': '0*1*',
        'description': 'Ceros seguidos de unos',
        'states': ['q0', 'q1', 'accept', 'reject'],
        'alphabet': ['0', '1', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', '0'): ('q0', '0', 'R'),
            ('q0', '1'): ('q1', '1', 'R'),
            ('q0', '_'): ('accept', '_', 'R'),
            ('q1', '1'): ('q1', '1', 'R'),
            ('q1', '0'): ('reject', '0', 'R'),
            ('q1', '_'): ('accept', '_', 'R')
        }
    },
    'pattern3': {
        'name': '(ab)*',
        'description': 'Repeticiones de "ab"',
        'states': ['q0', 'q1', 'accept', 'reject'],
        'alphabet': ['a', 'b', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q0', 'b'): ('reject', 'b', 'R'),
            ('q0', '_'): ('accept', '_', 'R'),
            ('q1', 'b'): ('q0', 'b', 'R'),
            ('q1', 'a'): ('reject', 'a', 'R'),
            ('q1', '_'): ('reject', '_', 'R')
        }
    },
    'pattern4': {
        'name': '1(01)*0',
        'description': 'Empieza con 1, termina con 0, "01" en el medio',
        'states': ['q0', 'q1', 'q2', 'q3', 'accept', 'reject'],
        'alphabet': ['0', '1', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', '1'): ('q1', '1', 'R'),
            ('q0', '0'): ('reject', '0', 'R'),
            ('q0', '_'): ('reject', '_', 'R'),
            ('q1', '0'): ('q2', '0', 'R'),
            ('q1', '1'): ('reject', '1', 'R'),
            ('q1', '_'): ('reject', '_', 'R'),
            ('q2', '1'): ('q1', '1', 'R'),
            ('q2', '0'): ('reject', '0', 'R'),
            ('q2', '_'): ('accept', '_', 'R')
        }
    },
    'pattern5': {
        'name': '(a+b)*a(a+b)*',
        'description': 'Contiene al menos una "a"',
        'states': ['q0', 'q1', 'accept', 'reject'],
        'alphabet': ['a', 'b', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q0', 'b'): ('q0', 'b', 'R'),
            ('q0', '_'): ('reject', '_', 'R'),
            ('q1', 'a'): ('q1', 'a', 'R'),
            ('q1', 'b'): ('q1', 'b', 'R'),
            ('q1', '_'): ('accept', '_', 'R')
        }
    },
    'pattern6': {
        'name': 'a*b*',
        'description': 'Aes seguidas de bes',
        'states': ['q0', 'q1', 'accept', 'reject'],
        'alphabet': ['a', 'b', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'a'): ('q0', 'a', 'R'),
            ('q0', 'b'): ('q1', 'b', 'R'),
            ('q0', '_'): ('accept', '_', 'R'),
            ('q1', 'b'): ('q1', 'b', 'R'),
            ('q1', 'a'): ('reject', 'a', 'R'),
            ('q1', '_'): ('accept', '_', 'R')
        }
    },
    'pattern7': {
        'name': '(aa)*',
        'description': 'Número par de aes',
        'states': ['q0', 'q1', 'accept', 'reject'],
        'alphabet': ['a', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q0', '_'): ('accept', '_', 'R'),
            ('q1', 'a'): ('q0', 'a', 'R'),
            ('q1', '_'): ('reject', '_', 'R')
        }
    },
    'pattern8': {
        'name': '0+1+',
        'description': 'Al menos un 0 seguido de al menos un 1',
        'states': ['q0', 'q1', 'q2', 'accept', 'reject'],
        'alphabet': ['0', '1', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', '0'): ('q1', '0', 'R'),
            ('q0', '1'): ('reject', '1', 'R'),
            ('q0', '_'): ('reject', '_', 'R'),
            ('q1', '0'): ('q1', '0', 'R'),
            ('q1', '1'): ('q2', '1', 'R'),
            ('q1', '_'): ('reject', '_', 'R'),
            ('q2', '1'): ('q2', '1', 'R'),
            ('q2', '0'): ('reject', '0', 'R'),
            ('q2', '_'): ('accept', '_', 'R')
        }
    },
    'pattern9': {
        'name': '(ba)*',
        'description': 'Repeticiones de "ba"',
        'states': ['q0', 'q1', 'accept', 'reject'],
        'alphabet': ['a', 'b', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'b'): ('q1', 'b', 'R'),
            ('q0', 'a'): ('reject', 'a', 'R'),
            ('q0', '_'): ('accept', '_', 'R'),
            ('q1', 'a'): ('q0', 'a', 'R'),
            ('q1', 'b'): ('reject', 'b', 'R'),
            ('q1', '_'): ('reject', '_', 'R')
        }
    },
    'pattern10': {
        'name': 'a(a|b)*b',
        'description': 'Empieza con "a" y termina con "b"',
        'states': ['q0', 'q1', 'q2', 'accept', 'reject'],
        'alphabet': ['a', 'b', '_'],
        'start_state': 'q0',
        'accept_states': ['accept'],
        'reject_states': ['reject'],
        'transitions': {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q0', 'b'): ('reject', 'b', 'R'),
            ('q0', '_'): ('reject', '_', 'R'),
            ('q1', 'a'): ('q1', 'a', 'R'),
            ('q1', 'b'): ('q2', 'b', 'R'),
            ('q1', '_'): ('reject', '_', 'R'),
            ('q2', 'a'): ('q1', 'a', 'R'),
            ('q2', 'b'): ('q2', 'b', 'R'),
            ('q2', '_'): ('accept', '_', 'R')
        }
    }
}