/*
============================================
DEX JAVASCRIPT
Advanced Pokedex with Team Builder, Favorites, Dark Mode
============================================
*/

// ============================================
// GLOBAL STATE
// ============================================

let currentPokemon = null;
let isShinyMode = false;
let myTeam = loadFromLocalStorage('pokemon_team') || [];
let favorites = loadFromLocalStorage('pokemon_favorites') || [];

// ============================================
// DOM ELEMENTS
// ============================================

// Search elements
const searchInput = document.getElementById('pokemon-search');
const searchBtn = document.getElementById('search-btn');
const randomBtn = document.getElementById('random-btn');
const loadingSpinner = document.getElementById('loading-spinner');
const pokemonDisplay = document.getElementById('pokemon-display');
const errorMessage = document.getElementById('error-message');

// Pokemon data elements
const pokemonName = document.getElementById('pokemon-name');
const pokemonId = document.getElementById('pokemon-id');
const pokemonSprite = document.getElementById('pokemon-sprite');
const pokemonType = document.getElementById('pokemon-type');
const pokemonHeight = document.getElementById('pokemon-height');
const pokemonWeight = document.getElementById('pokemon-weight');
const pokemonGeneration = document.getElementById('pokemon-generation');
const pokemonHabitat = document.getElementById('pokemon-habitat');
const pokemonGender = document.getElementById('pokemon-gender');
const pokemonCapture = document.getElementById('pokemon-capture');
const pokemonAbilities = document.getElementById('pokemon-abilities');
const pokemonStats = document.getElementById('pokemon-stats');
const statTotalValue = document.getElementById('stat-total-value');
const pokemonDescription = document.getElementById('pokemon-description');
const evolutionChain = document.getElementById('evolution-chain');
const pokemonMoves = document.getElementById('pokemon-moves');

// Type effectiveness elements
const weakTo = document.getElementById('weak-to');
const resistantTo = document.getElementById('resistant-to');
const immuneTo = document.getElementById('immune-to');

// Action buttons
const addToTeamBtn = document.getElementById('add-to-team-btn');
const toggleFavoriteBtn = document.getElementById('toggle-favorite-btn');
const toggleShinyBtn = document.getElementById('toggle-shiny-btn');

// Team sidebar elements
const teamSidebar = document.getElementById('team-sidebar');
const teamToggleBtn = document.getElementById('team-toggle-btn');
const closeSidebarBtn = document.getElementById('close-sidebar');
const teamCount = document.getElementById('team-count');
const teamSlots = document.getElementById('team-slots');
const clearTeamBtn = document.getElementById('clear-team-btn');

// Favorites elements
const favoritesBtn = document.getElementById('favorites-btn');
const favoritesCount = document.getElementById('favorites-count');

// Dark mode toggle
const darkModeToggle = document.getElementById('dark-mode-toggle');

// Toast notification
const toast = document.getElementById('toast');
const toastMessage = document.getElementById('toast-message');


// ============================================
// LOCALSTORAGE HELPERS
// ============================================

function saveToLocalStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
    } catch (e) {
        console.error('Error saving to localStorage:', e);
    }
}

function loadFromLocalStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.error('Error loading from localStorage:', e);
        return null;
    }
}


// ============================================
// TOAST NOTIFICATION
// ============================================

function showToast(message) {
    toastMessage.textContent = message;
    toast.classList.remove('hidden');

    setTimeout(() => {
        toast.classList.add('hidden');
    }, 3000);
}


// ============================================
// DARK MODE
// ============================================

function initDarkMode() {
    const darkMode = loadFromLocalStorage('dark_mode');
    if (darkMode) {
        document.body.classList.add('dark-mode');
        darkModeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }
}

darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    saveToLocalStorage('dark_mode', isDarkMode);

    // Update icon
    darkModeToggle.innerHTML = isDarkMode
        ? '<i class="fas fa-sun"></i>'
        : '<i class="fas fa-moon"></i>';

    showToast(isDarkMode ? 'Dark mode enabled' : 'Light mode enabled');
});


// ============================================
// EVENT LISTENERS
// ============================================

// Search button click
searchBtn.addEventListener('click', () => {
    const query = searchInput.value.trim();
    if (query) {
        searchPokemon(query);
    } else {
        showError('Please enter a Pokemon name or ID');
    }
});

// Enter key in search input
searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        searchBtn.click();
    }
});

// Random button click
randomBtn.addEventListener('click', () => {
    fetchRandomPokemon();
});

// Add to team button
addToTeamBtn.addEventListener('click', () => {
    if (currentPokemon) {
        addToTeam(currentPokemon);
    }
});

