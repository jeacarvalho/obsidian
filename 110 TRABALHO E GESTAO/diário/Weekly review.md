```dataview
TABLE file.mtime FROM -"99 TRABALHO E GESTAO/Serpro2021"
WHERE file.mtime >= (date("2025-01-26")) and file.mtime < (date("2025-01-30") + dur(1 day)) 
SORT file.mtime asc
