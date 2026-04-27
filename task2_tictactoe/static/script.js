const cells = document.querySelectorAll('.cell');
const statusText = document.getElementById('game-status');
const overlay = document.getElementById('overlay');
const endMessage = document.getElementById('end-message');
const resetBtn = document.getElementById('reset-btn');
const playAgainBtn = document.getElementById('play-again');
const playerX = document.getElementById('score-x');
const playerO = document.getElementById('score-o');

let board = ["", "", "", "", "", "", "", "", ""];
let isPlayerTurn = true;
let gameActive = true;

const winCombos = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
];

// Switch active UI glowing state
const setTurnUI = (isUser) => {
    if (isUser) {
        playerX.classList.add('active');
        playerO.classList.remove('active');
        statusText.textContent = "Your turn";
    } else {
        playerO.classList.add('active');
        playerX.classList.remove('active');
        statusText.textContent = "AI is thinking...";
    }
};

const handleWin = (winner) => {
    gameActive = false;
    let text = winner === 'Tie' ? "It's a Draw!" : winner === 'X' ? "You Won! (Impossible?!)" : "AI Wins!";
    if(winner === 'O') endMessage.style.color = "var(--accent-o)";
    else if(winner === 'X') endMessage.style.color = "var(--accent-x)";
    else endMessage.style.color = "var(--text-main)";

    endMessage.textContent = text;
    setTimeout(() => {
        overlay.classList.remove('hidden');
    }, 500);
};

const updateCell = (index, value) => {
    board[index] = value;
    cells[index].textContent = value;
    cells[index].classList.add(value.toLowerCase());
};

const aiMove = async () => {
    if (!gameActive) return;
    setTurnUI(false);

    try {
        const response = await fetch('/move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ board })
        });
        const data = await response.json();

        // Simulate slight delay for "thinking" 
        setTimeout(() => {
            if (data.status === 'success' || data.status === 'game_over') {
                if (data.move !== undefined && data.move !== -1) {
                    updateCell(data.move, 'O');
                }
                
                if (data.winner) {
                    handleWin(data.winner);
                } else {
                    isPlayerTurn = true;
                    setTurnUI(true);
                }
            }
        }, 400);

    } catch (err) {
        console.error("Failed to query AI", err);
        statusText.textContent = "Error connecting to AI";
    }
};

// Handle clicks
cells.forEach(cell => {
    cell.addEventListener('click', () => {
        const index = cell.getAttribute('data-index');

        if (board[index] !== "" || !isPlayerTurn || !gameActive) return;

        updateCell(index, 'X');
        isPlayerTurn = false;

        // Check if player won before sending to AI
        let playerWon = false;
        let emptySpots = 0;
        for (let combo of winCombos) {
            if (board[combo[0]] == 'X' && board[combo[1]] == 'X' && board[combo[2]] == 'X') {
                playerWon = true; break;
            }
        }
        board.forEach(c => c === "" && emptySpots++);

        if (playerWon) return handleWin('X');
        if (emptySpots === 0) return handleWin('Tie');

        aiMove();
    });
});

const restartGame = () => {
    board = ["", "", "", "", "", "", "", "", ""];
    gameActive = true;
    isPlayerTurn = true;
    cells.forEach(cell => {
        cell.textContent = "";
        cell.classList.remove('x', 'o');
    });
    overlay.classList.add('hidden');
    setTurnUI(true);
};

resetBtn.addEventListener('click', restartGame);
playAgainBtn.addEventListener('click', restartGame);