// Toggle favorite button
toggleFavoriteBtn.addEventListener('click', () => {
    if (currentPokemon) {
        toggleFavorite(currentPokemon);
    }
});

// Toggle shiny button
toggleShinyBtn.addEventListener('click', () => {
    if (currentPokemon) {
        toggleShiny();
    }
});

// Team sidebar toggle
teamToggleBtn.addEventListener('click', () => {
    teamSidebar.classList.toggle('active');
});

closeSidebarBtn.addEventListener('click', () => {
    teamSidebar.classList.remove('active');
});

// Clear team button
clearTeamBtn.addEventListener('click', () => {
    if (confirm('Are you sure you want to clear your entire team?')) {
        myTeam = [];
        saveToLocalStorage('pokemon_team', myTeam);
        updateTeamDisplay();
        showToast('Team cleared');
    }
});


// ============================================
// API FUNCTIONS
// ============================================

async function searchPokemon(identifier) {
    showLoading();
    hideError();
    isShinyMode = false; // Reset shiny mode

    try {
        const response = await fetch(`/api/pokemon/${identifier}`);
        const result = await response.json();

        if (result.success) {
            currentPokemon = result.data;
            displayPokemon(result.data);
        } else {
            showError(result.error || 'Pokemon not found');
            hideLoading();
        }
    } catch (error) {
        console.error('Error fetching Pokemon:', error);
        showError('Failed to fetch Pokemon data. Please try again.');
        hideLoading();
    }
}

async function fetchRandomPokemon() {
    showLoading();
    hideError();
    isShinyMode = false; // Reset shiny mode

    try {
        const response = await fetch('/api/random');
        const result = await response.json();

        if (result.success) {
            currentPokemon = result.data;
            displayPokemon(result.data);
            searchInput.value = result.data.name;
        } else {
            showError('Failed to fetch random Pokemon');
            hideLoading();
        }
    } catch (error) {
        console.error('Error fetching random Pokemon:', error);
        showError('Failed to fetch random Pokemon. Please try again.');
        hideLoading();
    }
}


// ============================================
// DISPLAY FUNCTIONS
// ============================================

function displayPokemon(data) {
    // Update basic info
    pokemonName.textContent = data.name;
    pokemonId.textContent = `#${String(data.id).padStart(3, '0')}`;
    pokemonSprite.src = isShinyMode ? data.sprite_shiny : data.sprite;
    pokemonSprite.alt = `${data.name} sprite`;

    // Update additional info
    pokemonHeight.textContent = data.height;
    pokemonWeight.textContent = data.weight;
    pokemonGeneration.textContent = data.generation;
    pokemonHabitat.textContent = data.habitat;
    pokemonGender.textContent = data.gender_ratio;
    pokemonCapture.textContent = data.capture_rate;

    // Update description
    pokemonDescription.textContent = data.description;

    // Update types
    displayTypes(data.types);

    // Update abilities
    displayAbilities(data.abilities);

    // Update stats
    displayStats(data.stats);

    // Update type effectiveness
    displayTypeEffectiveness(data.type_effectiveness);

    // Update moves
    displayMoves(data.moves);

    // Update evolution chain
    displayEvolutionChain(data.evolution_chain);

    // Update favorite button state
    updateFavoriteButton(data.id);

    // Hide loading, show Pokemon display
    hideLoading();
    pokemonDisplay.classList.remove('hidden');
}

function displayTypes(types) {
    pokemonType.innerHTML = '';
    const typeArray = types.split('/');
    typeArray.forEach(type => {
        const badge = document.createElement('span');
        badge.className = `type-badge type-${type.toLowerCase()}`;
        badge.textContent = type;
        pokemonType.appendChild(badge);
    });
}

function displayAbilities(abilities) {
    pokemonAbilities.innerHTML = '';
    abilities.forEach(ability => {
        const badge = document.createElement('span');
        badge.className = 'ability-badge';
        badge.textContent = ability;
        pokemonAbilities.appendChild(badge);
    });
}

function displayStats(stats) {
    pokemonStats.innerHTML = '';
    let total = 0;

    stats.forEach(stat => {
        total += stat.value;

        const statContainer = document.createElement('div');
        statContainer.className = 'stat-bar-container';

        const statName = document.createElement('span');
        statName.className = 'stat-name';
        statName.textContent = stat.name;

        const statBarBg = document.createElement('div');
        statBarBg.className = 'stat-bar-bg';

        const statBarFill = document.createElement('div');
        statBarFill.className = 'stat-bar-fill';

        const percentage = Math.min((stat.value / 255) * 100, 100);
        setTimeout(() => {
            statBarFill.style.width = `${percentage}%`;
        }, 100);

        const statValue = document.createElement('span');
        statValue.className = 'stat-value-text';
        statValue.textContent = stat.value;

        statBarBg.appendChild(statBarFill);
        statContainer.appendChild(statName);
        statContainer.appendChild(statBarBg);
        statContainer.appendChild(statValue);
        pokemonStats.appendChild(statContainer);
    });

    statTotalValue.textContent = total;
}

