Summary:	USB topology and device viewer
Summary(pl.UTF-8):	Przeglądarka topologii i urządzeń USB
Name:		usbview
Version:	2.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.kroah.com/linux/usb/%{name}-%{version}.tar.gz
# Source0-md5:	565f2e79f3924d14ab5b4d8aced557e5
URL:		http://www.kroah.com/linux/usb/
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	pkgconfig
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/usbview
%{_mandir}/man8/usbview.8*
