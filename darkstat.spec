Summary:	Network statistics gatherer (packet sniffer)
Name:		darkstat
Version:	3.0.718
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dmr.ath.cx/net/darkstat/%{name}-%{version}.tar.bz2
# Source0-md5:	1fb31ac01d4689493c917fa622a002e7
URL:		http://dmr.ath.cx/net/darkstat/
BuildRequires:	libpcap-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
darkstat is a network statistics gatherer (and packet sniffer).
It captures network traffic, calculates statistics about usage,
and serves reports over HTTP.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules	\
	--with-chroot-dir=%{_datadir}/empty
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README export-format.txt
%attr(755,root,root) %{_sbindir}/darkstat
%{_mandir}/man8/darkstat.8*

