Name:		archie
License:	non-commercial
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Version:	1.4.1
Release:	1
Summary:	Simple archie client
Summary(pl):	Klient us³ugi sieciowej archie
Source0:	c-%{name}-%{version}.tar.gz
Patch0:		%{name}-FLAGS.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool that will let you check a database containing thousands of entries 
for the files that're available at FTP sites around the world.

%description -l pl
Narzêdzie, pozwalaj±ce wyszukiwaæ pliki w bazie serwerów FTP

%prep
%setup -q 
%patch0 -p1

%build
%{__make} 

%install
install -d $RPM_BUILD_ROOT%{_bindir} \
			$RPM_BUILD_ROOT%{_mandir}/man1
install %{name} $RPM_BUILD_ROOT%{_bindir} 
install archie.man $RPM_BUILD_ROOT%{_mandir}/man1/archie.1

%files
%{_mandir}/man1/*
%defattr(644,root,root,755)
%doc README Prospero archie.doc
%attr(755,root,root) %{_bindir}/archie
