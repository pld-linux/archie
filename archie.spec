Summary:	Simple archie client
Summary(pl):	Klient us³ugi sieciowej archie
Name:		archie
Version:	1.4.1
Release:	11
License:	non-commercial
Group:		Applications/Networking
Source0:	c-%{name}-%{version}.tar.gz
#Source0:	http://www.netsw.org/infosys/archie/c-%{name}-%{version}-FIXED.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool that will let you check a database containing thousands of
entries for the files that're available at FTP sites around the world.

%description -l pl
Narzêdzie pozwalaj±ce wyszukiwaæ pliki w bazie serwerów FTP.

%prep
%setup -q

%build
%{__make} OPTIONS="%{rpmcflags} %{?debug:-DDEBUG} -I." \
	DEFINES="-DNEED_TIME_H" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install archie.man $RPM_BUILD_ROOT%{_mandir}/man1/archie.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.ALEX Prospero
%attr(755,root,root) %{_bindir}/archie
%{_mandir}/man1/*
