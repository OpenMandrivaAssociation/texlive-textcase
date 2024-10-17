Name:		texlive-textcase
Version:	67755
Release:	1
Summary:	Case conversion ignoring mathematics, etc
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textcase
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The textcase package offers commands \MakeTextUppercase and
\MakeTextLowercase are similar to the standard \MakeUppercase
and \MakeLowercase, but they do not change the case of any
sections of mathematics, or the arguments of \cite, \label and
\ref commands within the argument. A further command
\NoCaseChange does nothing but suppress case change within its
argument, so to force uppercase of a section including an
environment, one might say:
\MakeTextUppercase{...\NoCaseChange{\begin{foo}}
...\NoCaseChange{\end{foo}}...}.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textcase/textcase.sty
%doc %{_texmfdistdir}/doc/latex/textcase/README
%doc %{_texmfdistdir}/doc/latex/textcase/textcase.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textcase/textcase.dtx
%doc %{_texmfdistdir}/source/latex/textcase/textcase.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
