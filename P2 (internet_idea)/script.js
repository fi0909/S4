var nama = String("admin")
var password = String("admin123")
function myfunction(){
    let id = document.getElementById("user_input").value;
    let pass = document.getElementById("user_input2").value;
    if (nama == id && password == pass){
        confirm("lets gooo")
    }
    else{
        alert("wrong username or password")
    }
}

let the_color = "light"
function fungsi2(){
    if (the_color != "light"){
        document.getElementById("pagestyle").setAttribute("href","main.css");
        the_color = "light";
    }
    else if(the_color == "light"){
        document.getElementById("pagestyle").setAttribute("href","dark.css");
        the_color = "dark";
    }
}