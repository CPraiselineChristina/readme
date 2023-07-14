<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Welcome to HOLYBIBLE's documentation! — HOLY BIBLE : Version - 1.0 documentation</title>
    <link rel="stylesheet" type="text/css" href="_static/pygments.css" />
    <link rel="stylesheet" type="text/css" href="_static/alabaster.css" />
    <script data-url_root="./" id="documentation_options" src="_static/documentation_options.js"></script>
    <script src="_static/doctools.js"></script>
    <script src="_static/sphinx_highlight.js"></script>
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" />
    <style>
<style>
  body {
    font-size: 16px;
    font-family: Arial, sans-serif;
    background-color: grey;
    color: #adadac;
  }

  .document {
    background-color: black;
  }

  pre code {
    font-size: 14px;
    font-family: "Courier New", monospace;
  }

  /* Additional styles for specific elements */
  h1 {
    color: #7f7d9c; /* white color */
  }

  h2 {
    color: #9897a9; /* white color */
  }

  p {
    color: #adadac; /* light white color */
  }

  a {
    color: #808080; /* light white color */
  }

  /* Change background color of the theme window */
  .documentwrapper {
    background: linear-gradient(to top right, #808080, #373737); /* Replace with your desired gradient colors */
  }

  /* Apply gradient background color of the bodywrapper */
  .bodywrapper {
    background: linear-gradient(to top right, #adadc9, #4d4c5c); /* Replace with your desired gradient colors */
    background-size: cover;
  }
</style>

<script>
  /*
  function handleSearchFormSubmit(event) {
    event.preventDefault(); // Prevent form submission

    var query = document.getElementById("search-input").value;
    // Display the search keyword in the document
    document.getElementById("search-keyword").textContent = query;

    // Perform search operation based on the query
    // Add your search functionality code here
    console.log("Search query:", query);
  }
  */
</script>

    </style>
    <link rel="stylesheet" href="_static/custom.css" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=0.9, maximum-scale=0.9" />
  </head>
  <body>
    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            <section id="welcome-to-holybible-s-documentation">
              <h1>Welcome to HOLYBIBLE's documentation!<a class="headerlink" href="#welcome-to-holybible-s-documentation" title="Permalink to this heading">¶</a></h1>
              <div class="toctree-wrapper compound">
              </div>
            </section>

            <section id="bible-overview">
              <h2>Bible Overview</h2>
              <p>This is a HOLY BIBLE that helps in reading and refering the bible with multiple related search references of input text that
                provides various functionalities to work with the HOLY BIBLE text. It includes the following functions:</p>
              <ul>
                <li><strong>Load Bible:</strong> Loads the entire HOLY BIBLE text from a file.</li>
                <li><strong>Search Reference:</strong> Performs a search in the HOLY BIBLE text and displays related references based on the input query.</li>
                <li><strong>Books:</strong> Retrieves the chapter count for a specific book.</li>
              </ul>
              <p>These functions allow users to interact with the HOLY BIBLE text and perform various operations. developed by C. Praiseline Christina</p>
            </section>

            <section id="Load Bible">
              <h2>Load Bible</h2>
              <p>The load_bible function loads the HOLY BIBLE text from a file and stores it in memory for further processing.</p>
              <pre><code>def load_bible():
    file_path = r"C:\Users\path\f
            </section>

            <section id="Search Reference">
              <h2>Search Reference</h2>
              <p>The search_file function performs a search in the loaded HOLY BIBLE text based on the user's input query. It displays a list of related references that match the search query.</p>
              <pre><code>def search_file():
    search_query = query_entry.get()

            </section>

            <section id="Books">
              <h2>Books Search</h2>
              <p>The get books function retrieves the number of books for a specific book in the HOLY BIBLE. It returns a list of chapter numbers.</p>
              <pre><code>def on_book_selected(event):
    selected_book = book_combo.get()

    </code></pre>
            </section>

            <section id="Chapters Search">
              <h2>Chapters Search</h2>
              <p>The get chapters function retrieves the number of chapters for a specific book in the HOLY BIBLE. It returns a list of chapter numbers.</p>
              <pre><code>def on_chapter_selected(event):
    selected_book = book_combo.get()

    </code></pre>
            </section>

            <section id="Verses Search">
              <h2>Verses Search</h2>
              <p>The get verse function retrieves the number of verse for a specific verses in the HOLY BIBLE. It returns a list of chapter numbers.</p>
              <pre><code>def on_verse_selected(event):
    selected_book = book_combo.get()

    </code></pre>
            </section>  <section id="Module 1 Load Bible">
              <h2>Module 1 Load Bible</h2>
              <p>This code loads the entire HOLY BIBLE</p>
              <pre><code>def load_bible():
    file_path = (file_path, 'r')
    try:
        with open(file_path, 'r') as file:
            bible_text = file.read()
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, bible_text)
    except FileNotFoundError:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "Bible file not found.")

    </code></pre>

