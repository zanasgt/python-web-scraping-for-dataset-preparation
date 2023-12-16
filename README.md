![headshot] (octocat-random.png)

This repisotory is a part of my thesis study to detect negation on biomedial corpus with DL methods. 
Repisotory has two py script which is responsible to
  1. Collect the articles by simple web scraping applied to a spesific web page https://dergipark.org.tr/tr/.
  2. Translate collected pdf s into text files for pre-process stage to create a corpora.

The web page is a subproject of formal science institution in Turkey and Medical/Bimedical articles have been collect here by using sub branches URL for different departments of medicine. 

 * Unfortunately URL logic is not straightforward to download pdf s directly yet it solved by applying additional constant URL part "&section=articles&aggs%5BarticleType.id%5D%5B0%5D=55" in collect_articles.py.

To translate pdf s into text file for post edit, PyPDF2 library has been used. Here the files not translated in easy format because of pdf properties or the need of advance properties for pdf translator.
Because of this reason the text file should be review and correct via hand craft techniques or some code snippets.

  clean_text(input_text) function is written to manage the correction of some mistypes which can be automated with some regex functions in 're' library. 
