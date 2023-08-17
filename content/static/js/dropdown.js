function showDropdown() {
    const dropdown = document.getElementById("dropdown");
    dropdown.classList.remove("hidden");
}

let hideTimer; // Variable pour stocker le délai

function hideDropdown() {
    const dropdown = document.getElementById("dropdown");
    const dropdownDefaultButton = document.getElementById("dropdownDefaultButton");

    // Utilisation d'un délai de 200 millisecondes avant de masquer le dropdown
    hideTimer = setTimeout(() => {
        dropdown.classList.add("hidden");
    }, 200);
}

function cancelHideDropdown() {
    clearTimeout(hideTimer);
}

function dropdown() {
    const dropdownDefaultButton = document.getElementById("dropdownDefaultButton");
    const dropdown = document.getElementById("dropdown");

    dropdownDefaultButton.addEventListener("mouseenter", showDropdown);
    dropdownDefaultButton.addEventListener("mouseleave", hideDropdown);
    dropdown.addEventListener("mouseenter", showDropdown);
    dropdown.addEventListener("mouseleave", hideDropdown);

    dropdown.addEventListener("mouseenter", cancelHideDropdown); // Annuler le délai si la souris entre dans le dropdown
}

document.addEventListener("DOMContentLoaded", dropdown);