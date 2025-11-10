class TuringSimulator {
    constructor() {
        this.steps = [];
        this.currentStep = 0;
        this.isRunning = false;
        this.autoInterval = null;
        
        this.initializeElements();
        this.bindEvents();
    }
    
    initializeElements() {
        this.elements = {
            inputString: document.getElementById('input-string'),
            patternSelect: document.getElementById('pattern-select'),
            simulateBtn: document.getElementById('simulate-btn'),
            stepBtn: document.getElementById('step-btn'),
            autoBtn: document.getElementById('auto-btn'),
            resetBtn: document.getElementById('reset-btn'),
            machineDisplay: document.getElementById('machine-display'),
            tape: document.getElementById('tape'),
            head: document.getElementById('head'),
            currentState: document.getElementById('current-state'),
            stepCounter: document.getElementById('step-counter'),
            result: document.getElementById('result'),
            patternInfo: document.getElementById('pattern-info')
        };
    }
    
    bindEvents() {
        this.elements.simulateBtn.addEventListener('click', () => this.startSimulation());
        this.elements.stepBtn.addEventListener('click', () => this.nextStep());
        this.elements.autoBtn.addEventListener('click', () => this.toggleAuto());
        this.elements.resetBtn.addEventListener('click', () => this.reset());
        this.elements.patternSelect.addEventListener('change', () => this.updatePatternInfo());
        
        this.elements.inputString.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.startSimulation();
        });
    }
    
    async startSimulation() {
        const inputString = this.elements.inputString.value.trim();
        const pattern = this.elements.patternSelect.value;
        
        if (!inputString) {
            alert('Por favor ingresa una cadena de entrada');
            return;
        }
        
        this.setLoading(true);
        
        try {
            const response = await fetch('/simulate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input: inputString, pattern: pattern })
            });
            
            const data = await response.json();
            
            if (data.error) {
                alert(data.error);
                return;
            }
            
            this.steps = data.steps;
            this.currentStep = 0;
            this.accepted = data.accepted;
            
            this.showMachine();
            this.updateDisplay();
            this.enableControls();
            
        } catch (error) {
            alert('Error en la simulación: ' + error.message);
        } finally {
            this.setLoading(false);
        }
    }
    
    nextStep() {
        if (this.currentStep < this.steps.length - 1) {
            this.currentStep++;
            this.updateDisplay();
        }
        
        if (this.currentStep >= this.steps.length - 1) {
            this.showResult();
            this.elements.stepBtn.disabled = true;
            this.stopAuto();
        }
    }
    
    toggleAuto() {
        if (this.autoInterval) {
            this.stopAuto();
        } else {
            this.startAuto();
        }
    }
    
    startAuto() {
        this.autoInterval = setInterval(() => {
            if (this.currentStep < this.steps.length - 1) {
                this.nextStep();
            } else {
                this.stopAuto();
            }
        }, 800);
        
        this.elements.autoBtn.textContent = 'Pausar';
        this.elements.stepBtn.disabled = true;
    }
    
    stopAuto() {
        if (this.autoInterval) {
            clearInterval(this.autoInterval);
            this.autoInterval = null;
        }
        this.elements.autoBtn.textContent = 'Auto';
        this.elements.stepBtn.disabled = this.currentStep >= this.steps.length - 1;
    }
    
    updateDisplay() {
        const step = this.steps[this.currentStep];
        
        this.elements.currentState.textContent = step.current_state;
        this.elements.stepCounter.textContent = this.currentStep;
        
        this.renderTape(step.tape, step.head_position);
        this.updateHeadPosition(step.head_position);
        
        if (step.is_final) {
            this.elements.currentState.style.color = step.current_state === 'accept' ? 'var(--success)' : 'var(--error)';
        }
    }
    
    renderTape(tape, headPosition) {
        this.elements.tape.innerHTML = '';
        
        tape.forEach((symbol, index) => {
            const cell = document.createElement('div');
            cell.className = 'tape-cell';
            cell.textContent = symbol === '_' ? '∅' : symbol;
            
            if (symbol === '_') {
                cell.classList.add('blank');
            }
            
            if (index === headPosition) {
                cell.classList.add('active');
            }
            
            this.elements.tape.appendChild(cell);
        });
    }
    
    updateHeadPosition(position) {
        const cells = this.elements.tape.children;
        if (cells[position]) {
            const cellRect = cells[position].getBoundingClientRect();
            const tapeRect = this.elements.tape.getBoundingClientRect();
            const headPosition = cellRect.left - tapeRect.left + cellRect.width / 2 - 12;
            
            this.elements.head.style.left = `${headPosition}px`;
        }
    }
    
    showResult() {
        this.elements.result.style.display = 'block';
        this.elements.result.className = `result ${this.accepted ? 'accepted' : 'rejected'}`;
        this.elements.result.innerHTML = this.accepted 
            ? '✅ Cadena ACEPTADA' 
            : '❌ Cadena RECHAZADA';
    }
    
    showMachine() {
        this.elements.machineDisplay.style.display = 'block';
        this.elements.result.style.display = 'none';
    }
    
    enableControls() {
        this.elements.stepBtn.disabled = false;
        this.elements.autoBtn.disabled = false;
        this.elements.resetBtn.disabled = false;
    }
    
    reset() {
        this.stopAuto();
        this.currentStep = 0;
        this.steps = [];
        
        this.elements.machineDisplay.style.display = 'none';
        this.elements.stepBtn.disabled = true;
        this.elements.autoBtn.disabled = true;
        this.elements.resetBtn.disabled = true;
        this.elements.currentState.style.color = 'var(--mint-light)';
        
        this.elements.inputString.focus();
    }
    
    setLoading(loading) {
        this.elements.simulateBtn.disabled = loading;
        this.elements.simulateBtn.textContent = loading ? 'Simulando...' : 'Simular';
        
        if (loading) {
            this.elements.simulateBtn.classList.add('processing');
        } else {
            this.elements.simulateBtn.classList.remove('processing');
        }
    }
    
    updatePatternInfo() {
        const selectedOption = this.elements.patternSelect.selectedOptions[0];
        const text = selectedOption.textContent;
        this.elements.patternInfo.innerHTML = `
            <p><strong>Patrón seleccionado:</strong> ${text}</p>
            <p>Esta expresión regular define las reglas que debe seguir la cadena de entrada para ser aceptada.</p>
        `;
    }
}

// Inicializar la aplicación
document.addEventListener('DOMContentLoaded', () => {
    new TuringSimulator();
});