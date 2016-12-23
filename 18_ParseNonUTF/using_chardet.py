import chardet

curlinkname = 'Good bye in Swedish is Hej'
code = chardet.detect(curlinkname)
linkname = curlinkname.decode(code['encoding'], errors="replace")

print linkname