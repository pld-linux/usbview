Summary:	USB topology and device viewer
Name:		usbview
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Url:		http://www.kroah.com/linux-usb/
Source0:	http://www.kroah.com/linux-usb/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2.3

%description
USBView is a GTK program that displays the topography of the devices
that are plugged into the USB bus on a Linux machine. It also displays
information on each of the devices. This can be useful to determine if
a device is working properly or not.

%prep
%setup -q

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/usbview
