var workspace_id = null;
var document_id = null;
var document_name_edit = null;

var text = "";
var editor = null;
var preview = null;
var message = null;
var preview_container = null;
var download_link = null;
var markdowned = false;
var save_buttons = [];
var delete_buttons = [];
var i;

function document_action(link) {
    fetch(link)
    .then(response => {
        return response.json();
    })
    .then(data => {
        message.innerHTML = `<span class='${data.status_color}'>${data.status}</span>`;
    });
}

//Save text as .md file
function save_md() {
    let blob = new Blob([text], {type: "text/plain;charset=utf-8"});
    download_link.href = URL.createObjectURL(blob);
    download_link.download = "document.md";
    download_link.click();
}

function save() {
    let params = new URLSearchParams({text: text});

    let link = "/workspace/" + workspace_id + "/document/" + document_id + "/save?" + params.toString();
    document_action(link);
}

function remove() {
    let link = "/workspace/" + workspace_id + "/document/" + document_id + "/delete";
    document_action(link);

    window.location.replace("/workspace/" + workspace_id);
}

function change_markdown() {
    if (markdowned) {
        editor.style.display = "block";
        preview_container.style.display = "none";
        preview.innerHTML = "Preview";
        markdowned = false;
        message.innerHTML = "<span class='text-info'>Markdown is disabled</span>";
    } 
    else {
        editor.style.display = "none";
        preview_container.innerHTML = marked.parse(text);
        preview_container.style.display = "block";
        preview.innerHTML = "Text";
        markdowned = true;
        message.innerHTML = "<span class='text-info'>Markdown is enabled</span>";
    }
}

function change_markdown_handle(e) {
    if (e.ctrlKey && e.keyCode == 83) {
        //Make on Ctrl+S press
        e.preventDefault();
        save_md();
    }
    else if (e.ctrlKey && e.keyCode == 77) {
        //Make on Ctrl+M press
        e.preventDefault();
        change_markdown();
    }
}

function change_text() {
    text = editor.value;
    preview_container.innerHTML = marked.parse(text);
    save();
}

function save_document_name() {
    let params = new URLSearchParams({name: document_name_edit.value});

    let link = "/workspace/" + workspace_id + "/document/" + document_id + "/name?" + params.toString();
    document_action(link);
}

//Get text from d-text id on window load
window.addEventListener("load", () => {
    text = document.getElementById("d-text").innerHTML;
    editor = document.getElementById("editor");
    editor.innerHTML = text;
    preview = document.getElementById("preview");
    message = document.getElementById("message");
    message.innerHTML = "<span class='text-info'>Status</span>";
    preview_container = document.getElementById("preview-container");
    preview_container.style.display = "none";
    workspace_id = document.getElementById("workspace-id").innerHTML;
    document_id = document.getElementById("document-id").innerHTML;
    document_name_edit = document.getElementById("document-name-edit");
    download_link = document.getElementById("download-link");

    save_buttons = document.getElementsByClassName("save-button");
    delete_buttons = document.getElementsByClassName("delete-button");

    console.log('loaded');

    window.addEventListener("keydown", e => change_markdown_handle(e));
    preview.addEventListener("click", e => change_markdown(e));
    document_name_edit.addEventListener("keyup", () => save_document_name())
    editor.addEventListener("input", () => change_text());
    editor.addEventListener("keydown", function(e) {
        if (e.key == 'Tab') {
          e.preventDefault();
          var start = this.selectionStart;
          var end = this.selectionEnd;
      
          // set textarea value to: text before caret + tab + text after caret
          this.value = this.value.substring(0, start) + "\t" + this.value.substring(end);
      
          // put caret at right position again
          this.selectionStart = this.selectionEnd = start + 1;
        }
    });

    //Save buttons on click save
    for (i = 0; i < save_buttons.length; i++) {
        save_buttons[i].addEventListener("click", () => save_md());
    }
    //Delete buttons on click delete
    for (i = 0; i < delete_buttons.length; i++) {
        delete_buttons[i].addEventListener("click", () => remove());
    }
});