var https = require('http')


jsonObject = JSON.stringify(
    "C:\\Users\\devansh\\Desktop\\Zehnaseeb.mp3"
);
 

var postheaders = {
    'Content-Type' : 'application/json',
    'Content-Length' : Buffer.byteLength(jsonObject, 'utf8')
};
 

var optionspost = {
    host : '127.0.0.1',
    port : 8000,
    path : '/files/info/swift-container2',
    method : 'PUT',
    headers : postheaders
};
 
console.info('Options prepared:');
console.info(optionspost);
//console.info('Do the POST call');
 

var reqPost = https.request(optionspost, function(res) {
    console.log("statusCode: ", res.statusCode);
//  console.log("headers: ", res.headers);
 
    res.on('data', function(d) {
        console.info('POST result:\n');
        process.stdout.write(d);
        //console.info('\n\nPOST completed');
    });
});
 

reqPost.write(jsonObject);
reqPost.end();
reqPost.on('error', function(e) {
    console.error(e);
});
 