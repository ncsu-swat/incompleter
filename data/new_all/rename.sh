for file in *; do 
  mv "$file" "${file%.py}.py.orig"
done
