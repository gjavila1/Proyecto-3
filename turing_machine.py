class TuringMachine:
    def __init__(self, pattern_config):
        self.states = pattern_config['states']
        self.alphabet = pattern_config['alphabet']
        self.transitions = pattern_config['transitions']
        self.start_state = pattern_config['start_state']
        self.accept_states = pattern_config['accept_states']
        self.reject_states = pattern_config.get('reject_states', ['reject'])
        
        self.reset()
    
    def reset(self):
        self.tape = []
        self.head_position = 0
        self.current_state = self.start_state
        self.steps = []
        self.accepted = False
    
    def simulate(self, input_string):
        self.reset()
        self.tape = list(input_string) + ['_'] * 10  # Padding con blanks
        
        max_steps = 1000  # Prevenir loops infinitos
        step_count = 0
        
        while (self.current_state not in self.accept_states and 
               self.current_state not in self.reject_states and 
               step_count < max_steps):
            
            self.steps.append(self._get_current_step())
            
            if not self._execute_step():
                break
                
            step_count += 1
        
        # Agregar paso final
        self.steps.append(self._get_current_step())
        self.accepted = self.current_state in self.accept_states
        
        return self.steps
    
    def _execute_step(self):
        if self.head_position >= len(self.tape):
            self.tape.extend(['_'] * 5)
        
        current_symbol = self.tape[self.head_position]
        transition_key = (self.current_state, current_symbol)
        
        if transition_key not in self.transitions:
            self.current_state = 'reject'
            return False
        
        new_state, write_symbol, direction = self.transitions[transition_key]
        
        self.tape[self.head_position] = write_symbol
        self.current_state = new_state
        
        if direction == 'R':
            self.head_position += 1
        elif direction == 'L':
            self.head_position = max(0, self.head_position - 1)
        
        return True
    
    def _get_current_step(self):
        return {
            'tape': self.tape[:max(20, self.head_position + 5)],
            'head_position': self.head_position,
            'current_state': self.current_state,
            'is_final': self.current_state in self.accept_states or self.current_state in self.reject_states
        }
    
    def is_accepted(self):
        return self.accepted