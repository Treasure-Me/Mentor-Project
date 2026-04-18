// Matrix Multiplier Mayhem - Production Game Logic
class MatrixGame {
    constructor() {
        this.currentLevel = 0;
        this.selectedMatrix = null;
        this.placedMatrices = [];
        this.init();
    }

    init() {
        this.setupEventListeners();
        // If we are on the game board, initialize the UI data
        if (document.getElementById('input-matrix-data')) {
            this.renderInitialMatrices();
            this.generateMatrixPalette();
        }
    }

    setupEventListeners() {
        // Drag and drop events
        document.addEventListener('dragstart', this.handleDragStart.bind(this));
        document.addEventListener('dragover', this.handleDragOver.bind(this));
        document.addEventListener('drop', this.handleDrop.bind(this));

        // Button events (Using optional chaining in case elements don't exist on all pages)
        document.getElementById('verify-btn')?.addEventListener('click', this.verifySolution.bind(this));
        document.getElementById('hint-btn')?.addEventListener('click', this.getHint.bind(this));
        document.getElementById('reset-btn')?.addEventListener('click', () => location.reload());
    }

    renderInitialMatrices() {
        // Parse data embedded in the HTML by Jinja
        const inputData = JSON.parse(document.getElementById('input-matrix-data').textContent);
        const targetData = JSON.parse(document.getElementById('target-matrix-data').textContent);

        const inputContainer = document.getElementById('input-matrix-render');
        const targetContainer = document.getElementById('target-matrix-render');

        inputContainer.appendChild(this.createMatrixVisual(inputData));
        targetContainer.appendChild(this.createMatrixVisual(targetData));
    }

    handleDragStart(e) {
        if (e.target.closest('.draggable-matrix')) {
            const el = e.target.closest('.draggable-matrix');
            this.selectedMatrix = JSON.parse(el.dataset.matrix);
            e.dataTransfer.setData('text/plain', el.id);
            e.dataTransfer.effectAllowed = 'copy';
        }
    }

    handleDragOver(e) {
        e.preventDefault();
        const slot = e.target.closest('.matrix-slot');
        if (slot) {
            slot.classList.add('drag-over');
            e.dataTransfer.dropEffect = 'copy';
        }
    }

    handleDrop(e) {
        e.preventDefault();
        const slot = e.target.closest('.matrix-slot');
        
        if (slot) {
            slot.classList.remove('drag-over');
            
            if (this.selectedMatrix) {
                // Clear previous content
                slot.innerHTML = '';
                slot.classList.add('filled');
                
                // Render the new matrix
                const matrixVisual = this.createMatrixVisual(this.selectedMatrix);
                slot.appendChild(matrixVisual);
                
                // Store state (Handling single slot for now, but structured for multiple)
                this.placedMatrices = [this.selectedMatrix];
                this.hideFeedback();
            }
        }
    }

    createMatrixVisual(matrix) {
        const container = document.createElement('div');
        container.className = 'matrix-visual';
        
        // Use CSS Grid dynamically based on columns
        const cols = matrix[0].length;
        container.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
        
        matrix.forEach(row => {
            row.forEach(val => {
                const cell = document.createElement('div');
                cell.className = 'matrix-cell';
                cell.textContent = val;
                container.appendChild(cell);
            });
        });
        
        return container;
    }

    generateMatrixPalette() {
        const palette = document.getElementById('matrix-palette');
        if (!palette) return;
        
        palette.innerHTML = '';

        // Standard palette. In a full production app, this could come from an API
        const sampleMatrices = [
            [[1, 0], [0, 1]],  
            [[2, 0], [0, 2]],  
            [[0, 1], [1, 0]],  
            [[-1, 0], [0, 1]], 
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]] 
        ];

        sampleMatrices.forEach((matrix, index) => {
            const matrixElement = document.createElement('div');
            matrixElement.className = 'draggable-matrix';
            matrixElement.id = `palette-matrix-${index}`;
            matrixElement.draggable = true;
            matrixElement.dataset.matrix = JSON.stringify(matrix);
            
            matrixElement.appendChild(this.createMatrixVisual(matrix));
            palette.appendChild(matrixElement);
        });
    }

    async verifySolution() {
        if (this.placedMatrices.length === 0) {
            this.showFeedback('warning', 'Please drag a matrix into the transformation slot first!');
            return;
        }

        const originalBtnText = document.getElementById('verify-btn').textContent;
        document.getElementById('verify-btn').textContent = 'Verifying...';

        try {
            const response = await fetch('/check_solution', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ matrices: this.placedMatrices })
            });
            
            const result = await response.json();
            
            if (result.correct) {
                this.showFeedback('correct', 'Matrix Matched! Excellent work.');
                document.getElementById('next-level-btn').style.display = 'inline-flex';
            } else {
                this.showFeedback('false', result.message || 'Incorrect transformation. Try again!');
            }
        } catch (error) {
            console.error('API Error:', error);
            this.showFeedback('false', 'Server error checking solution.');
        } finally {
            document.getElementById('verify-btn').textContent = originalBtnText;
        }
    }

    async getHint() {
        try {
            const response = await fetch('/hint');
            const data = await response.json();
            this.showFeedback('hint', data.hint);
        } catch (error) {
            this.showFeedback('hint', 'Think about how row and column dimensions align.');
        }
    }

    showFeedback(type, message) {
        const feedback = document.getElementById('feedback');
        feedback.textContent = message;
        // Reset classes
        feedback.className = 'feedback';
        feedback.classList.add(`feedback-${type}`);
        feedback.style.display = 'block';
    }

    hideFeedback() {
        const feedback = document.getElementById('feedback');
        if (feedback) feedback.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.matrixGame = new MatrixGame();
});