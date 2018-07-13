var https = require('http')

jsonObject = JSON.stringify(
    "file path"
);

var postheaders = {
    'Content-Type' : 'application/json',
    'Content-Length' : Buffer.byteLength(jsonObject, 'utf8')
};
 
var optionspost = {
    host : '127.0.0.1',
    port : 8000,
    path : '/file/inside/container2',
    method : 'PUT',
    headers : postheaders
};
 
console.info('Options prepared:');
console.info(optionspost);

var reqPost = https.request(optionspost, function(res) {
    console.log("statusCode: ", res.statusCode);
 
    res.on('data', function(d) {
        console.info('POST result:\n');
        process.stdout.write(d);
    });
});
 

reqPost.write(jsonObject);
reqPost.end();
reqPost.on('error', function(e) {
    console.error(e);
});
 
