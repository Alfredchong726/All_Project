function testingElse(val)
{
    if (val > 10){
        return "Bigger than 10";
    }
    else if (val < 5){
        return "Smaller than 5";
    }
   else{
        return "Between 5 and 10";
    }
}

function testSize(num)
{
    if (num < 5) {
        return "Tiny"
    }
    else if (num < 10) {
        return "Small"
    }
    else if (num < 15) {
        return "Medium"
    }
    else if (num < 20) {
        return "Large"
    }
    else {
        return "Huge"
    }

}


// console.log(testSize(19))

var names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]
function golfScore(par, strokes)
{
    if (strokes == 1) {
        return names[0]
    }
    else if (strokes <= par -2) {
        return names[1]
    }
    else if (strokes == par -1) {
        return names[2]
    }
    else if (strokes == par) {
        return names[3]
    }
    else if (strokes = par + 1) {
        return names[4]
    }
    else if (strokes == par + 2) {
        return naems[5]
    }
    else if (strokes >= par + 3) {
        return names[6]
    }
}

// console.log(golfScore(4, 5));

function caseInSwitch(val)
{
    var answer = "";
    switch (val) {
        case 1:
            answer = "alpha";
            break;

        case 2:
            answer = "beta";
            break;

        case 3:
            answer = "gamma";
            break;

        case 4:
            answer = "delta";
            break;
    }
    return answer;
}

// console.log(caseInSwitch(4))

function switchOfStuff(val)
{
    var answer = "";
    switch (val) {
        case "a":
            answer = "apple";
            break;

        case "b":
            answer = "bird";
            break;

        case "c":
            answer = "cat";
            break;

        default:
            answer = "stuff";
            break;
    }
    return answer;
}

// console.log(switchOfStuff("t"))

function sequentialSizes(val)
{
    var answer = "";
    switch(val){
        case 1:
        case 2:
        case 3:
            answer = "Low";
            break;
        case 4:
        case 5:
        case 6:
            answer = "Mid";
            break;
        case 7:
        case 8:
        case 9:
            answer = "High";
            break;

    }
    return answer
}

// console.log(sequentialSizes(5))

function chainToSwitch(val)
{
    var answer = "";

    switch(val){
        case "bob":
            answer = "Marley";
            break;
        case 42:
            answer = "The Answer";
            break;
        case 1:
            answer = "There is no #1";
            break;
        case 99:
            answer = "Missed me by this much!"
            break;
        case 7:
            answer = "Ate Nine";
            break;
    }
    return answer
}
