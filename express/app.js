var WebSocketServer = require('ws').Server;
var http = require('http');
var express = require('express');
var app = express();

app.use(express.static(__dirname + '/'));

/*app.get('/endpoint', function(req, res){
	var obj = {};
	obj.title = 'title';
	obj.data = 'data';
	
	console.log('params: ' + JSON.stringify(req.params));
	console.log('body: ' + JSON.stringify(req.body));
	console.log('query: ' + JSON.stringify(req.query));
	
	res.header('Content-type','application/json');
	res.header('Charset','utf8');
	res.send(req.query.callback + '('+ JSON.stringify(obj) + ');');
});*/

app.post('/', function(req, res){
    var obj = {};
    console.log(req)
	// console.log('body: ' + JSON.stringify(req.body));
	res.send(req.body);
});


app.listen(3000);