---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:00.266162+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: dispositivos_de_bloco_so
    weight: 10
    confidence: 0.98
  - name: dispositivos_loop
    weight: 9
    confidence: 0.95
  - name: dispositivos_hd
    weight: 8
    confidence: 0.9
  - name: dispositivos_ssd
    weight: 8
    confidence: 0.9
  - name: sistema_operacional
    weight: 7
    confidence: 0.85
  - name: gerenciamento_armazenamento
    weight: 7
    confidence: 0.8
  - name: particionamento_disco
    weight: 6
    confidence: 0.75
  - name: montagem_sistema_arquivos
    weight: 6
    confidence: 0.7
  - name: dispositivos_rom
    weight: 5
    confidence: 0.65
  - name: snap_pacotes
    weight: 5
    confidence: 0.6
  cdu_primary: '004.77'
  cdu_secondary:
  - '004.42'
  - '004.11'
  cdu_description: Organização e gestão de dispositivos de armazenamento e sistemas de arquivos em sistemas operacionais, com foco em dispositivos de bloco como HDs, SSDs e dispositivos loop (usados por pacotes Snap).
---
- Lista os dispostivos de bloco que o SO enxerga. Interessante que não são somente os HDs ou SSDs. Há também dispositivos de "loop". Exemplo em minha máquina dia 20201117:
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0    7:0    0 240,8M  1 loop /snap/chromium/1399
loop1    7:1    0 240,8M  1 loop /snap/chromium/1395
loop2    7:2    0  55,4M  1 loop /snap/core18/1932
loop3    7:3    0 161,4M  1 loop /snap/gnome-3-28-1804/128
loop4    7:4    0 162,9M  1 loop /snap/gnome-3-28-1804/145
loop5    7:5    0  55,3M  1 loop /snap/core18/1885
loop6    7:6    0    31M  1 loop /snap/snapd/9721
loop7    7:7    0  50,7M  1 loop /snap/snap-store/481
loop8    7:8    0 255,6M  1 loop /snap/gnome-3-34-1804/36
loop9    7:9    0  43,2M  1 loop /snap/snap-store/415
loop10   7:10   0    31M  1 loop /snap/snapd/9607
loop11   7:11   0 217,9M  1 loop /snap/gnome-3-34-1804/60
loop12   7:12   0 169,3M  1 loop /snap/spotify/42
loop13   7:13   0  62,1M  1 loop /snap/gtk-common-themes/1506
loop15   7:15   0   173M  1 loop /snap/spotify/43
sda      8:0    0 223,6G  0 disk 
├─sda1   8:1    0   529M  0 part 
├─sda2   8:2    0    99M  0 part /boot/efi
├─sda3   8:3    0    16M  0 part 
├─sda4   8:4    0 183,1G  0 part 
└─sda5   8:5    0  39,9G  0 part /
sr0     11:0    1  1024M  0 rom  
