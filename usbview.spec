Summary:	USB topology and device viewer
Summary(pl):	Przegl±darka topologii i urz±dzeñ USB
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

%description -l pl
USBView to program w GTK+ wy¶wietlaj±cy topografiê urz±dzeñ
pod³±czonych do szyny USB w maszynie dzia³aj±cej pod Linuksem.
Wy¶wietla tak¿e informacje o ka¿dym z urz±dzeñ. Mo¿e to byæ przydatne
do stwierdzenia, czy dane urz±dzenie dzia³a poprawnie, czy nie.

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
%doc ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/usbview