</section>  <section id="Module 2 Search Reference">
              <h2>Module 2 Search Reference</h2>
              <p>This code results in the multiple related references of the input Word</p>
              <pre><code>def search_file():
    search_query = query_entry.get()

    if search_query == '':
        messagebox.showerror("Error", "Please enter a search query.")
        return

    try:
        with open(r"C:\Users\THINK\Desktop\kjv.txt", 'r') as file:
            bible_text = file.read()

        found_lines = []
        found_references = []
        lines = bible_text.split('\n')
        for index, line in enumerate(lines):
            if search_query.lower() in line.lower():
                found_lines.append(line)
                reference = f"Verse {index + 1}"
                found_references.append(reference)

        if found_lines:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Search results:\n")
            for found_line, found_reference in zip(found_lines, found_references):
                result_text.insert(tk.END, f"{found_reference}: {found_line.strip()}\n")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No matching results found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    </code></pre>

            </section>  <section id="Module 3 Search Books">
              <h2>Module 3 Search Books</h2>
              <p>This code results in the book search fom the HOLY BIBLE</p>
              <pre><code>def on_book_selected(event):
    selected_book = book_combo.get()
    chapters = get_chapters(selected_book)
    chapter_combo['values'] = chapters
                 </code></pre>


             </section>  <section id="Module 4 Search Chapters">
              <h2>Module 4 Search Chapters</h2>
              <p>This code results in the Chapter search fom the HOLY BIBLE</p>
              <pre><code>def on_chapter_selected(event):
    selected_book = book_combo.get()
    selected_chapter = chapter_combo.get()
    verses = get_verses(selected_book, selected_chapter)
    verse_combo['values'] = verses
                 </code></pre>


            </section>  <section id="Module 5 Search Verses">
              <h2>Module 5 Search Verses</h2>
              <p>This code results in the Verses search fom the HOLY BIBLE</p>
              <pre><code>def on_verse_selected(event):
    selected_book = book_combo.get()
    selected_chapter = chapter_combo.get()
    selected_verse = verse_combo.get()

    # Retrieve the verse from the Bible text file
    verse = get_verse(selected_book, selected_chapter, selected_verse)

    # Display the result in the selected_verse_text widget
    selected_verse_text.delete('1.0', tk.END)
    selected_verse_text.insert(tk.END, f"Selected Verse: {selected_book} {selected_chapter}:{selected_verse}\n")
    selected_verse_text.insert(tk.END, f"Verse Text: {verse}\n")
                 </code></pre>



            <section id="details-about-the-software">
              <h2>Details about the Software</h2>
              <p>Package Name: HOLY BIBLE
                Version: 1.0.0
              </p>

              <p>This is a HOLY BIBLE Module where it loads an entire HOLY BIBLE, performs searches and displays related references, and provides functionalities to access specific chapters and verses. HOLY BIBLE is a package that aims to facilitate the integration of biblical content into Python projects.</p>

              <p>Installation Instructions:</p>
              <p>To install HOLY BIBLE, you can use pip, the Python package manager. Simply run the following command in your terminal:</p>

              <p>Windows: <code>pip install HOLY-BIBLE</code></p>
              <p>Mac: <code>$ pip install HOLY-BIBLE</code></p>

              <p>Usage Guide:</p>
              <p>Once HOLY BIBLE is installed, you can import it into your Python projects using the following import statement:</p>

              <pre><code>import holy_bible</code></pre>

              <p>HOLY BIBLE offers a rich set of functionalities to work with the Bible text. You can retrieve specific verses, search for keywords or phrases, access chapters and books, and more. Detailed usage examples and API documentation can be found in the package's documentation.</p>

              <p>API Documentation:</p>
              <p>The HOLY BIBLE package provides a user-friendly API to interact with the biblical text. The documentation covers all the available methods, classes, and parameters, along with example code snippets to help you get started.</p>

              <p>License Information:</p>
              <p>HOLY BIBLE is released under a software license. You can find the full text of the license in the LICENSE file included with the package.</p>

              <p>Author and Contact Information:</p>
              <p>HOLY BIBLE is developed and maintained by C. Praiseline Christina, the founder of God Claved Hallow Ministries. You can contact the author via email at praiseline2021@outlook.com.</p>

              <p>Links and References:</p>
              <ul>
                <li><a href="https://pypi.org/project/HOLY-BIBLE">PyPI Package Page</a></li>
              </ul>

              <p>Please note that HOLY BIBLE is a package providing access to the biblical text and does not include any religious interpretations or commentary. It aims to facilitate the integration of Bible content into Python applications and projects.</p>
            </section>

            <section id="indices-and-tables">
              <h1>Indices and tables<a class="headerlink" href="#indices-and-tables" title="Permalink to this heading">¶</a></h1>
              <ul class="simple">
                <li><p><a class="reference internal" href="#bible-overview">Bible Overview</a></p></li>
                <li><p><a class="reference internal" href="#load-bible">Load Bible</a></p></li>
                <li><p><a class="reference internal" href="#search-file">Search References</a></p></li>
                <li><p><a class="reference internal" href="#get-books">Books Search</a></p></li>
                <li><p><a class="reference internal" href="#get-chapters">Chapter Search</a></p></li>
                <li><p><a class="reference internal" href="#get-verses">Verses Search</a></p></li>
                <li><p><a class="reference internal" href="#Module 1">Module 1 - Load Bible</a></p></li>
                <li><p><a class="reference internal" href="#Module 2">Moddule 2 - Search Reference</a></p></li>
                <li><p><a class="reference internal" href="#Module 3">Module 3 - Search Books</a></p></li>
                <li><p><a class="reference internal" href="#Module 4">Module 4 - Search Chapters</a></p></li>
                <li><p><a class="reference internal" href="#Module 5">Module 5 - Search Verses</a></p></li>
                <li><p><a class="reference internal" href="genindex.html"><span class="std std-ref">Index</span></a></p></li>
                <li><p><a class="reference internal" href="py-modindex.html"><span class="std std-ref">Module Index</span></a></p></li>
                <li><p><a class="reference internal" href="search.html"><span class="std std-ref">Search Page</span></a></p></li>
              </ul>
            </section>
          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
          <h1 class="logo"><a href="#">HOLYBIBLE</a></h1>
          <h3>God Claved Hallow Ministries</h3>
          <div class="relations">
            <h3>Related Topics</h3>
            <ul>

              <li><a href="#">Documentation overview</a>
                <ul>
                </ul>
              </li>
            </ul>
          </div>
          <div id="searchbox" style="display: none" role="search">
            <h3 id="searchlabel">Quick search</h3>
            <div class="searchformwrapper">
              <form class="search" action="search.html" method="get">
                <input type="text" name="q" aria-labelledby="searchlabel" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" />
                <input type="submit" value="Go" />
              </form>
            </div>
          </div>
          <script>document.getElementById('searchbox').style.display = "block"</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="footer">
      &copy;2023, C. Praiseline Christina. |
      Powered by <a href="God claved hallow ministries">God Claved Hallow Ministries</a> |
      <a href="_sources/index.rst.txt" rel="nofollow">Page source</a>
    </div>
  </body>
</html>
