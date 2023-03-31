Name:		texlive-docutils
Version:	56594
Release:	2
Summary:	Helper commands and element definitions for Docutils LaTeX output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/docutils
License:	bsd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docutils.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docutils.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is intended for use with LaTeX documents generated
from reStructuredText sources with Docutils. When generating
LaTeX documents, specify this package with the stylesheet
configuration option, e.g. rst2latex --stylesheet=docutils
exampledocument.txt

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/docutils
%doc %{_texmfdistdir}/doc/latex/docutils

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
