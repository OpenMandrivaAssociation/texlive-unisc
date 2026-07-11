%global tl_name unisc
%global tl_revision 78632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Unicode small caps with Lua/XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/unisc
License:	gpl3+ fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unisc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unisc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unisc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX produces small caps with \textsc{text} or {\scshape text}. Neither
of these commands produce small caps in Unicode. If the output text is
copied and pasted somewhere it shows the same characters as used in the
input. This package aims to internally convert all the characters
provided to the commands mentioned above. It assumes that the file using
this package is compiled with Lua/XeLaTeX and a good Unicode font which
has the small caps characters, e.g., Charis SIL.

