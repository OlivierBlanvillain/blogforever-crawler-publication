# watchmedo shell-command --wait --patterns="*.s*.md;*.template" --command "sh mk.sh"

cat *.md | pandoc \
  -t revealjs --template revealjs.template \
  --slide-level 1 -s -o index.html
   
xdotool search --name Chrome key --window %@ F5
