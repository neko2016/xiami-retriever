// retrieve song, album and artist ids from an encrypted URI

var location = "7h%md2F22285Emu%%8f63%%5nt25nF5F1F179pt35ca1255EutF..987216%23hDE34cbEE-lp%ac19%67451%_7636cd5%%l%2lo515279E_3k2%312-3553Fim%5E53_%lFe5577b15EEAoc%2%9%415.ayeEd9558%-";

var url = decodeURL(location);

function decodeURL(location){
    var loc = location.slice(1);
    var length = loc.length;
    var rows = parseInt(location[0]);
    var mod = length % rows;
    var baseCol = Math.floor(length / rows)

    nestedArr = [];
    for(var row = 0; row < rows; row++){
        if(row < mod){
            chunk = baseCol + 1;
        } else {
            chunk = baseCol;
        }
        nestedArr.push(loc.slice(0,chunk));
        loc = loc.slice(chunk);
    }

    dURL = '';
    for(var n = 0; n < length; n++){
        dURL += nestedArr[n%row][Math.floor(n/rows)];
    }
    console.log(decodeURIComponent(dURL).replace(/\^/g, '0'));
    return decodeURIComponent(dURL).replace(/\^/g, '0');

}

function getPosition(string, subString, index) {
   return string.split(subString, index).join(subString).length;
}

function getIDs(url){
    var ids = {};
    var nArtist = parseInt(getPosition(url, '/', 4));
    var nAlbum = parseInt(getPosition(url, '/', 5));
    var nSong = parseInt(getPosition(url, '/', 6));
    var nLine = parseInt(getPosition(url, '_',1));

    ids["artistID"] = url.slice(nArtist+1,nAlbum);;
    ids["albumID"] = url.slice(nAlbum+1,nSong);
    ids["songID"] = url.slice(nSong+1,nLine);
    return ids;
}

console.log(getIDs(url))
