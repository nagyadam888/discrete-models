# Lecture notes for Applications of discrete models and Diszkrét modellek alkalmazásai

This is is the source of lecture notes for the subjects in the title.
The subject is taught in two different language (english and hungarian) with the same content.

TODO write about the purpose of this lecture notes and about the general directions.

## Supporting multiple languages

The support for multiple languages in this latex document based on the 
`multilang` package, which can be found [here](https://github.com/Ri-Ga/multilang). 
With the help of this package the document can be structured logically according
to the content and there is no need to create two document for the various languages. 

#### Compiling for different languages
To get the pdf document in hungarian for example you need the 
```
    \usepackage[magyar]{babel}
```
line not commented, while the 
```
    \usepackage[english]{babel}
```  
commented in the `lecture_notes.tex` document. Then you can compile it 
(for example with `pdflatex) and get the pdf document in the desired language.

#### Editing the multi-language document
There are a few environments and commands that need to be used to edit both
of the languages in the same time. The first command is the `\Wrap` which is 
used to give separate translations of the same content and can be used like this:
```
\Wrap{
    content/english={The english text about something},
    content/magyar ={Szöveg magyarul}
}
```
You could solve almost everything with this little wrapper command, but for 
convinient you can use the `Part, Part*, Section, Section*, Subsection, Subsection*, 
Paragraph, Paragraph*, Subparagraph, Subparagraph*` environments and then you only
need to define the title of it just like this:
```
\begin{Section}{title/english=CoolSectionTitle, title/magyar=MenőSectionCím}
    ...
    \Wrap{
        ...
    }
    ...
\end{Section}
```

The last part that is need to be mentioned are the `theorem` commands, which 
are the`\definition, \theorem` and `\exercise` (as of now). The usage of them 
are very similar to each other and here is an example with `definition`:
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
