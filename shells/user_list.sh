#!/bin/bash

input="/etc/passwd"

while IFS=',' read -r username uid gid comment home shell
do
    echo "$count : $username - $uid - $gid - $home - $shell"
    let count+=1
done < $input