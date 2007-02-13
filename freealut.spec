Summary:	Free implementation of OpenAL's ALUT standard
Summary(pl.UTF-8):	Wolnodostępna implementacja standardu ALUT OpenAL-a
Name:		freealut
Version:	1.1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.openal.org/openal_webstf/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	e089b28a0267faabdb6c079ee173664a
URL:		http://www.openal.org/
BuildRequires:	OpenAL-devel >= 0.0.8-1
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free implementation of ALUT (OpenAL Utility Toolkit) standard.

%description -l pl.UTF-8
Wolnodostępna implementacja standartu ALUT (OpenAL Utility Toolkit).

%package devel
Summary:	Headers for freealut
Summary(pl.UTF-8):	Pliki nagłówkowe do freealuta
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenAL-devel >= 0.0.8-1

%description devel
freealut header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe freealuta.

%package static
Summary:	Static alut library
Summary(pl.UTF-8):	Statyczna biblioteka alut
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static alut library.

%description static -l pl.UTF-8
Biblioteka alut do konsolidacji statycznej.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I admin/autotools/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libalut.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/libalut.so
%{_libdir}/libalut.la
%{_examplesdir}/%{name}-%{version}
%{_includedir}/AL/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libalut.a
