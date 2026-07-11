%global tl_name docutils
%global tl_revision 56594

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Helper commands and element definitions for Docutils LaTeX output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/docutils
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docutils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docutils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is intended for use with LaTeX documents generated from
reStructuredText sources with Docutils. When generating LaTeX documents,
specify this package with the stylesheet configuration option, e.g.
rst2latex --stylesheet=docutils exampledocument.txt

