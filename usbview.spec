Summary:	USB topology and device viewer
Summary(pl.UTF-8):   Przeglądarka topologii i urządzeń USB
Name:		usbview
Version:	1.0
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.kroah.com/linux-usb/%{name}-%{version}.tar.gz
# Source0-md5:	2ac1bdae03a858b965e895b211a75ad7
URL:		http://www.kroah.com/linux-usb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.3
Requires:	gtk+ >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
USBView is a GTK+ program that displays the topography of the devices
that are plugged into the USB bus on a Linux machine. It also displays
information on each of the devices. This can be useful to determine if
a device is working properly or not.

%description -l pl.UTF-8
USBView to program w GTK+ wyświetlający topografię urządzeń
podłączonych do szyny USB w maszynie działającej pod Linuksem.
Wyświetla także informacje o każdym z urządzeń. Może to być przydatne
do stwierdzenia, czy dane urządzenie działa poprawnie, czy nie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/usbview
