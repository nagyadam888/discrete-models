# Lecture notes for Applications of discrete models and Diszkrét modellek alkalmazásai

This is is the source of lecture notes for the subjects in the title.
The subject is taught in two different language (english and hungarian) with the same content.

TODO write about the purpose of this lecture notes and about the general directions.

## Supporting multiple languages

The support of multiple languages in this latex document based on the 
`multilang` package, which can be found [here](https://github.com/Ri-Ga/multilang). 
With the help of this package the document can be structured logically (according
to the content) so there is no need to create/manage two document for the various languages. 

#### Compiling for different languages
The document can be compiled with one of the latex compilers (I prefer and use `pdflatex`), 
the only thing that will decide, in which language the output will be written depends on the
language settings of the `babel` package. For hungarian you need the
```
    \usepackage[magyar]{babel}
```
line; while for english you need the 
```
    \usepackage[english]{babel}
```  
line in the `lecture_notes.tex` document's preamble.

[TODO Makefile reference if there will be a makefile]

#### Editing the multi-language document
There are just a few commands that you need to know to edit both of the languages
in the same time. The first such command is the `\Wrap`, which you can use to write 
content in multiple languages. An example looks like this:
```
\Wrap{
    content/english={The english text about something},
    content/magyar ={Szöveg magyarul}
}
```

This little command would be enough to write the document parallelly using two or 
more languages, but this little wrapper not intended to contain more complicated things
than simple text. The convenient use of environments can be done via the `Part, Part*, 
Section, Section*, Subsection, Subsection*, Paragraph, Paragraph*, Subparagraph, Subparagraph*` 
commands like this:
```
\begin{Section}{title/english=CoolSectionTitle, title/magyar=MenőSectionCím}
    ...
    \Wrap{
        ...
    }
    ...
\end{Section}
```

A few`theorem` type of environments also could be used. The `\definition, \theorem` and 
`\exercise` (as of now) works according to the language settings, so for example the 
`definition` used like this below would result *1.1 Definition (...)* in english and 
*1.1 Definíció (...)* in hungarian (if it is the 1.1 definition).
```
\begin{definition}[\wrap{...}]
    ...
\end{definition}
```
### TODO list 
- Write the translation (english) for the first section
- Structure the source according to the logical structure
- Add a more informative README.md
- Add solutions for the exercises 
- Add a section that gives introduction to SageMath
- Add more sections 
