document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const movieInput = document.getElementById('movie-input');
    const searchBtn = document.getElementById('search-btn');
    const errorMsg = document.getElementById('error-message');
    const resultsSection = document.getElementById('results-section');
    const matchedMovieLabel = document.getElementById('matched-movie');
    const moviesGrid = document.getElementById('movies-grid');

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const query = movieInput.value.trim();
        if (!query) return;

        // UI Loading State
        errorMsg.classList.add('hidden');
        searchBtn.textContent = 'Searching...';
        searchBtn.disabled = true;

        try {
            const response = await fetch('/recommend', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ movie: query })
            });

            const data = await response.json();

            if (!response.ok || data.error) {
                throw new Error(data.error || "Failed to fetch recommendations.");
            }

            renderRecommendations(data.matched_movie, data.recommendations);

        } catch (error) {
            errorMsg.textContent = error.message;
            errorMsg.classList.remove('hidden');
            resultsSection.classList.add('hidden');
        } finally {
            searchBtn.textContent = 'Find Matches';
            searchBtn.disabled = false;
        }
    });

    function renderRecommendations(matchedMovie, recommendations) {
        matchedMovieLabel.textContent = matchedMovie;
        moviesGrid.innerHTML = ''; // Clear previous results

        recommendations.forEach((movie, index) => {
            const card = document.createElement('div');
            card.className = 'movie-card';
            // Stagger animation delay slightly for each card
            card.style.animationDelay = `${index * 0.1}s`;

            card.innerHTML = `
                <div class="mc-rank">#${index + 1}</div>
                <div class="mc-title">${movie.title}</div>
                <div class="mc-genre">${movie.genre}</div>
            `;
            
            moviesGrid.appendChild(card);
        });

        resultsSection.classList.remove('hidden');
        
        // Smooth scroll to results
        setTimeout(() => {
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        }, 100);
    }
});
