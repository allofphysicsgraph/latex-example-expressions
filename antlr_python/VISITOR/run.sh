file_name=$(ls cases|shuf|sed -n 1p)
echo $file_name
cat cases/"$file_name"
python test.py cases/$file_name
