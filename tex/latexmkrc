$pdflatex = 'pdflatex --file-line-error --shell-escape -interaction=nonstopmode  %O %S';
$pdf_previewer = "start evince %O %S";
$pdf_update_method = 0;
$pdf_mode = 1;
$bibtex_use = 1;
$preview_continuous_mode = 1;

@default_files = ('main.tex');

add_cus_dep('md', 'mdtex', 0, 'md2tex');
sub md2tex {
  return system("
    cat $_[0].md | sed -r '
    s/@@/@@ /g
    s/##/## /g
    s/@([A-Za-z0-9]+)/\\\\cite{\\1}/g
    s/#([A-Za-z0-9]+)/\\\\autoref{\\1}/g
    s/@@ /@/g
    s/## /#/g
    ' | pandoc -f markdown -t latex -o $_[0].mdtex");
};
