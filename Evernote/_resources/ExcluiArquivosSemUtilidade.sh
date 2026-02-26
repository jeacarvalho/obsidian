#!/usr/bin/env bash
# mycat.sh
#
# versão 1: solução naïve

arquivo="$1"

while read linha; do
    echo "$linha"
    rm "$linha"
done < "$arquivo"

