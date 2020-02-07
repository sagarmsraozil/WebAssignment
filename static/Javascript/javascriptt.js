// Quiz 
var questions = ["Who is main character of Your name?", "Who is main character of Weathering with you?", "Who is main character of A silent voice?", "Who is main character of Wolf Children?", "Who is main character of Spirited Away?","Who is the main female character of I want to eat your pancreas?"];
var answers = ["Taki and Mitshua", "Hodaka and Hina", "Nishimiya and Ishida", "Sohei", "Chihiro","Sakura"];
var options = [
    ["Kaneki and Touka", "Taki and Mitshua", "Mikasa and Eren"],
    ["Nezuko and Tanjiro", "Emma and Norman", "Hodaka and Hina"],
    ["Kaneki and Touka", "Nishimiya and Ishida", "Mikasa and Eren"],
    ["Zenitsu", "Ray", "Sohei"],
    ["Hyakkimaru", "Chihiro", "Armen"],
    ["Sakura","Touka","Mikasa"]
];

var i = 0;
var ans_holder = new Array(questions.length);

function btn_next() {
    ans_holder[i] = document.forms["quiz-Work"]["quiz"].value;
    if (ans_holder[i] != answers[i]) {
        document.querySelector(".checker").innerHTML = "Wrong";


    } else {
        if (i < questions.length - 1) {
            document.querySelector(".checker").innerHTML = "";

            i++;
            iterator(i);

        } else {
            document.querySelector(".checker").innerHTML = "You successfully answered every questions!!";
        }
    }

}

function btn_previous() {
    ans_holder[i] = document.forms["quiz-Work"]["quiz"].value;
    if (ans_holder[i] != answers[i]) {
        document.querySelector(".checker").innerHTML = "Wrong";


    } else {
        if (i > 0) {
            document.querySelector(".checker").innerHTML = "";

            i--;
            iterator(i);

        }
    }

}

function iterator(x) {

    document.getElementById("questions").innerHTML = ((x + 1) + ". " + questions[x]);
    do {
        for (var k = x; k <= x; k++) {
            for (var i = 0; i < options[k].length; i++) {
                document.getElementById("quiz" + (i + 1)).value = options[k][i];
                document.getElementById("label" + (i + 1)).innerHTML = options[k][i];
                if (ans_holder[k] == document.getElementById("quiz" + (i + 1)).value) {
                    document.getElementById("quiz" + (i + 1)).checked = true;
                } else {
                    document.getElementById("quiz" + (i + 1)).checked = false;
                }
            }
        }
    }
    while (k > 1000)
}


iterator(i);

// Time


var datee = new Date();
var year = datee.getFullYear();
document.getElementById("yeart").innerHTML += (year + " 4AM Movies.pvt.Ltd. All rights reserved.");