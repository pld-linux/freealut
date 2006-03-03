Summary:	Free implementation of OpenAL's ALUT standard
Summary(pl):	Wolna implementacja standartu ALUT OpenALa
Name:		freealut
Version:	1.0.1
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.openal.org/openal_webstf/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	2df161090428a77660999dd3d12ab65f
URL:		http://www.openal.org/
BuildRequires:	OpenAL-devel >= 0.0.8-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free implementation of OpenAL's ALUT standard.

%description -l pl
Wolna implementacja standartu ALUT OpenALa.

%package devel
Summary:	Headers for freealut
Summary(pl):	Pliki nagłówkowe do freealuta
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenAL-devel >= 0.0.8-1

%description devel
freealut header files.

%description devel -l pl
Pliki nagłówkowe freealuta.

%package static
Summary:	Static alut library
Summary(pl):	Statyczna biblioteka alut
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static alut library.

%description static -l pl
Biblioteka alut do konsolidacji statycznej.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/libalut.so
%{_libdir}/*.la
%{_pkgconfigdir}/*
%{_includedir}/AL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
