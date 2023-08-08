const addButton = document.getElementById("add-form");
const delButton = document.getElementById("del-form");
const formsetLineDiv = document.getElementById("formset-line-div");
const formsetLineButton = document.getElementById("formset-line-button");
const formPieDiv = document.getElementById("form-pie-div");
const typeGraphique = document.getElementById("id_type_graphique");
const totalForms = document.getElementById("id_form_line-TOTAL_FORMS");
let formNum = formsetLineDiv.children.length / 3;


function hiddenFormsetLine() {
    if (typeGraphique.value !== "line") {
        formsetLineDiv.style.display = "none";
        formsetLineButton.style.display = "none";
    } else {
        formsetLineDiv.style.display = "block";
        formsetLineButton.style.display = "block";
    }
}

function hiddenFormPie() {
    if (typeGraphique.value !== "pie") {
        formPieDiv.style.display = "none";
    } else {
        formPieDiv.style.display = "block";
    }
}

function addForm(e) {
    e.preventDefault();

    const newFormsetTitre = document.createElement("div");
    newFormsetTitre.classList.add("form-group");
    newFormsetTitre.innerHTML = `
                <label class="block mt-8 mb-2 text-sm font-medium text-gray-800 w-1/2">Titre de la courbe</label>
                <input type="text" name="form_line-${formNum}-titre" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form-${formNum}-x_valeurs" value="">
            `;

    const newFormsetX = document.createElement("div");
    newFormsetX.classList.add("form-group");
    newFormsetX.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de x</label>
                <input type="text" name="form_line-${formNum}-x_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form-${formNum}-x_valeurs" value="">
            `;

    const newFormsetY = document.createElement("div");
    newFormsetY.classList.add("form-group");
    newFormsetY.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de y</label>
                <input type="text" name="form_line-${formNum}-y_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form-${formNum}-y_valeurs" value="">
            `;
    formNum++

    formsetLineDiv.appendChild(newFormsetTitre);
    formsetLineDiv.appendChild(newFormsetX);
    formsetLineDiv.appendChild(newFormsetY);

    totalForms.setAttribute("value", formNum);
};

function delForm(e) {
    e.preventDefault();
    if (totalForms.value > 1) {
        for (let i = 0; i < 3; i++) {
            formsetLineDiv.removeChild(formsetLineDiv.lastChild);
        }
        formNum -= 1;
        totalForms.setAttribute("value", formNum);
    }
}
hiddenFormsetLine()
hiddenFormPie()
addButton.addEventListener('click', addForm);
delButton.addEventListener('click', delForm);
typeGraphique.addEventListener("change", hiddenFormsetLine);
typeGraphique.addEventListener("change", hiddenFormPie);