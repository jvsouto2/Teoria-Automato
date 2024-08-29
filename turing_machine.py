class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transitions, initial_state, accept_state, reject_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.current_state = initial_state
        self.tape = {}  
        self.head_position = 0
    
    def reset(self, word):
        self.tape = {i: char for i, char in enumerate(word)}  
        self.head_position = 0
        self.current_state = self.initial_state
    
    def step(self):
        current_symbol = self.tape.get(self.head_position, '_')  
        if self.current_state in self.transitions and current_symbol in self.transitions[self.current_state]:
            next_state, write_symbol, direction = self.transitions[self.current_state][current_symbol]
            self.tape[self.head_position] = write_symbol  
            self.head_position += 1 if direction == 'R' else -1  
            self.current_state = next_state  
        else:
            self.current_state = self.reject_state  
   
    def run(self, word):
        self.reset(word)
        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            self.step()
        
        final_tape = ''.join(self.tape.get(i, '_') for i in range(min(self.tape), max(self.tape) + 1))
        
        return self.current_state == self.accept_state, final_tape  
