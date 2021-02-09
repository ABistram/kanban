function addchild(e) {
    
}

function removechild(e){
    
}

document.addEventListener('DOMContentLoaded', (event) => {

    

    editor = true;
    if (editor) {
        if (tables){

        }

        var elements = document.getElementsByClassName("editable");

        for (var i = 0; i < elements.length; i++){
            var removebutton = document.createElement("div");
            removebutton.style.position = "relative";
            removebutton.style.top = "0";
            removebutton.style.right = "0";
            removebutton.style.width = "12px";
            removebutton.style.height = "12px"
            removebutton.style.float = "right";
            removebutton.addEventListener('click', function(e) {
                var remover = document.getElementById("remove_div");
                remover.style.display = "block";
                document.getElementById("remove_div_name").innerHTML = this.parentElement.id;
                document.getElementById("no_button").onclick = function(){
                    remover.style.display = "none";
                }
            });
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
            addbutton.addEventListener('click', function(e){
                console.log("Adding " + this.parentElement.id);
            });
            elements[i].appendChild(addbutton);

            var settingsbutton = document.createElement("div");
            settingsbutton.style.position = "relative";
            settingsbutton.style.top = "0";
            settingsbutton.style.right = "0";
            settingsbutton.style.width = "12px";
            settingsbutton.style.height = "12px"
            settingsbutton.style.float = "right";
            settingsbutton.innerHTML = "S";
            settingsbutton.addEventListener('click', function(e){
                console.log("Settings of " + this.parentElement.id);
            });
            elements[i].appendChild(settingsbutton);
        }
    }
})