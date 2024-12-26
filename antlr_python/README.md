#Reused examples from https://github.com/AkiraHakuta/antlr4_Python3_examples
antlr4 -Dlanguage=Python3 LATEX.g4

python test.py ~/test.tex  
\begin{equation}
\langle \psi | \phi \rangle
\end{equation}

[@0,0:15='\begin{equation}',<86>,1:0]
[@1,17:23='\langle',<486>,2:0]
[@2,25:28='\psi',<779>,2:8]
[@3,30:30='|',<8>,2:13]
[@4,32:35='\phi',<751>,2:15]
[@5,37:43='\rangle',<810>,2:20]
[@6,45:58='\end{equation}',<337>,3:0]
[@7,60:59='<EOF>',<-1>,4:0]
(words (token (begin_equation \begin{equation})) (token (langle \langle)) (token (greek (psi \psi))) (token (absolute_value | user_variable <missing '|'>)) (token (greek (phi \phi))) (token (rangle \rangle)) (token (end_equation \end{equation})))
