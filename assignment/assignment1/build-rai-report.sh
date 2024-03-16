# de citeproc is nodig om referenties te kunnen resolven
# de link-citations metadata kan je ofwel command line, ofwel via een extension meegeven, dwz --from markdown+yaml_metadata_block als extra optie aan de pandoc binary meegeven


rm rai-report.pdf;docker run --rm --volume "$(pwd):/opt/docs" avhconsult/pandoc pandoc --filter pandoc-fignos --from markdown+smart+table_captions --citeproc --bibliography /opt/docs/rai-report.bib --csl /opt/docs/vancouver.sty -M link-citations=true rai-report.md -o rai-report.pdf;open rai-report.pdf
