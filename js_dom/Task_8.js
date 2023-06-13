let senseOfLife = 42;

function showVariable (otherSenseOfLife) {
    if(!otherSenseOfLife) {
        return senseOfLife;
    }
    senseOfLife=otherSenseOfLife;
    return senseOfLife;
}
console.log(showVariable(42));