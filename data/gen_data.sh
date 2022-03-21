INT=$(( $RANDOM % 20 + 2 ))
let DATA_SIZE=$(( $RANDOM % 50 + 5 ))
for a in {0..20}
do
    LINE=$(cat names.txt | shuf | head -n $INT | tr '\n' ',' | sed 's/.$/\n/')
    echo $LINE >> data.txt
done
