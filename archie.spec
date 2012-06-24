Name:		archie
License:	non-commercial
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Version:	1.4.1
Release:	10
Summary:	Simple archie client
Summary(pl):	Klient us�ugi sieciowej archie
Source0:	c-%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool that will let you check a database containing thousands of
entries for the files that're available at FTP sites around the world.

%description -l pl
Narz�dzie, pozwalaj�ce wyszukiwa� pliki w bazie serwer�w FTP

%prep
%setup -q 

%build
%{__make} OPTIONS="%{?debug:-O -g -DDEBUG}%{!?debug:$RPM_OPT_FLAGS} -I." DEFINES="" \
	LDFLAGS="%{!?debug:-s}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name} $RPM_BUILD_ROOT%{_bindir} 
install archie.man $RPM_BUILD_ROOT%{_mandir}/man1/archie.1
gzip -9nf README README.ALEX Prospero

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/archie
%{_mandir}/man1/*
%doc {README,README.ALEX,Prospero}.gz
