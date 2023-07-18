const descriptionEl = document.getElementById('description');
const toggleBtnEl = document.getElementById('toggle-btn');
const hideBtnEl = document.getElementById('hide-btn');

const originalText = descriptionEl.textContent.trim();
const truncatedText = originalText.split('\n').slice(0, 3).join('\n');
descriptionEl.textContent = truncatedText;

toggleBtnEl.addEventListener('click', () => {
    descriptionEl.textContent = originalText;
    toggleBtnEl.classList.add('hidden');
    hideBtnEl.classList.remove('hidden');
});

hideBtnEl.addEventListener('click', () => {
    descriptionEl.textContent = truncatedText;
    toggleBtnEl.classList.remove('hidden');
    hideBtnEl.classList.add('hidden');
});