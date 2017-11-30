%{
/*
 * this sample demonstrates (very) simple recognition:
 * a verb/not a verb.
 */
#include <iostream> /* include c++ i/o routines */
using namespace std;
%}
%%

[\t ]+          /* ignore white space */ ;


is |
am |
are |
were |
was |
be |
being |
been |
do |      
does |
did |
will |
would |
should |
can |
could |
has |
have |
had |
go              { cout<<yytext<<": is a verb"<<endl; }

[a-zA-Z]+       { cout<<yytext<<": is not a verb"<<endl; }

.|\n            { ECHO; /* normal default anyway */ }
%%

int main()
{
        yylex();
}            
