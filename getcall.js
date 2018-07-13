var https = require('http');
 

var optionsget = {
    host : '127.0.0.1', 
    port : 8000,
    path : '/files/info/container5', // the rest of the url 
    method : 'GET' 
};
 
console.info('Options prepared:');
console.info(optionsget);
console.info('Do the GET call');
 
// do the GET request
var reqGet = https.request(optionsget, function(res) {
    console.log("statusCode: ", res.statusCode);
 
 
    res.on('data', function(d) {
        console.info('GET result:\n');
        process.stdout.write(d);
        console.info('\n\nCall completed');
    });
 
});
 
reqGet.end();
reqGet.on('error', function(e) {
    console.error(e);
});