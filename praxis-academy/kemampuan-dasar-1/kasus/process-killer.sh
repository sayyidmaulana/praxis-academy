function psapp() {
 ps -ax | grep -i $1 | grep -i -v  "grep.-i.$1" | awk '{print $1}'
 }
 function killapp() {
     kill $(psapp $1)
 }