function displayTypeEffectiveness(effectiveness) {
    // Weak to
    weakTo.innerHTML = '';
    if (effectiveness.weak_to.length === 0) {
        weakTo.textContent = 'None';
        weakTo.style.color = '#9ca3af';
    } else {
        effectiveness.weak_to.forEach(type => {
            const badge = document.createElement('span');
            badge.className = `type-badge effectiveness-badge type-${type}`;
            badge.textContent = type;
            weakTo.appendChild(badge);
        });
    }

    // Resistant to
    resistantTo.innerHTML = '';
    if (effectiveness.resistant_to.length === 0) {
        resistantTo.textContent = 'None';
        resistantTo.style.color = '#9ca3af';
    } else {
        effectiveness.resistant_to.forEach(type => {
            const badge = document.createElement('span');
            badge.className = `type-badge effectiveness-badge type-${type}`;
            badge.textContent = type;
            resistantTo.appendChild(badge);
        });
    }

    // Immune to
    immuneTo.innerHTML = '';
    if (effectiveness.immune_to.length === 0) {
        immuneTo.textContent = 'None';
        immuneTo.style.color = '#9ca3af';
    } else {
        effectiveness.immune_to.forEach(type => {
            const badge = document.createElement('span');
            badge.className = `type-badge effectiveness-badge type-${type}`;
            badge.textContent = type;
            immuneTo.appendChild(badge);
        });
    }
}

function displayMoves(moves) {
    pokemonMoves.innerHTML = '';

    if (moves.length === 0) {
        pokemonMoves.textContent = 'No moves data available';
        return;
    }

    moves.forEach(move => {
        const moveItem = document.createElement('div');
        moveItem.className = 'move-item';

        const moveName = document.createElement('div');
        moveName.className = 'move-name';
        moveName.textContent = move.name;

        const moveLevel = document.createElement('div');
        moveLevel.className = 'move-level';
        moveLevel.textContent = move.level === 0 ? 'Start' : `Level ${move.level}`;

        moveItem.appendChild(moveName);
        moveItem.appendChild(moveLevel);
        pokemonMoves.appendChild(moveItem);
    });
}

function displayEvolutionChain(evolutions) {
    evolutionChain.innerHTML = '';

    if (evolutions.length === 0) {
        evolutionChain.textContent = 'No evolution data available';
        return;
    }

    evolutions.forEach((evo, index) => {
        const evoStage = document.createElement('div');
        evoStage.className = 'evolution-stage';
        evoStage.onclick = () => searchPokemon(evo.name.toLowerCase());

        const evoSprite = document.createElement('img');
        evoSprite.src = evo.sprite;
        evoSprite.alt = evo.name;
        evoSprite.className = 'evolution-sprite';

        const evoName = document.createElement('span');
        evoName.className = 'evolution-name';
        evoName.textContent = evo.name;

        evoStage.appendChild(evoSprite);
        evoStage.appendChild(evoName);

        if (evo.method) {
            const evoMethod = document.createElement('span');
            evoMethod.className = 'evolution-method';
            evoMethod.textContent = evo.method;
            evoStage.appendChild(evoMethod);
        }

        evolutionChain.appendChild(evoStage);

        if (index < evolutions.length - 1) {
            const arrow = document.createElement('span');
            arrow.className = 'evolution-arrow';
            arrow.textContent = '→';
            evolutionChain.appendChild(arrow);
        }
    });
}


// ============================================
// TEAM BUILDER
// ============================================

function addToTeam(pokemon) {
    if (myTeam.length >= 6) {
        showToast('Team is full! (Max 6 Pokemon)');
        return;
    }

    // Check if already in team
    if (myTeam.some(p => p.id === pokemon.id)) {
        showToast(`${pokemon.name} is already in your team!`);
        return;
    }

    myTeam.push({
        id: pokemon.id,
        name: pokemon.name,
        sprite: pokemon.sprite,
        types: pokemon.types
    });

    saveToLocalStorage('pokemon_team', myTeam);
    updateTeamDisplay();
    showToast(`${pokemon.name} added to team!`);
}

