# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/textcase
# catalog-date 2007-03-01 12:49:13 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-textcase
Version:	20070301
Release:	1
Summary:	Case conversion ignoring mathematics, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textcase
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textcase.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textcase/textcase.sty
%doc %{_texmfdistdir}/doc/latex/textcase/README
%doc %{_texmfdistdir}/doc/latex/textcase/textcase.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textcase/textcase.dtx
%doc %{_texmfdistdir}/source/latex/textcase/textcase.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
