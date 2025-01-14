counter=0;while read f ;do echo $f > test_"$counter".tex ;counter=$(($counter+1));done < <(grep sum *.py|grep '\\' |grep Sum|grep -oP '".*?"'|tr -d '"' |sed 's/\\/\\\\/g')

