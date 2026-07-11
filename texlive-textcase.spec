%global tl_name textcase
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	Case conversion ignoring mathematics, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textcase
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The textcase package offers commands \MakeTextUppercase and
\MakeTextLowercase which are similar to the standard \MakeUppercase and
\MakeLowercase, but they do not change the case of any sections of
mathematics, or the arguments of \cite, \label and \ref commands within
the argument. A further command \NoCaseChange does nothing but suppress
case change within its argument, so to force uppercase of a section
including an environment, one might say:
\MakeTextUppercase{...\NoCaseChange{\begin{foo}}
...\NoCaseChange{\end{foo}}...} In current LaTeX this package is
obsolete. You can use the standard \MakeUppercase and \MakeLowercase,
but it defines legacy names \MakeTextUppercase and \MakeTextLowercase.

