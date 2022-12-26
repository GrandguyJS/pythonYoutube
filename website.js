
function getVids() {
    console.log("ABC");
    var json = {}


    var vids = document.getElementById("vids");
    console.log(json["id"].length);



    for (var i = 0; i < json["id"].length; i++) {
        
        
        var vid = document.createElement("div");
        vid.setAttribute("class", "vid");
        vid.setAttribute("id", "vid" + i);
        vid.setAttribute("onclick", `window.open('https://youtube.com/watch?v=${json["id"][i]}','_blank');`)
        vid.style.cursor = "pointer";
        
        vids.appendChild(vid);
        

        var img = document.createElement("img");
        img.setAttribute("class", "vidImg");
        img.setAttribute("id", "vidImg" + i);
        img.setAttribute("src", json["picture"][i]);
        vid.appendChild(img);

        var titleDiv = document.createElement("div");
        titleDiv.setAttribute("class", "titleDiv");
        
        titleDiv.style.width = "100%";
        titleDiv.style.textAlign = "center";
        titleDiv.style.fontFamily = "'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif";
        titleDiv.style.fontSize = "25px";

        var title = document.createElement("p");
        title.setAttribute("class", "vidTitle");
        title.innerHTML = json["title"][i];
        vid.appendChild(titleDiv);
        titleDiv.appendChild(title);

        

    
    }
}