function removeFromTeam(pokemonId) {
    myTeam = myTeam.filter(p => p.id !== pokemonId);
    saveToLocalStorage('pokemon_team', myTeam);
    updateTeamDisplay();
    showToast('Pokemon removed from team');
}

function updateTeamDisplay() {
    teamCount.textContent = myTeam.length;
    teamSlots.innerHTML = '';

    // Create 6 slots
    for (let i = 0; i < 6; i++) {
        const slot = document.createElement('div');
        slot.className = 'team-slot';

        if (myTeam[i]) {
            const pokemon = myTeam[i];
            slot.classList.add('filled');

            const sprite = document.createElement('img');
            sprite.src = pokemon.sprite;
            sprite.className = 'team-slot-sprite';

            const info = document.createElement('div');
            info.className = 'team-slot-info';

            const name = document.createElement('h4');
            name.textContent = pokemon.name;

            const types = document.createElement('div');
            types.className = 'team-slot-types';
            pokemon.types.split('/').forEach(type => {
                const badge = document.createElement('span');
                badge.className = `type-badge type-${type.toLowerCase()}`;
                badge.textContent = type;
                badge.style.fontSize = '0.7rem';
                badge.style.padding = '4px 8px';
                types.appendChild(badge);
            });

            info.appendChild(name);
            info.appendChild(types);

            const removeBtn = document.createElement('button');
            removeBtn.className = 'team-slot-remove';
            removeBtn.innerHTML = '<i class="fas fa-times"></i>';
            removeBtn.onclick = (e) => {
                e.stopPropagation();
                removeFromTeam(pokemon.id);
            };

            slot.appendChild(sprite);
            slot.appendChild(info);
            slot.appendChild(removeBtn);

            // Click to view Pokemon
            slot.style.cursor = 'pointer';
            slot.onclick = () => {
                searchPokemon(pokemon.name.toLowerCase());
                teamSidebar.classList.remove('active');
            };
        } else {
            slot.innerHTML = `<i class="fas fa-plus" style="font-size: 2rem; color: #9ca3af;"></i>`;
        }

        teamSlots.appendChild(slot);
    }
}


// ============================================
// FAVORITES SYSTEM
// ============================================

function toggleFavorite(pokemon) {
    const index = favorites.findIndex(f => f.id === pokemon.id);

    if (index > -1) {
        favorites.splice(index, 1);
        showToast(`${pokemon.name} removed from favorites`);
    } else {
        favorites.push({
            id: pokemon.id,
            name: pokemon.name,
            sprite: pokemon.sprite,
            types: pokemon.types
        });
        showToast(`${pokemon.name} added to favorites!`);
    }

    saveToLocalStorage('pokemon_favorites', favorites);
    updateFavoriteButton(pokemon.id);
    updateFavoritesCount();
}

function updateFavoriteButton(pokemonId) {
    const isFavorite = favorites.some(f => f.id === pokemonId);

    if (isFavorite) {
        toggleFavoriteBtn.innerHTML = '<i class="fas fa-star"></i> Favorited';
        toggleFavoriteBtn.classList.add('favorited');
    } else {
        toggleFavoriteBtn.innerHTML = '<i class="far fa-star"></i> Favorite';
        toggleFavoriteBtn.classList.remove('favorited');
    }
}

function updateFavoritesCount() {
    favoritesCount.textContent = favorites.length;
}


// ============================================
// SHINY TOGGLE
// ============================================

function toggleShiny() {
    if (!currentPokemon) return;

    isShinyMode = !isShinyMode;

    pokemonSprite.src = isShinyMode ? currentPokemon.sprite_shiny : currentPokemon.sprite;

    toggleShinyBtn.innerHTML = isShinyMode
        ? '<i class="fas fa-sparkles"></i> Normal Form'
        : '<i class="fas fa-sparkles"></i> Shiny Form';

    showToast(isShinyMode ? 'Shiny mode ON ✨' : 'Shiny mode OFF');
}


// ============================================
// UI STATE FUNCTIONS
// ============================================

function showLoading() {
    loadingSpinner.classList.remove('hidden');
    pokemonDisplay.classList.add('hidden');
}

function hideLoading() {
    loadingSpinner.classList.add('hidden');
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
}

function hideError() {
    errorMessage.classList.add('hidden');
}


// ============================================
// INITIALIZATION
// ============================================

window.addEventListener('DOMContentLoaded', () => {
    // Initialize dark mode
    initDarkMode();

    // Update team and favorites displays
    updateTeamDisplay();
    updateFavoritesCount();

    // Load default Pokemon (Pikachu)
    searchInput.value = 'pikachu';
    searchPokemon('pikachu');
});
