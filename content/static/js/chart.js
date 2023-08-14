const addButtonLine = document.getElementById("add-form-line");
const delButtonLine = document.getElementById("del-form-line");
const addButtonScatter = document.getElementById("add-form-scatter");
const delButtonScatter = document.getElementById("del-form-scatter");
const addButtonBar = document.getElementById("add-form-bar");
const delButtonBar = document.getElementById("del-form-bar");
const formsetLineDiv = document.getElementById("formset-line-div");
const formsetLineButton = document.getElementById("formset-line-button");
const formsetScatterDiv = document.getElementById("formset-scatter-div");
const formsetScatterButton = document.getElementById("formset-scatter-button");
const formPieDiv = document.getElementById("form-pie-div");
const typeGraphique = document.getElementById("id_type_graphique");
const totalFormsLine = document.getElementById("id_form_line-TOTAL_FORMS");
const totalFormsScatter = document.getElementById("id_form_scatter-TOTAL_FORMS");
const totalFormsBar = document.getElementById("id_form_bar-TOTAL_FORMS");
const formsetBarDiv = document.getElementById("formset-bar-div");
const formsetBarButton = document.getElementById("formset-bar-button");
let formNumLine = parseFloat(totalFormsLine.value) || 1;
let formNumScatter = parseFloat(totalFormsScatter.value) || 1;
let formNumBar = parseFloat(totalFormsBar.value) || 1;




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

function hiddenFormScatter() {
    if (typeGraphique.value !== "scatter") {
        formsetScatterDiv.style.display = "none";
        formsetScatterButton.style.display = "none";
    } else {
        formsetScatterDiv.style.display = "block";
        formsetScatterButton.style.display = "block";
    }
}

function hiddenFormsetBar() {
    if (typeGraphique.value !== "bar") {
        formsetBarDiv.style.display = "none";
        formsetBarButton.style.display = "none";
    } else {
        formsetBarDiv.style.display = "block";
        formsetBarButton.style.display = "block";
    }
}


function addFormLine(e) {
    e.preventDefault();

    const newFormsetTitre = document.createElement("div");
    newFormsetTitre.classList.add("form-group");
    newFormsetTitre.innerHTML = `
                <label class="block mt-8 mb-2 text-sm font-medium text-gray-800 w-1/2">Titre de la courbe</label>
                <input type="text" name="form_line-${formNumLine}-titre" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_line-${formNumLine}-x_valeurs" value="">
            `;

    const newFormsetX = document.createElement("div");
    newFormsetX.classList.add("form-group");
    newFormsetX.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de x</label>
                <input type="text" name="form_line-${formNumLine}-x_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_line-${formNumLine}-x_valeurs" value="">
            `;

    const newFormsetY = document.createElement("div");
    newFormsetY.classList.add("form-group");
    newFormsetY.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de y</label>
                <input type="text" name="form_line-${formNumLine}-y_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_line-${formNumLine}-y_valeurs" value="">
            `;
    formNumLine++

    formsetLineDiv.appendChild(newFormsetTitre);
    formsetLineDiv.appendChild(newFormsetX);
    formsetLineDiv.appendChild(newFormsetY);

    totalFormsLine.setAttribute("value", formNumLine);
};

function delFormLine(e) {
    e.preventDefault();
    if (totalFormsLine.value > 1) {
        for (let i = 0; i < 3; i++) {
            const lastChild = formsetLineDiv.lastElementChild;
            if (lastChild) {
                formsetLineDiv.removeChild(lastChild);
            }
        }
        formNumLine -= 1;
        totalFormsLine.setAttribute("value", formNumLine);
    }
}

function addFormScatter(e) {
    e.preventDefault();

    const newFormsetTitre = document.createElement("div");
    newFormsetTitre.classList.add("form-group");
    newFormsetTitre.innerHTML = `
                <label class="block mt-8 mb-2 text-sm font-medium text-gray-800 w-1/2">Titre du nuage de points</label>
                <input type="text" name="form_scatter-${formNumScatter}-titre" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_scatter-${formNumScatter}-x_valeurs" value="">
            `;

    const newFormsetX = document.createElement("div");
    newFormsetX.classList.add("form-group");
    newFormsetX.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de x</label>
                <input type="text" name="form_scatter-${formNumScatter}-x_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_scatter-${formNumScatter}-x_valeurs" value="">
            `;

    const newFormsetY = document.createElement("div");
    newFormsetY.classList.add("form-group");
    newFormsetY.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs de y</label>
                <input type="text" name="form_scatter-${formNumScatter}-y_valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_scatter-${formNumScatter}-y_valeurs" value="">
            `;
    formNumScatter++

    formsetScatterDiv.appendChild(newFormsetTitre);
    formsetScatterDiv.appendChild(newFormsetX);
    formsetScatterDiv.appendChild(newFormsetY);

    totalFormsScatter.setAttribute("value", formNumScatter);
};

function delFormScatter(e) {
    e.preventDefault();
    if (totalFormsScatter.value > 1) {
        for (let i = 0; i < 3; i++) {
            const lastChild = formsetScatterDiv.lastElementChild;
            if (lastChild) {
                formsetScatterDiv.removeChild(lastChild);
            }
        }
        formNumScatter -= 1;
        totalFormsScatter.setAttribute("value", formNumScatter);
    }
}


function addFormBar(e) {
    e.preventDefault();

    const newFormsetNom = document.createElement("div");
    newFormsetNom.classList.add("form-group");
    newFormsetNom.innerHTML = `
                <label class="block mt-8 mb-2 text-sm font-medium text-gray-800 w-1/2">Nom de la colonne</label>
                <input type="text" name="form_bar-${formNumBar}-titre" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_bar-${formNumBar}-titre" value="">
            `;

    const newFormsetValeurs = document.createElement("div");
    newFormsetValeurs.classList.add("form-group");
    newFormsetValeurs.innerHTML = `
                <label class="block mb-2 text-sm font-medium text-gray-800 w-1/2">Valeurs</label>
                <input type="text" name="form_bar-${formNumBar}-valeurs" class="block w-full rounded border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 w-full" maxlength="100" id="id_form_bar-${formNumBar}-valeurs" value="">
            `;
    formNumBar++

    formsetBarDiv.appendChild(newFormsetNom);
    formsetBarDiv.appendChild(newFormsetValeurs);

    totalFormsBar.setAttribute("value", formNumBar);
};

function delFormBar(e) {
    e.preventDefault();
    if (totalFormsBar.value > 1) {
        for (let i = 0; i < 2; i++) {
            const lastChild = formsetBarDiv.lastElementChild;
            if (lastChild) {
                formsetBarDiv.removeChild(lastChild);
            }
        }
        formNumBar -= 1;
        totalFormsBar.setAttribute("value", formNumBar);
    }
}


hiddenFormsetLine()
hiddenFormPie()
hiddenFormScatter()
hiddenFormsetBar()

addButtonLine.addEventListener('click', addFormLine);
delButtonLine.addEventListener('click', delFormLine);
addButtonScatter.addEventListener('click', addFormScatter);
delButtonScatter.addEventListener('click', delFormScatter);
addButtonBar.addEventListener('click', addFormBar);
delButtonBar.addEventListener('click', delFormBar);

typeGraphique.addEventListener("change", hiddenFormsetLine);
typeGraphique.addEventListener("change", hiddenFormPie);
typeGraphique.addEventListener("change", hiddenFormScatter);
typeGraphique.addEventListener("change", hiddenFormsetBar);
