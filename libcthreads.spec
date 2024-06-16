# see m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support cross-platform C threads functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi wątków w C
Name:		libcthreads
Version:	20240413
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcthreads/releases
Source0:	https://github.com/libyal/libcthreads/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	e8de09740800c62f39c3dd35437c5c1b
URL:		https://github.com/libyal/libcthreads/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcthreads is a library to support cross-platform C thread functions.

%description -l pl.UTF-8
libcthreads to biblioteka wspierająca wieloplatformowe funkcje obsługi
wątków w C.

%package devel
Summary:	Header files for libcthreads library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcthreads
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}

%description devel
Header files for libcthreads library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcthreads.

%package static
Summary:	Static libcthreads library
Summary(pl.UTF-8):	Statyczna biblioteka libcthreads
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcthreads library.

%description static -l pl.UTF-8
Statyczna biblioteka libcthreads.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcthreads.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcthreads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcthreads.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcthreads.so
%{_includedir}/libcthreads
%{_includedir}/libcthreads.h
%{_pkgconfigdir}/libcthreads.pc
%{_mandir}/man3/libcthreads.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcthreads.a
