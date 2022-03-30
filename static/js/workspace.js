var workspace_id = null;
var workspace_name_edit = null;
var workspace_link = null;
var delete_workspace = null;

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

window.addEventListener("load", () => {
    workspace_id = document.getElementById("workspace-id").innerHTML;
    workspace_name_edit = document.getElementById("workspace-name-edit");
    workspace_link = document.getElementById("workspace-link");
    delete_workspace = document.getElementById("delete-workspace");

    workspace_name_edit.addEventListener("keyup", () => {
        workspace_link.innerHTML = workspace_name_edit.value;
        save_workspace_name();
    });

    delete_workspace.addEventListener("click", () => remove());
});