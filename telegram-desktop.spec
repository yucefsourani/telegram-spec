%global debug_package %{nil}
Name:           telegram-desktop
Version:        0.10.10
Release:        2%{?dist}
Summary:     	Telegram is a messaging app with a focus on speed and security
Group:		Applications/Internet
License:    	GPLv3    
URL:            https://telegram.org/
Source0:   	https://updates.tdesktop.com/tlinux32/tsetup32.%version.tar.xz     
Source1:	https://updates.tdesktop.com/tlinux/tsetup.%version.tar.xz	
Source2:	https://github.com/yucefsourani/telegram-spec/raw/master/telegram128.png
Source3:	https://raw.githubusercontent.com/yucefsourani/telegram-spec/master/telegram.desktop
BuildRequires:  desktop-file-utils
       

%description
Telegram is a messaging app with a focus on speed and security,
it’s super-fast, simple and free. You can use Telegram on all
your devices at the same time — your messages sync seamlessly
across any number of your phones, tablets or computers.


%prep
%ifarch %ix86
%setup -b0 -q -n Telegram
%endif

%ifarch x86_64 amd64
%setup -b1 -q -n Telegram
%endif


%build


%install
%{__mkdir} -p %{buildroot}%{_datadir}/%{name}
%{__mkdir} -p %{buildroot}%{_datadir}/pixmaps
%{__mkdir} -p %{buildroot}%{_datadir}/applications
%{__mkdir} -p %{buildroot}%{_bindir}

%{__cp} -arf ./Telegram %{buildroot}%{_datadir}/%{name}/telegram
%{__cp} %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

%{__ln_s} -f %{_datadir}/%{name}/telegram %{buildroot}%{_bindir}/telegram

%{__cp} %{SOURCE3} %{buildroot}%{_datadir}/%{name}.desktop
desktop-file-install                          \
--add-category="Network"                  \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/%{name}.desktop

%files
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/telegram
%{_datadir}/applications/telegram-desktop.desktop
%{_datadir}/pixmaps/telegram128.png
%{_bindir}/telegram



%changelog
* Mon Oct 03 2016 youcef sourani <youssef.m.sourani@gmail.com> - 0.10.10-2
- Update description

* Mon Oct 03 2016 youcef sourani <youssef.m.sourani@gmail.com> - 0.10.10-1
- Update To Version 0.10.10

* Fri Sep 23 2016 youcef sourani <youssef.m.sourani@gmail.com> - 0.10.8-1
- Update To Version 0.10.8

* Wed Sep 21 2016 youcef sourani youssef.m.sourani@gmail.com - 0.10.7-1
- Update To Version 0.10.7

* Sat Sep 17 2016 youcef sourani youssef.m.sourani@gmail.com - 0.10.6-1
- Initial For Fedora

