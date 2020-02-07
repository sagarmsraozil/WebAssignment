// Time


var datee = new Date();
var year = datee.getFullYear();
document.getElementById("yeart").innerHTML += (year + " 4AM Movies.pvt.Ltd. All rights reserved.");

// looop
function abcd() {
    // var colors = ["red", "blue", "brown", "green"];
    // var color = ["white", "yellow", "orangered"];
    $("#loop").fadeOut(2000, function() {
        $("#moviee").fadeIn(2000, function() {
            $("#moviee").fadeOut(2000, function() {
                $("#loop").fadeIn(2000)
            })
        })
    });
    // var a = parseInt(Math.random() * color.length - 1);
    // var b = parseInt(Math.random() * colors.length - 1);
    // console.log(a);
    // console.log(b);
    // $("#loop").css({ "color": colors[b] }, 2000);
    // $("#moviee").css({ "color": color[a] }, 2000);




}



setInterval(
    function() {
        if (1 > 0) {
            abcd();
        }
    }, 8000);

/*  modal */

//setTimeout(
//        function() {
//            document.getElementById("modalFunction").click() == true;
//        }, 3000
//    )
    /* Owl carousel */
$('.wrapper').owlCarousel({
    loop: true,
    margin: 5,
    nav: true,
    autoplay: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});

function mouseclick() {
    document.querySelector(".down").style.display = "block";
    document.querySelector(".right").style.display = "none";
}

function mous() {
    document.querySelector(".down").style.display = "none";
    document.querySelector(".right").style.display = "block";
}

document.querySelector(".abcd").click()=true

function priceView()
{
    var quantity=parseInt(document.getElementById("no").value);
    var type=document.querySelector("#type").value;
    if(type=="2D")
    {
        document.getElementById("price").value=quantity*300;
    }
    else
    {
        document.getElementById("price").value=quantity*480;
    }
}