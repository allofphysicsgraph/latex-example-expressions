name=$(echo $1)
echo \(\"\\\\$name\", \" $(echo $name|tr '[a-z]' '[A-Z]') \" \),
