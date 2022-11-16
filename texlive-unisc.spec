Name:		texlive-unisc
Version:	63178
Release:	1
Summary:	Unicode small caps with Lua/XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unisc
License:	gpl3+ fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unisc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unisc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unisc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX produces small caps with \textsc{text} or {\scshape
text}. Neither of these commands produce small caps in Unicode.
If the output text is copied and pasted somewhere it shows the
same characters as used in the input. This package aims to
internally convert all the characters provided to the commands
mentioned above. It assumes that the file using this package is
compiled with Lua/XeLaTeX and a good Unicode font which has the
small caps characters, e.g., Charis SIL.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/unisc
%{_texmfdistdir}/tex/latex/unisc
%doc %{_texmfdistdir}/doc/latex/unisc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
