function addchild(element) {
    
}

document.addEventListener('DOMContentLoaded', (event) => {

    editor = true;
    if (editor) {
        

        var elements = document.getElementsByClassName("editable");
        console.log(elements);

        for (var i = 0; i < elements.length; i++){
            var removebutton = document.createElement("div");
            removebutton.style.position = "relative";
            removebutton.style.top = "0";
            removebutton.style.right = "0";
            removebutton.style.width = "12px";
            removebutton.style.height = "12px"
            removebutton.style.float = "right";
            removebutton.innerHTML = "-";
            elements[i].appendChild(removebutton);
            
            var addbutton = document.createElement("div");
            addbutton.style.position = "relative";
            addbutton.style.top = "0";
            addbutton.style.right = "0";
            addbutton.style.width = "12px";
            addbutton.style.height = "12px"
            addbutton.style.float = "right";
            addbutton.innerHTML = "+";
            elements[i].appendChild(addbutton);

            var settingsbutton = document.createElement("div");
            settingsbutton.style.position = "relative";
            settingsbutton.style.top = "0";
            settingsbutton.style.right = "0";
            settingsbutton.style.width = "12px";
            settingsbutton.style.height = "12px"
            settingsbutton.style.float = "right";
            settingsbutton.innerHTML = "S";
            elements[i].appendChild(settingsbutton);
        }
    }
})