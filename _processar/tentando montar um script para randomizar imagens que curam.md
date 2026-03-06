---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:41:34.330854+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: plugins_obsidian
    weight: 8
    confidence: 0.9
  - name: dataviewjs
    weight: 10
    confidence: 0.98
  - name: gerenciamento_notas
    weight: 7
    confidence: 0.85
  - name: selecao_aleatoria_notas
    weight: 9
    confidence: 0.92
  - name: codigos_javascript
    weight: 7
    confidence: 0.88
  - name: organizacao_digital
    weight: 6
    confidence: 0.75
  - name: ferramentas_produtividade
    weight: 7
    confidence: 0.8
  - name: comunidade_obsidian
    weight: 6
    confidence: 0.7
  - name: gerenciamento_tarefas
    weight: 5
    confidence: 0.65
  - name: links_externos
    weight: 5
    confidence: 0.6
  cdu_primary: '004.9'
  cdu_secondary:
  - '004.41'
  - '004.89'
  cdu_description: Processamento de dados. Sistemas de computadores. Organização. Gestão. Programação. Software. Inteligência artificial. Aplicações específicas de computadores. Sistemas de informação. Gestão de conhecimento.
---
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