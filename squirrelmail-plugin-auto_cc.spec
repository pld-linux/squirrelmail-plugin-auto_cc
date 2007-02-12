%define		_plugin	auto_cc
%define		mversion	1.2
Summary:	Auto CC/BCC plugin for squirrelmail
Summary(pl.UTF-8):	Wtyczka pozwalająca ustawić automatyczne wysyłanie CC/BCC
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	259a001d964c7257be11bbb2b764ba52
URL:		http://www.squirrelmail.org/plugin_view.php?id=28
Requires:	squirrelmail >= 1.4.6-2
Requires:	squirrelmail-compatibility-2.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}

%description
This plugin allows users to specify a default list of CC and/or BCC
addresses that should be included on every email sent.

%description -l pl.UTF-8
Wtyczka pozwalająca użytkownikom na stworzenie listy adresów CC i/lub
BCC, które będą automatycznie dołączane do każdego wysłanego maila.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install *.php $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%dir %{_plugindir}
%{_plugindir}/*.php
