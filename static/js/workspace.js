var workspace_id = null;
var workspace_name_edit = null;
var workspace_link = null;
var delete_workspace = null;
var header = null;
var color_picker_fore = null;
var color_picker_back = null;

function workspace_action(link) {
    fetch(link)
    .then(response => {
        return response.json();
    })
    .then(data => {
        message.innerHTML = `<span class='${data.status_color}'>${data.status}</span>`;
    });
}

function save_workspace_name() {
    let params = new URLSearchParams({name: workspace_name_edit.value});

    let link = "/workspace/" + workspace_id + "/name?" + params.toString();
    workspace_action(link);
}

function remove() {
    let link = "/workspace/" + workspace_id + "/delete";
    workspace_action(link);
    
    window.location.replace("/");
}

function change_color(forecolor, backcolor) {
    let params = new URLSearchParams({backcolor: backcolor, forecolor: forecolor});

    let link = "/workspace/" + workspace_id + "/color?" + params.toString();
    workspace_action(link);
}

window.addEventListener("load", () => {
    workspace_id = document.getElementById("workspace-id").innerHTML;
    workspace_name_edit = document.getElementById("workspace-name-edit");
    workspace_link = document.getElementById("workspace-link");
    delete_workspace = document.getElementById("delete-workspace");
    header = document.getElementById("header");

    color_picker_back = document.getElementById("color-picker-back");
    color_picker_fore = document.getElementById("color-picker-fore");

    workspace_name_edit.addEventListener("keyup", () => {
        workspace_link.innerHTML = workspace_name_edit.value;
        save_workspace_name();
    });

    delete_workspace.addEventListener("click", () => remove());
    
    color_picker_back.addEventListener("change", () => {
        header.style.backgroundColor = color_picker_back.value;
        change_color(color_picker_fore.value, color_picker_back.value);
    });
    color_picker_fore.addEventListener("change", () => {
        header.style.color = color_picker_fore.value;
        change_color(color_picker_fore.value, color_picker_back.value);
    });
});