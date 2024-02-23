function decodeHtml(html) {
    var txt = document.createElement("textarea");
    txt.innerHTML = html;
    return txt.value;
}

function getTime(timestamp) {
     date = new Date(timestamp);

    var year = date.getFullYear();
    var month = (date.getMonth() + 1);
    var day = date.getDate();

    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();

    return formateTime(year, month, day, hour, minute, second);
}

function formateTime(year, month, day, hour, minute, second) {
    return makeDoubleDigit(year) + "-" +
        makeDoubleDigit(month) + "-" +
        makeDoubleDigit(day) + " " +
        makeDoubleDigit(hour) + ":" +
        makeDoubleDigit(minute) + ":" +
        makeDoubleDigit(second);
}

function makeDoubleDigit(x) {
    return (x < 10) ? "0" + x : x;
}


String.prototype.format = String.prototype.f = function () {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};