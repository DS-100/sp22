const startOfSu20InMilli = new Date(2020, 5, 22, 0, 0, 0, 0).getTime();
const oneWeekInMilli = 604800000;

function highlightAndScrollToWeek() {
    const currentMilli = (new Date()).getTime();
    const currWeekIndex = Math.floor((currentMilli - startOfSu20InMilli) / oneWeekInMilli);
    var currentWeekTab = document.getElementsByClassName("module")[currWeekIndex];
    currentWeekTab.style.background = "linear-gradient(90deg, #2869e6 1%, white 1%)";
    var header = currentWeekTab.children[0];
    header.style.borderStyle = "none";
    var body = currentWeekTab.children[1];
    body.style.borderStyle = "none";
    var children = body.children;
    for (var i = 0; i < children.length; i++) {
        var currChild = children[i];
        if (!currChild.className.startsWith("module-event")) {
        currChild.style.border = "none";
        }
    }
    var embedScriptTabs = document.getElementsByClassName("module-body");
    for (var i = 0; i < embedScriptTabs.length; i++) {
        var embedChildren = embedScriptTabs[i].children;
        if (embedChildren.length == 1) {
            if (embedChildren[0].tagName.toLowerCase() == 'script') {
                embedScriptTabs[i].style.width = "0px";
                embedScriptTabs[i].style.height = "0px";
                embedScriptTabs[i].style.padding = "0px";
            }
        }
    }
    // Auto Scroll To Current Week's Tab
    currentWeekTab.scrollIntoView({
        behavior: 'auto',
        block: 'center'
    });

}

document.addEventListener("DOMContentLoaded", function(event) {
    highlightAndScrollToWeek();
});
