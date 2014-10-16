var fs = require('fs');
var path = require('path');
var args = process.argv.splice(2);
var command = args.shift();
var taskDescription = args.join('  ');
var file = path.join(process.cwd(), '/.tasks');

switch(command){
  case 'list':
    listTasks(file);
    break;

  case 'add':
    addTask(file, taskDescription);
    break;

  case 'remove':
    removeTask(file, taskDescription);
    break;

  default:
    var nameOfProcess = [];
    nameOfProcess = process.argv[1].split("/");//Holy crap it worked!
    console.log('Usage: ' + nameOfProcess[5] + ' list|add [taskDescription]');

}

function loadOrInitializeTaskArray(file, cb) {
  fs.exists(file, function(exists){
    var tasks = [];  
    var data = "";
    if (exists) {
      fs.readFile(file,'utf8', function(err, data){
        if (err) throw err;
        data = data.toString();
        var tasks = JSON.parse(data || '[]');
        cb(tasks);
      });
    }else {
      cb([]);
    }
  });
}

function listTasks(file)
{
  loadOrInitializeTaskArray(file, function (tasks) {
    for(var i in tasks) {
      console.log(tasks[i]);
    }
  });
}

function storeTasks(file, tasks){
    fs.writeFile(file, JSON.stringify(tasks), 'utf8', function(err) {
      if (err) throw err;
      console.log('Saved');
    });
}

function removeTask(file, taskDescription){
  loadOrInitializeTaskArray(file, function(tasks){
    var i = tasks.indexOf(taskDescription);
    console.log((tasks.splice(i,1).toString()));//even more holy crap, this worked too.
    storeTasks(file, tasks);
});
}

function addTask(file, taskDescription){
  loadOrInitializeTaskArray(file, function(tasks){
    tasks.push(taskDescription);
    storeTasks(file, tasks);
  });
}
