```dataviewjs
let docs = dv.pages('"iniciodia"');
let length = docs.length;
let numberToReturn = 2;
let rand1 = Math.floor(Math.random() * 2);
let rand2 = Math.floor(Math.random() * 2);
var items = [];
items.push(docs[rand1]);
items.push(docs[rand2]);

var randos = items

dv.list(items);
```

https://forum.obsidian.md/t/use-dataview-to-select-a-random-note-from-a-specified-folder/62476

https://notes.nicolevanderhoeven.com/obsidian-playbook/Obsidian+Plugins/Community+Plugins/dataview/Dataviewjs+Examples


```dataviewjs
dv.taskList(dv.pages('-"iniciodia"').file.tasks .where(t => !t.completed))
```