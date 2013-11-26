%define		packname	GO.db

Summary:	A set of annotation maps describing the entire Gene Ontology
Name:		R-%{packname}
Version:	2.10.1
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	5429c641ae326f75894ccfff9105dd21
URL:		http://www.bioconductor.org/packages/release/data/annotation/html/GO.db.html
BuildRequires:	R-AnnotationDbi
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-AnnotationDbi
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of annotation maps describing the entire Gene Ontology assembled
using data from GO.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/extdata
