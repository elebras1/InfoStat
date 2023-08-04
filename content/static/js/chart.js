const addButton = document.getElementById("add-form");
const delButton = document.getElementById("del-form");
const formsetDiv = document.getElementById("formset-div");
const totalForms = document.getElementById("id_form-TOTAL_FORMS");
let formNum = formsetDiv.children.length / 3;

addButton.addEventListener('click', addForm);
delButton.addEventListener('click', delForm);

function addForm(e) {
    e.preventDefault();

    const newFormsetTitre = document.createElement("div");
    newFormsetTitre.classList.add("form-group");
    newFormsetTitre.innerHTML = `
                <label class="block mt-8 mb-2 text-sm font-medium text-gray-800 w-1/2">Titre de la courbe</label>
                <input type="text" name="form-${formNum}-titre" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form-${formNum}-x_valeurs" value="">
            `;

    const newFormsetX = document.createElement("div");
    newFormsetX.classList.add("form-group");
    newFormsetX.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de x</label>
                <input type="text" name="form-${formNum}-x_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form-${formNum}-x_valeurs" value="">
            `;

    const newFormsetY = document.createElement("div");
    newFormsetY.classList.add("form-group");
    newFormsetY.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de y</label>
                <input type="text" name="form-${formNum}-y_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form-${formNum}-y_valeurs" value="">
            `;
    formNum++

    formsetDiv.appendChild(newFormsetTitre);
    formsetDiv.appendChild(newFormsetX);
    formsetDiv.appendChild(newFormsetY);

    totalForms.setAttribute("value", formNum);
};

function delForm(e) {
    e.preventDefault();
    if (totalForms.value > 1) {
        for (let i = 0; i < 3; i++) {
            formsetDiv.removeChild(formsetDiv.lastChild);
        }
        formNum -= 1;
        totalForms.setAttribute("value", formNum);
    }
}